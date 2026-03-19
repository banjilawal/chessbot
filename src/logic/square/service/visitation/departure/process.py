# src/logic/square/service/visitation/departure/process.py

"""
Module: logic.square.service.visitation.departure.process
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations

from logic.token import Token
from logic.system import DeletionResult, LoggingLevelRouter
from logic.square import (
    DepartingEmptySquareException, Square, SquareDepartureException, SquareValidationProcess, SquareState
)

class SquareDepartureProcess:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner
        
    Responsibilities:
        1.  Square departure process owner.
        2.  Ensure both the token and the squares are consistent throughout
            square departure lifecycle.

    Attributes:

    Provides:
        -   execute(
                    square: Square,
                    square_validator: SquareValidationProcess,
            ) -> DeletionResult[Token]

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            square: Square,
            square_validator: SquareValidationProcess = SquareValidationProcess(),
    ) -> DeletionResult[Token]:
        """
        Takes the token out of the square.

        Action:
            1.  Send  an exception chain in the DeletionResult if:
                    -   The square is not certified as safe.
                    -   The square is empty.
            2.  Otherwise:
                    -   Store the occupant before setting square.occupant null.
                    -   Update the state to empty
            3.  Send the success result.
        Args:
            square: Square
            square_validator: SquareValidationProcess
        Returns:
            DeletionResult[Token]
        Raises:
            SquareDepartureException
            DepartingEmptySquareException
        """
        method = f"{cls.__name__}.execute"
        
        # Handle the case that, the square is not certified as safe.
        validation_result = square_validator.validator.validate(candidate=square)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareDepartureException(
                        mthd=method,
                        op=SquareDepartureException.OP,
                        msg=SquareDepartureException.MSG,
                        err_code=SquareDepartureException.ERR_CODE,
                        rslt_type=SquareDepartureException.RSLT_TYPE,
                        ex=validation_result.exception,
                )
            )
        # Handle the case that, the square is empty.
        if square.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareDepartureException(
                        mthd=method,
                        op=SquareDepartureException.OP,
                        msg=SquareDepartureException.MSG,
                        err_code=SquareDepartureException.ERR_CODE,
                        rslt_type=SquareDepartureException.RSLT_TYPE,
                        ex=DepartingEmptySquareException(
                            val=square,
                            var=f"{square.name}",
                            msg=DepartingEmptySquareException.MSG,
                            err_code=DepartingEmptySquareException.ERR_CODE,
                        )
                )
            )
        # --- Process the removal logic that maintains integrity and consistency. ---#
        
        # Store the square's occupant.
        token = square.occupant
        # Break the relationship between them and update the square's state.
        square.occupant = None
        square.state = SquareState.EMPTY
        
        # --- Send the work product. ---#
        DeletionResult.success(payload=token)
