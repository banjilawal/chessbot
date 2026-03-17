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
    NoVisitForTerminationException, Square, SquareService, SquareState, SquareVisitorDisabledException,
    StartSquareVisitException, TerminateSquareVisitException, TokenVisitHandlerException,
    VisitingOccupiedSquareException, VisitingWrongOpeningSquareException, VisitorFromWrongBoardException
)
from logic.system import DeletionResult, LoggingLevelRouter, UpdateResult, ValidationResult
from logic.token import Token, TokenBoardState, TokenService


class DepartSquareProcess:
    """
    Role:Update Handler, Consistency, Integrity Maintenance, Lifecycle Management

    Responsibilities:
    1.  Ensure integrity and consistency are maintained during the  square's occupation lifecycle.

    Super Class:
   None

    Provides:


    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR ARGS:
    None

    # LOCAL METHODS:
        *   start_visit(token: Token, square: Square, square_validator: SquareValidator) -> UpdateResult[Square]
        *   terminate_visit(square: Square, square_validator: SquareValidator) -> DeletionResult[Token]

    # INHERITED METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            square: Square,
            square_service: SquareService = SquareService(),
    ) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  If the square fails its safety checks send and exception chain in the DeletionResult.
            2.  If the square is empty send an exception chain in the DeletionResult.
            3.  Store the square's occupant in a temp variable.
            4.  Set square.occupant to null and  square.state to empty.

        Args:
            square: Square
            square_service: SquareService
        Returns:
            DeletionResult[Token]
        Raises:
            TokenVisitHandlerException
            TerminateSquareVisitException
            NoVisitForTerminationException
        """
        method = "TokenVistHandler.terminate_visit"
        
        # Handle the case that, the square is not certified as safe.
        validation = square_service.validator.validate(candidate=square)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenVisitHandlerException(
                    msg=TokenVisitHandlerException.MSG,
                    err_code=TokenVisitHandlerException.ERR_CODE,
                    ex=TerminateSquareVisitException(
                        mthd=method,
                        op=TerminateSquareVisitException.OP,
                        msg=TerminateSquareVisitException.MSG,
                        err_code=TerminateSquareVisitException.ERR_CODE,
                        rslt_type=TerminateSquareVisitException.RSLT_TYPE,
                        ex=validation.exception,
                    )
                )
            )
        # Handle the case that, the square is empty.
        if square.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenVisitHandlerException(
                    msg=TokenVisitHandlerException.MSG,
                    err_code=TokenVisitHandlerException.ERR_CODE,
                    ex=TerminateSquareVisitException(
                        mthd=method,
                        op=TerminateSquareVisitException.OP,
                        msg=TerminateSquareVisitException.MSG,
                        err_code=TerminateSquareVisitException.ERR_CODE,
                        rslt_type=TerminateSquareVisitException.RSLT_TYPE,
                        ex=NoVisitForTerminationException(
                            val=square,
                            var=f"{square.name}",
                            msg=NoVisitForTerminationException.MSG,
                            err_code=NoVisitForTerminationException.ERR_CODE,
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
