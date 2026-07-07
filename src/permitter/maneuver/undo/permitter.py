# src/permitter/token/maneuver/undo/permitter.py

"""
Module: permitter.token.maneuver.undo.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from analyzer import TokenReadinessAnalyzer
from err import (
    DisabledTokenUndoMoveException, MaxMoveUndoException, UndeployedTovenMoveException,
    TokenUndoMovePermitterException
)
from model import Token
from permitter import TokenManeuverPermitter
from report import PopApprovalReport, TokenReadinessReport
from result import AnalysisResult
from util import LoggingLevelRouter
from validator import TokenValidator


class TokenUndoMovePermitter(TokenManeuverPermitter):
    """
    Role:
        - Permission Granter
        - Consistency, Integrity Maintenance

    Responsibilities:
        1.  Determine if Token can undo its last move.

    Attributes:

    Provides:
        -   def execute(
                    cls,
                    token: Token,
                    token_validator: TokenValidator | None = None,
                    readiness_analyzer: TokenReadinessAnalyzer | None = None,
            ) -> AnalysisResult[Coord]
    Super Class:
        TokenManeuverPermitter
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def run(
            cls,
            requestor: Token,
            token_validator: TokenValidator | None = None,
            readiness_analyzer: TokenReadinessAnalyzer | None = None,
    ) -> AnalysisResult[PopApprovalReport]:
        """
        Forwards a request that the CoordDatabase instance removed its latest insert.

        Action:
            1.  Send an exception chain in the AnalysisResult if:
                    -   The readiness_analyzer aborts.
            2.  Deny UndoMove permission if any of the following occur.
                    -   The token is not free.
                    -   It has already undone one move during its turn.
            3.  If none of the conditions in (2) apply approve the request.
        Args:
            requestor: Token,
            token_validator: TokenValidator
            readiness_analyzer: TokenReadinessAnalyzer
        Returns:
            AnalysisResult[PopApproval]
        Raises:
            TokenUndoMovePermitterException
            DisabledTokenUndoMoveException
            MaxMoveUndoException
        """
        method = f"{cls.__class__.__name__}.execute"
        
        # --- Supply missing dependencies. ---#
        if token_validator is None:
            token_validator = TokenValidator()
        if readiness_analyzer is None:
            readiness_analyzer = TokenReadinessAnalyzer()
            
        readiness_analysis_result = readiness_analyzer.execute(
            token=requestor,
            token_validator=token_validator
        )
        # Handle the case that, the analyzer aborts.
        if readiness_analysis_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.aborted(
                    TokenUndoMovePermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenUndoMovePermitterException.MSG,
                    err_code=TokenUndoMovePermitterException.ERR_CODE,
                    ex=readiness_analysis_result.exception
                )
            )
        report = cast(TokenReadinessReport, readiness_analysis_result.payload)
        # Handle the case that, the token is not actionable.
        if report.token_is_not_ready:
            # Send the exception chain on failure.
            return AnalysisResult.completed(
                PopApprovalReport.deny(
                    exception=TokenUndoMovePermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenUndoMovePermitterException.MSG,
                        err_code=TokenUndoMovePermitterException.ERR_CODE,
                        ex=DisabledTokenUndoMoveException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=DisabledTokenUndoMoveException.MSG,
                            err_code=DisabledTokenUndoMoveException.ERR_CODE,
                        )
                    )
                )
            )
        # Handle the case that, an attempt is made to undo more than one turn.
        if requestor.previous_coord == requestor.current_position:
            # Send the exception chain on failure.
            return AnalysisResult.completed(
                PopApprovalReport.deny(
                    exception=TokenUndoMovePermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenUndoMovePermitterException.MSG,
                        err_code=TokenUndoMovePermitterException.ERR_CODE,
                        ex=MaxMoveUndoException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=MaxMoveUndoException.MSG,
                            err_code=MaxMoveUndoException.ERR_CODE,
                        )
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return AnalysisResult.completed(PopApprovalReport.approve(token.positions.))
        

