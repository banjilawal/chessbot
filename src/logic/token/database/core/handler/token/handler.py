# src/logic/token/database/core/handler/token/service.py

"""
Module: logic.token.database.core.handler.token.service
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy
from typing import List

from logic.token import (
    TokenStackTokenHandlerException,  Token, VisitDestinationNotFoundException, TokenService, TokenStackService
)
from logic.system import DeletionResult, LoggingLevelRouter, UpdateResult, ValidationResult
from logic.token import Token, TokenService


class TokenStackTokenHandler:
    """
    # ROLE: Utilities, Update Management,

    # RESPONSIBILITIES:
    1.  Owns Token operations in TokenStackService.
    2.  Transfers Team.roster members to their opening tokens.
    2.  Conducts update transactions for individual tokens in the stack

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   SERVICE_NAME (str)
        *   roster_deployer (TokenStackRosterHandler)

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
        Local:
            *   id (int)
            *   name (str)
            *   roster_deployer (TokenStackRosterHandler)
            
        Inherited:
        None

    # LOCAL METHODS:
        *   add_occupant(token: Token, token: Token, token_list: list[Token]) -> UpdateResult[Token]
        *   remove_occupant_by_search(occupant: Token, token_list: List[Token]) -> DeletionResult[Token]

    # INHERITED METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def occupy_stack_token(
            cls,
            token: Token,
            token: Token,
            token_stack: TokenStackService,
            token_service: TokenService = TokenService(),
    ) -> UpdateResult[Token]:
        """
        # ACTION:
            1.  If token_service cannot verify the occupation candidate is actionable send the wrapped exception
                in the InsertionResult.
            2.  If the token either:
                    *   Fails validation.
                    *   Searching for it in the database raises an error.
                    *   The token is not in the database.
                send the wrapped exception in the InsertionResult.
            3.  If the occupation fails send the wrapped exception in the InsertionResult.
            4.  Add an entry for the occupant in the token_map then send the success InsertionResult.
        # PARAMETERS:
            *   token (Token)
            *   token (Token)
            *   token_service (TokenService)
        # RETURN:
            *   DeletionResult[Token] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
                    - On occupant not found: Empty DeletionResult.
        Raises:
            *   TokenDatabaseException
            *   TokenToOccupyNotFoundException
            *   StartTokenVisitException
        """
        method = "TokenStackTokenHandler.occupy_stack_token"
        
        # Handle the case that either the token does not or is not safe.
        token_verification_result = cls._token_exists_and_is_safe(token=token, token_stack=token_stack)
        if token_verification_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=token,
                exception=TokenStackTokenHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenStackTokenHandlerException.MSG,
                    err_code=TokenStackTokenHandlerException.ERR_CODE,
                    ex=token_verification_result.exception
                )
            )
        # --- After the token is validated, get a snapshot of its pre-update state. then call visit handler.---#
        pre_update_token = deepcopy(token)
        update_result = token_stack.integrity_service.token_visit_handler.start_visit(
            token=token,
            token=token,
            token_service=token_service,
        )
        # Handle the case that the token is not updated.
        if update_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_token,
                exception=TokenStackTokenHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenStackTokenHandlerException.MSG,
                    err_code=TokenStackTokenHandlerException.ERR_CODE,
                    ex=update_result.exception
                    )
            )
        # --- Send the success result to the client. ---#
        return UpdateResult.update_success(original=pre_update_token, updated=token)
   
    @classmethod
    @LoggingLevelRouter.monitor
    def remove_occupant_from_stack(
            cls,
            occupant: Token,
            token_service: TokenService,
            token_stack: TokenStackService,
    ) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  If the search handler cannot certify the occupant is a valid token the exception chain will include.
                TokenVerificationFailedException.
            2.  If the token is not found in any of the tokens send a nothing_to_delete result.
            3.  If the token was found in a token but the removal failed send the wrapped exception in the
                DeletionResult.
            4.  When the token is successfully removed from the token remove its entry from the token_map then
                send the ejected token in the DeletionResult.
        # PARAMETERS:
            *   occupant (Token)
        # RETURN:
            *   DeletionResult[Token] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
                    - On occupant not found: Empty DeletionResult.
        Raises:
            *   TokenDatabaseException
            *   DeleteTokenBySearchException
        """
        method = "TokenService.remove_occupant_from_stack"
        
        # Handle the case that, the token is not certified as safe.
        token_validation = token_service.validator.validate(occupant)
        if token_validation.is_failure:
            # Send the debug exception to the client.
            return DeletionResult.failure(
                exception=TokenStackTokenHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenStackTokenHandlerException.MSG,
                    err_code=TokenStackTokenHandlerException.ERR_CODE,
                    ex=token_validation.exception
                )
            )
        # --- Find the token holding the token. There should be either zero or onne. ---#
        occupations = [token for token in token_stack.items if token.occupant == occupant]
        
        # Process the simplest case: No tokens are holding the token.
        if len(occupations) == 0:
            return DeletionResult.nothing_to_delete()
        
        # Process the case: Some tokens are holding the token
        return cls._eviction_handler(occupations, token_stack.integrity_service.token_service)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _eviction_handler(
            cls,
            occupied_tokens: List[Token],
            token_service: TokenService = TokenService
    ) -> DeletionResult[Token]:
        """
        """
        method = "TokenService._eviction_handler"
        
        occupant = None
        # --- Expecting only one token in the list.  ---#
        for token in occupied_tokens:
            # --- Handoff the deletion responsibility to token_service. ---#
            deletion_result = token_service.remove_occupant(token)
            
            # Handle the case that, the removal is not completed.
            if deletion_result.is_failure:
                # Send the debug exception to the client.
                return DeletionResult.failure(
                    exception=TokenStackTokenHandlerException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenStackTokenHandlerException.MSG,
                        err_code=TokenStackTokenHandlerException.ERR_CODE,
                        ex=deletion_result.exception
                    )
                )
            occupant = deletion_result.payload
        # --- After the loop completes return the success result to the client. ---#
        if occupant is None:
            return DeletionResult.nothing_to_delete()
        return DeletionResult.success(payload=occupant)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _token_exists_and_is_safe(
            cls,
            token: Token,
            token_stack: TokenStackService
    ) -> ValidationResult[int]:
        method = "TokenStackTokenHandler._safe_token_exists"
        
        # Handle the case that, the token is not certified safe.
        token_validation = token_stack.integrity_service.validator.validate(token)
        if token_validation.is_failure:
            return ValidationResult.failure(
                exception=TokenStackTokenHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenStackTokenHandlerException.MSG,
                    err_code=TokenStackTokenHandlerException.ERR_CODE,
                    ex=token_validation.exception
                )
            )
        if token not in token_stack.items:
            return ValidationResult.failure(
                exception=TokenStackTokenHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenStackTokenHandlerException.MSG,
                    err_code=TokenStackTokenHandlerException.ERR_CODE,
                    ex=VisitDestinationNotFoundException(
                        var="token",
                        val=f"{token.name}",
                        msg=VisitDestinationNotFoundException.MSG,
                        err_code=VisitDestinationNotFoundException.ERR_CODE,
                    )
                )
            )
        return ValidationResult.success(1)