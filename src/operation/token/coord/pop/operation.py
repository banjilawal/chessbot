# src/logic/token/service/operation/coord/exception.py

"""
Module: logic.token.service.operation.coord.operation
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations

from typing import cast

from logic.coord import Coord

from analyzer import TokenReadinessAnalyzer
from err import DisabledTokenManeuverException
from report import TokenReadinessReport
from system import DeletionResult, LoggingLevelRouter
from model.state.token import (
    InactiveTokenPoppingCoordException, MoveUndoLimitException, Token, TokenPopCoordException, TokenValidation,
    UnopenedTokenPoppingCoordException
)


class TokenPositionPopper:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Maintain the token's integrity and consistency when the last coord is popped.
        2.  Enforce chess constraints on coord popes.

    Attributes:

    Provides:
            -   execute(
                        token: Token,
                        token_validator: TokenValidator = TokenValidator(),
                ) -> DeletionResult[Coord]
    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            token_validator: TokenValidator | None = None,
            readiness_analyzer: TokenReadinessAnalyzer | None = None,
    ) -> DeletionResult[Coord]:
        """
        Forwards a request that the CoordDatabase instance removed its latest insert.

        Action:
            1.  Send an exception chain in the DeletionResult if:
                    *   The token is unsafe or not actionable.
                    *   It has no position history.
                    *   It has not moved from its opening square.
            2.  Otherwise, pop the last move and send the success result.
        Args:
            token: Token
            token_validator: TokenValidator
        Returns:
            DeletionResult[Coord]
        Raises:
            TokenPopCoordException
            MoveUndoLimitException
            TokenCoordHandlerException
            PoppingEmtpyCoordStackException
            InactiveTokenPoppingCoordException
            UnopenedTokenPoppingCoordException
        """
        method = f"{cls.__class__.__name__}undo_last_coord_push"
        
        if token_validator is None:
            token_validator = TokenValidation()
        if readiness_analyzer is None:
            readiness_analyzer = TokenReadinessAnalyzer()
            
        readiness_analysis_result = readiness_analyzer.analyze(
            token=token,
            token_validator=token_validator
        )
        # Handle the case that, the analyzer aborts.
        if readiness_analysis_result.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                TokenPopCoordException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenPopCoordException.OP,
                    msg=TokenPopCoordException.MSG,
                    err_code=TokenPopCoordException.ERR_CODE,
                    mthd_rslt_type=TokenPopCoordException.MTHD_RSLT,
                    ex=readiness_analysis_result.exception
                )
            )
        report = cast(TokenReadinessReport, readiness_analysis_result.payload)
        # Handle the case that, the token is not actionable.
        if report.token_is_not_ready:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                TokenPopCoordException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenPopCoordException.OP,
                    msg=TokenPopCoordException.MSG,
                    err_code=TokenPopCoordException.ERR_CODE,
                    mthd_rslt_type=TokenPopCoordException.MTHD_RSLT,
                    ex=DisabledTokenManeuverException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=DisabledTokenManeuverException.MSG,
                        err_code=DisabledTokenManeuverException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the token does not pass a validation check.
        validation_result = token_validator.build(token)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                TokenPopCoordException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenPopCoordException.OP,
                    msg=TokenPopCoordException.MSG,
                    err_code=TokenPopCoordException.ERR_CODE,
                    mthd_rslt_type=TokenPopCoordException.MTHD_RSLT,
                    ex=validation_result.exception
                )
            )
        # Handle the case that, token is not active
        if not token.is_active:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                TokenPopCoordException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenPopCoordException.OP,
                        msg=TokenPopCoordException.MSG,
                        err_code=TokenPopCoordException.ERR_CODE,
                        mthd_rslt_type=TokenPopCoordException.MTHD_RSLT,
                        ex=InactiveTokenPoppingCoordException(
                            var="token",
                            val=token.designation,
                            msg=InactiveTokenPoppingCoordException.MSG,
                            err_code=InactiveTokenPoppingCoordException.ERR_CODE,
                        )
                )
            )
        # Handle the case that, the active token has not opened.
        if token.positions.size == 1:
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return DeletionResult.failure(
                    TokenPopCoordException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenPopCoordException.OP,
                        msg=TokenPopCoordException.MSG,
                        err_code=TokenPopCoordException.ERR_CODE,
                        mthd_rslt_type=TokenPopCoordException.MTHD_RSLT,
                        ex=UnopenedTokenPoppingCoordException(
                            var="token",
                            val=token.designation,
                            msg=UnopenedTokenPoppingCoordException.MSG,
                            err_code=UnopenedTokenPoppingCoordException.ERR_CODE,
                        )
                    )
                )
        # Handle the case that, an attempt is made to undo more than one turn.
        if token.previous_coord == token.current_position:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                TokenPopCoordException(
                    cls_mthd=method,
                    op=TokenPopCoordException.OP,
                    msg=TokenPopCoordException.MSG,
                    err_code=TokenPopCoordException.ERR_CODE,
                    mthd_rslt_type=TokenPopCoordException.MTHD_RSLT,
                    ex=MoveUndoLimitException(
                        var=token.designation,
                        msg=MoveUndoLimitException.MSG,
                        err_code=MoveUndoLimitException.ERR_CODE,
                    )
                )
            )
        # --- Integrity are passed. ServiceRequest that, the CoordDatabase instance pop the last record. ---#
        popping_cord_stack_result = token.positions.pop()
        
        # Handle the case that, the pop was not completed.
        if popping_cord_stack_result.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                TokenPopCoordException(
                    cls_mthd=method,
                    op=TokenPopCoordException.OP,
                    msg=TokenPopCoordException.MSG,
                    err_code=TokenPopCoordException.ERR_CODE,
                    mthd_rslt_type=TokenPopCoordException.MTHD_RSLT,
                    ex=popping_cord_stack_result.exception
                )
            )
        # --- Forward the work product to the client. ---#
        return popping_cord_stack_result

