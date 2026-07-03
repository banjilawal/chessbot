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
from model.token import Token, TokenService


class SquareStackOccupationWorker(Worker):
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
    def work(
            cls,
            token: Token,
            square: Square,
            square_stack: SquareStackService,
            token_service: TokenService = TokenService(),
    ) -> UpdateResult[Square]:
        """
        # ACTION:
            1.  If token_service cannot verify the occupation rank is actionable send the wrapped exception
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
            *   SquareEntryException
        """
        method = "SquareStackOccupationWorker.occupy_stack_square"
        
        # Handle the case that either the square does not or is not safe.
        square_verification_result = cls._square_exists_and_is_safe(square=square, square_stack=square_stack)
        if square_verification_result.is_failure:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=square,
                exception=SquareStackTokenHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareStackTokenHandlerException.MSG,
                    err_code=SquareStackTokenHandlerException.ERR_CODE,
                    ex=square_verification_result.exception
                )
            )
        # --- After the square is validated, get a snapshot of its pre-update state. then call visit operation.---#
        pre_update_square = deepcopy(square)
        update_result = square_stack.microservice.token_visit_handler.start_visit(
            token=token,
            square=square,
            token_service=token_service,
        )
        # Handle the case that the square is not updated.
        if update_result.is_failure:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_square,
                exception=SquareStackTokenHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareStackTokenHandlerException.MSG,
                    err_code=SquareStackTokenHandlerException.ERR_CODE,
                    ex=update_result.exception
                    )
            )
        # --- Send the success result to the client. ---#
        return UpdateResult.update_success(original=pre_update_square, updated=square)

    
    @classmethod
    @LoggingLevelRouter.monitor
    def _square_exists_and_is_safe(
            cls,
            square: Square,
            square_stack: SquareStackService
    ) -> ValidationResult[int]:
        method = "SquareStackOccupationWorker._safe_square_exists"
        
        # Handle the case that, the squareis not safe.
        square_validation = square_stack.microservice.validator.build(square)
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