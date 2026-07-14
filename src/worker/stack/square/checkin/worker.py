# src/logic/square/database/kernel/operation/token/validator.py

"""
Module: logic.square.database.kernel.operation.token.service
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
from system import DeletionResult, LoggingLevelRouter, UpdateResult, ValidationResult
from model.state.token import Token, TokenService


class SquareStackDepartureWorker:
    """
    Role:Utilities, Update Management,

    Responsibilities:
    1.  Owns Token operations in SquareStackService.
    2.  Transfers Team.roster members to their opening squares.
    2.  Conducts update transactions for individual squares in the schema

    Super Class:
    None

    Provides:

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   SERVICE_NAME (str)
        *   roster_deployer (SquareStackRosterHandler)

    # INHERITED ATTRIBUTES:
    None

    Attributes:
        Local:
            *   id (int)
            *   schema (str)
            *   roster_deployer (SquareStackRosterHandler)
            
        Inherited:
        None

    # LOCAL METHODS:
        *   add_occupant(token: Token, square: Square, square_list: list[Square]) -> UpdateResult[Square]
        *   remove_occupant_by_search(occupant: Token, square_list: List[Square]) -> DeletionResult[Token]

    # INHERITED METHODS:
    None
    """
  
    @classmethod
    @LoggingLevelRouter.monitor
    def remove_occupant_from_stack(
            cls,
            occupant: Token,
            token_service: TokenService,
            square_stack: SquareStackService,
    ) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  If the search operation cannot certify the occupant is a valid token the exception chain will include.
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
        
        # Handle the case that, the token does not pass a validation check.
        token_validation = token_service.run.search_service(occupant)
        if token_validation.is_failure:
            # Send the debug exception to the client.
            return DeletionResult.failure(
                exception=SquareStackTokenHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareStackTokenHandlerException.MSG,
                    err_code=SquareStackTokenHandlerException.ERR_CODE,
                    ex=token_validation.exception
                )
            )
        # --- Find the square holding the token. There should be either zero or onne. ---#
        occupations = [square for square in square_stack.items if square.occupant == occupant]
        
        # Process the simplest case: No squares are holding the token.
        if len(occupations) == 0:
            return DeletionResult.nothing_to_delete()
        
        # Process the case: Some squares are holding the token
        return cls._eviction_handler(occupations, square_stack.microservice.square_service)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _eviction_handler(
            cls,
            occupied_squares: List[Square],
            square_service: SquareService = SquareService
    ) -> DeletionResult[Token]:
        """
        """
        method = "SquareService._eviction_handler"
        
        occupant = None
        # --- Expecting only one square in the list.  ---#
        for square in occupied_squares:
            # --- Handoff the deletion responsibility to square_validator. ---#
            deletion_result = square_service.remove_occupant(square)
            
            # Handle the case that, the removal is not completed.
            if deletion_result.is_failure:
                # Send the debug exception to the client.
                return DeletionResult.failure(
                    exception=SquareStackTokenHandlerException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
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
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _square_exists_and_is_safe(
            cls,
            square: Square,
            square_stack: SquareStackService
    ) -> ValidationResult[int]:
        method = "SquareStackDepartureWorker._safe_square_exists"
        
        # Handle the case that, the squareis not safe.
        square_validation = square_stack.microservice.run.execute(square)
        if square_validation.is_failure:
            return ValidationResult.failure(
                exception=SquareStackTokenHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareStackTokenHandlerException.MSG,
                    err_code=SquareStackTokenHandlerException.ERR_CODE,
                    ex=square_validation.exception
                )
            )
        if square not in square_stack.items:
            return ValidationResult.failure(
                exception=SquareStackTokenHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
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