# src/logic/square/database/core/handler/token/service.py

"""
Module: logic.square.database.core.handler.token.service
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy
from typing import List

from logic.square import (
    SquareStackTokenHandlerException,  Square, VisitDestinationNotFoundException, SquareService, SquareStackService
)
from logic.system import DeletionResult, IdFactory, LoggingLevelRouter, UpdateResult, ValidationResult
from logic.token import Token, TokenService


class SquareStackTokenHandler:
    """
    # ROLE: Utilities, Update Management,

    # RESPONSIBILITIES:
    1.  Owns Token operations in SquareStackService.
    2.  Transfers Team.roster members to their opening squares.
    2.  Conducts update transactions for individual squares in the stack

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   SERVICE_NAME (str)
        *   roster_deployer (SquareStackRosterHandler)

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
        Local:
            *   id (int)
            *   name (str)
            *   roster_deployer (SquareStackRosterHandler)
            
        Inherited:
        None

    # LOCAL METHODS:
        *   add_occupant(token: Token, square: Square, square_list: list[Square]) -> UpdateResult[Square]
        *   remove_occupant_by_search(occupant: Token, square_list: List[Square]) -> DeletionResult[Token]

    # INHERITED METHODS:
    None
    """
    
    @LoggingLevelRouter.monitor
    def occupy_stack_square(
            self,
            token: Token,
            square: Square,
            stack: SquareStackService,
    ) -> UpdateResult[Square]:
        """
        # ACTION:
            1.  If token_service cannot verify the occupation candidate is actionable send the wrapped exception
                in the InsertionResult.
            2.  If the square either:
                    *   Fails validation.
                    *   Searching for it in the database raises an error.
                    *   The square is not in the database.
                send the wrapped exception in the InsertionResult.
            3.  If the occupation fails send the wrapped exception in the InsertionResult.
            4.  Add an entry for the occupant in the token_map then send the success InsertionResult.
        # PARAMETERS:
            *   token (Token)
            *   square (Square)
            *   token_service (TokenService)
        # RETURN:
            *   DeletionResult[Token] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
                    - On occupant not found: Empty DeletionResult.
        Raises:
            *   SquareDatabaseException
            *   SquareToOccupyNotFoundException
            *   StartSquareVisitException
        """
        method = "SquareStackTokenHandler.occupy_stack_square"
        
        # Handle the case that either the square does not or is not safe.
        square_verification_result = self.square_exists_and_is_safe(square, stack)
        if square_verification_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=SquareStackTokenHandlerException(
                    cls_mthd=method,
                    cls_name=self.__name__,
                    msg=SquareStackTokenHandlerException.MSG,
                    err_code=SquareStackTokenHandlerException.ERR_CODE,
                    ex=square_verification_result.exception
                )
            )
        # --- After the square is validated, get a snapshot of its pre-update state. then call visit handler.---#
        pre_update_square = deepcopy(square)
        update_result = stack.integrity_service.token_visit_handler.start_visit(
            token=token,
            square=square
        )
        # Handle the case that the square is not updated.
        if update_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_square,
                exception=SquareStackTokenHandlerException(
                    cls_mthd=method,
                    cls_name=self.__name__,
                    msg=SquareStackTokenHandlerException.MSG,
                    err_code=SquareStackTokenHandlerException.ERR_CODE,
                    ex=update_result.exception
                    )
            )
        # --- Send the success result to the client. ---#
        return UpdateResult.update_success(original=pre_update_square, updated=square)
    
    @LoggingLevelRouter.monitor
    def remove_occupant_from_stack(
            self,
            occupant: Token,
            stack: SquareStackService,
            token_service: TokenService = TokenService(),
    ) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  If the search handler cannot certify the occupant is a valid token the exception chain will include.
                TokenVerificationFailedException.
            2.  If the token is not found in any of the squares send a nothing_to_delete result.
            3.  If the token was found in a square but the removal failed send the wrapped exception in the
                DeletionResult.
            4.  When the token is successfully removed from the square remove its entry from the token_map then
                send the ejected token in the DeletionResult.
        # PARAMETERS:
            *   occupant (Token)
        # RETURN:
            *   DeletionResult[Token] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
                    - On occupant not found: Empty DeletionResult.
        Raises:
            *   SquareDatabaseException
            *   DeleteTokenBySearchException
        """
        method = "SquareService.remove_occupant_from_stack"
        
        # Handle the case that, the token is not certified as safe.
        token_validation = token_service.validator.validate(occupant)
        if token_validation.is_failure:
            # Send the debug exception to the client.
            return DeletionResult.failure(
                exception=SquareStackTokenHandlerException(
                    cls_mthd=method,
                    cls_name=self.__name__,
                    msg=SquareStackTokenHandlerException.MSG,
                    err_code=SquareStackTokenHandlerException.ERR_CODE,
                    ex=token_validation.exception
                )
            )
        # --- Find the square holding the token. There should be either zero or onne. ---#
        occupations = [square for square in stack.items if square.occupant == occupant]
        
        # Process the simplest case: No squares are holding the token.
        if len(occupations) == 0:
            return DeletionResult.nothing_to_delete()
        
        # Process the case: Some squares are holding the token
        return self._eviction_handler(occupations, stack.integrity_service.square_service)
    
    def _eviction_handler(
            self,
            occupied_squares: List[Square],
            square_service: SquareService = SquareService()
    ) -> DeletionResult[Token]:
        """
        """
        method = "SquareService._eviction_handler"
        occupant: Token = None
        # --- Expecting only one square in the list.  ---#
        for square in occupied_squares:
            # --- Handoff the deletion responsibility to square_service. ---#
            deletion_result = square_service.remove_occupant(square)
            
            # Handle the case that, the removal is not completed.
            if deletion_result.is_failure:
                # Send the debug exception to the client.
                return DeletionResult.failure(
                    exception=SquareStackTokenHandlerException(
                        cls_mthd=method,
                        cls_name=self.__name__,
                        msg=SquareStackTokenHandlerException.MSG,
                        err_code=SquareStackTokenHandlerException.ERR_CODE,
                        ex=deletion_result.exception
                    )
                )
            occupant = deletion_result.payload
        # --- After the loop completes return the success result to the client. ---#
        if occupant is None:
            return DeletionResult.nothing_to_delete()
        return DeletionResult.success(payload=occupant)
    
    def square_exists_and_is_safe(
            self,
            square: Square,
            square_stack: SquareStackService
    ) -> ValidationResult[int]:
        method = "SquareStackTokenHandler._safe_square_exists"
        # Handle the case that, the square is not certified safe.
        square_validation = square_stack.integrity_service.validator.validate(square)
        if square_validation.is_failure:
            return ValidationResult.failure(
                exception=SquareStackTokenHandlerException(
                    cls_mthd=method,
                    cls_name=self.__name__,
                    msg=SquareStackTokenHandlerException.MSG,
                    err_code=SquareStackTokenHandlerException.ERR_CODE,
                    ex=square_validation.exception
                )
            )
        if square not in square_stack.items:
            return ValidationResult.failure(
                exception=SquareStackTokenHandlerException(
                    cls_mthd=method,
                    cls_name=self.__name__,
                    msg=SquareStackTokenHandlerException.MSG,
                    err_code=SquareStackTokenHandlerException.ERR_CODE,
                    ex=VisitDestinationNotFoundException(
                        var="square",
                        val=f"{square.name}",
                        msg=VisitDestinationNotFoundException.MSG,
                        err_code=VisitDestinationNotFoundException.ERR_CODE,
                    )
                )
            )
        return ValidationResult.success(1)