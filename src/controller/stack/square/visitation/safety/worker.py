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