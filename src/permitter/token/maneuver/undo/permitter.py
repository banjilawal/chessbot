# src/permitter/token/maneuver/undo/permitter.py

"""
Module: permitter.token.maneuver.undo.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from logic.coord import Coord

from analyzer import TokenReadinessAnalyzer
from err import DisabledTokenManeuverException
from permitter import TokenManeuverPermitter
from report import PopApproval, TokenReadinessReport
from system import AnalysisResult, LoggingLevelRouter
from model.token import (
    InactiveTokenPoppingCoordException, MoveUndoLimitException, Token, TokenPopCoordException, TokenValidation,
    UnopenedTokenPoppingCoordException
)
from validation import TokenValidator


class TokenUndoMovePermitter(TokenManeuverPermitter):
    """
    Role:
        - Permission Granter
        - Consistency, Integrity Maintenance

    Responsibilities:
        1.  Determine if Token can undo its last move.

    Attributes:

    Provides:
        -   def execute(cls,token: Token, *args, **kwargs) -> AnalysisResult

    Super Class:
        TokenManeuverPermitter
    """
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
        -   def execute(
                    cls,
                    token: Token,
                    token_validator: TokenValidator | None = None,
                    readiness_analyzer: TokenReadinessAnalyzer | None = None,
            ) -> AnalysisResult[Coord]
    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            token_validator: TokenValidator | None = None,
            readiness_analyzer: TokenReadinessAnalyzer | None = None,
    ) -> AnalysisResult[PopApproval]:
        """
        Forwards a request that the CoordDatabase instance removed its latest insert.

        Action:
            1.  Send an exception chain in the AnalysisResult if:
                    *   The token is unsafe or not actionable.
                    *   It has no position history.
                    *   It has not moved from its opening square.
            2.  Otherwise, pop the last move and send the success result.
        Args:
            token: Token
            token_validator: TokenValidator
        Returns:
            AnalysisResult[Coord]
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
            return AnalysisResult.aborted(
                    TokenPopCoordException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPopCoordException.MSG,
                    err_code=TokenPopCoordException.ERR_CODE,
                    ex=readiness_analysis_result.exception
                )
            )
        report = cast(TokenReadinessReport, readiness_analysis_result.payload)
        # Handle the case that, the token is not actionable.
        if report.token_is_not_ready:
            # Send the exception chain on failure.
            return AnalysisResult.completed(
                PopApproval.deny(
                    exception=TokenPopCoordException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenPopCoordException.MSG,
                        err_code=TokenPopCoordException.ERR_CODE,
                        ex=DisabledTokenManeuverException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=DisabledTokenManeuverException.MSG,
                            err_code=DisabledTokenManeuverException.ERR_CODE,
                        )
                    )
                )
            )
        # Handle the case that, the active token has not opened.
        if token.positions.size == 1:
            # Send the exception chain on failure.
            return AnalysisResult.completed(
                PopApproval.deny(
                    exception=TokenPopCoordException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenPopCoordException.MSG,
                        err_code=TokenPopCoordException.ERR_CODE,
                        ex=DisabledTokenManeuverException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=DisabledTokenManeuverException.MSG,
                            err_code=DisabledTokenManeuverException.ERR_CODE,
                        )
                    )
                )
            )
        # Handle the case that, an attempt is made to undo more than one turn.
        if token.previous_coord == token.current_position:
            # Send the exception chain on failure.
            return AnalysisResult.completed(
                PopApproval.deny(
                    exception=TokenPopCoordException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenPopCoordException.MSG,
                        err_code=TokenPopCoordException.ERR_CODE,
                        ex=MoveUndoLimitException(
                            var=token.designation,
                            msg=MoveUndoLimitException.MSG,
                            err_code=MoveUndoLimitException.ERR_CODE,
                        )
                    )
                )
            )
        return AnalysisResult.completed(PopApproval.approve(token.positions.))
        

