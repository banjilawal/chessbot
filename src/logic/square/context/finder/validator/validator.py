# src/logic/square/validator/validator.py

"""
Module: logic.square.validator
Author: Banji Lawal
Created: 2025-09-11
"""

from __future__ import annotations
from typing import Any, List, cast

from logic.board import BoardService
from logic.square import (
    Square, SquareDataSourceEmptyException, SquareDataSourceNullException, SquareValidationException
)
from logic.system import LoggingLevelRouter, ValidationResult, Validator


class SquareListValidator(Validator[List[Square]]):
    """
    Role:
        - Data Integrity Worker
        - Exception Chain Layer 1
        - Exception Messaging

    Responsibilities:
        1.  Verifies that mission-critical operations that need a non-empty List[Square] get one.

    Attributes:

    Provides:
        -   validate(
                    candidate: Any,
                    board_service: BoardService = BoardService(),
                    coord_service: CoordService = CoordService(),
                    identity_service: IdentityService = IdentityService(),
            ) -> ValidationResult[[List[Square]]

    Super:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[List[Square]]:
        """
        Tests if a squareFinder is getting a List[Square]

        Args:
            1.  Send an exception chain in the ValidationResult if:
                    -   The candidate is null
                    -   Is not a List.
                    -   Is an empty list.
                    -   If the first item is not a Square.
            2.  Otherwise, send the success result.
        # Args:
            candidate: Any
        # RETURNS:
            ValidationResult[List[Square]]
        Raises:
            -   TypeError
            -   SquareDataSourceNullException
            -   SquareDataSourceEmptyException
        """
        method = f"{cls.__name__}.validate_dataset"
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    rslt_type=SquareValidationException.RSLT_TYPE,
                    ex=SquareDataSourceNullException(
                        msg=SquareDataSourceNullException.MSG,
                        err_code=SquareDataSourceNullException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, List):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    rslt_type=SquareValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected type{List.__name__}, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast the candidate to a List for additional tests. ---#
        square_list = cast(List, candidate)
        
        # Handle the case that, the list is empty
        if len(square_list) == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    rslt_type=SquareValidationException.RSLT_TYPE,
                    ex=SquareDataSourceEmptyException(
                        msg=SquareDataSourceEmptyException.MSG,
                        err_code=SquareDataSourceEmptyException.ERR_CODE
                    )
                )
            )
        # Handle the case that, the list does not contain squares.
        if not isinstance(square_list[0], Square):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    rslt_type=SquareValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Searching for squares in a dataset of {type(square_list[0]).__name__}."
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(square_list)


