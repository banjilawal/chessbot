# src/logic/square/service/visitation/departure/process.py

"""
Module: logic.square.service.visitation.departure.process
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from copy import deepcopy

from logic.square import (
    DepartingEmptySquareException, Square, SquareService, SquareState, SquareVisitorDisabledException,
    StartSquareVisitException, SquareDepartureException, TokenVisitHandlerException,
    VisitingOccupiedSquareException, VisitingWrongOpeningSquareException, VisitorFromWrongBoardException
)
from logic.system import DeletionResult, LoggingLevelRouter, DeletionResult, validation_resultResult
from logic.token import Token, TokenBoardState, TokenService


class DepartSquareProcess:
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
                    square_service: SquareService,
            ) -> DeletionResult[Token]

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            square: Square,
            square_service: SquareService = SquareService(),
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
            square_service: SquareService
        Returns:
            DeletionResult[Token]
        Raises:
            TokenVisitHandlerException
            SquareDepartureException
            DepartingEmptySquareException
        """
        method = f"{cls.__name__}.execute"
        
        # Handle the case that, the square is not certified as safe.
        validation_result = square_service.validator.validate(candidate=square)
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
            )
        # --- Process the removal logic that maintains integrity and consistency. ---#
        
        # Store the square's occupant.
        token = square.occupant
        
        # Break the relationship between the square and the token then update the square's state.
        square.occupant = None
        square.state = SquareState.EMPTY
        
        # --- Send the success result to the client. ---#
        DeletionResult.success(payload=token)
