# src/analyzer/promotion/manager/analyzer.py

"""
Module: analyzer.promotion.manager.analyzer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from analyzer import Analyzer, TokenReadinessAnalyzer
from err import PawnDoublePromotionException, PawnPromotionRowException, PromoteInactivePawnException
from err.analyzer.promotion import PromotionApprovalManagerException
from model import PawnToken
from report import PromotionApprovalManagerReport, TokenReadinessReport
from result import AnalysisResult, MethodResultType
from util import LoggingLevelRouter
from validator import TokenValidator


class PawnPromotionApprovalManager(Analyzer):
    """
    Role:
        -   Transaction Worker
        -   Consistency
        -   Integrity Maintenance
        -   Process Runner
        
    Responsibilities:
        1.  Pawn promotion exception owner.
        2.  Preserve original and updated data for rollbacks.
        3.  Ensure the pawn's integrity and consistency are maintained during the transaction.
        
    Attributes:
    
    Provides:
        -   execute(
                    rank: Rank,
                    pawn_token: PawnToken,
                    rank_service: RankService,
                    schema_service: SchemaService,
                    token_validator: TokenValidator
            ) -> UpdateResult[PawnToken]
            
    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            pawn: PawnToken,
            token_validator: TokenValidator | None = None,
            token_freedom_analyzer: TokenReadinessAnalyzer | None = None,
    ) -> AnalysisResult[PromotionApprovalManagerReport]:
        """
        Executes the promotion transaction.
        
        Action:
            1.  Send the unmodified pawn_token along with an exception chain in the UpdateResult if:
                    *   The token is not certified as a safe, actionable PawnToken.
                    *   The pawn_token is already promoted.
                    *   Is not on its enemy's rank_row.
                    *   The new rank is either King or Pawn.
            2.  Otherwise:
                    *   Make a deepcopy of the pawn_token to pre_update_pawn_token.
                    *   Set the new rank
                    *   Set the pawn_token's promotion_state to PromotionState.PROMOTED.
            3.  Send the success result containing, the finished work product.
        Args:
            pawn: PawnToken
            token_validator: TokenValidator
            token_freedom_analyzer: TokenFreedomAnalyzer
        Returns:
            AnalysisResult[PromotionReport]
        Raises:
            PawnPromotionAnalyzerException
            PromoteInactivePawnException
            PawnDoublePromotionException
            PawnPromotionRowException
            TypeError
        """
        method = f"{cls.__class__.__name__}.promote"
        
        # --- Supply any missing dependencies. ---#
        if token_freedom_analyzer is None:
            token_freedom_analyzer = TokenReadinessAnalyzer()
        if token_validator is None:
            token_validator = TokenValidator()
            
        analysis_result = token_freedom_analyzer.execute(
            token=pawn,
            token_validator=token_validator
        )
        # Handle the case that, the freedom analysis is not completed.
        if analysis_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                PromotionApprovalManagerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PromotionApprovalManagerException.MSG,
                    err_code=PromotionApprovalManagerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=analysis_result.exception
                )
            )
        report = cast(TokenReadinessReport, analysis_result.payload)
        
        # Handle the case that, the token is not free.
        if report.token_is_not_ready:
            # Send the exception chain on failure.
            return AnalysisResult.completed(
                PromotionApprovalManagerReport.deny_promotion(
                    PromoteInactivePawnException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=PromoteInactivePawnException.MSG,
                        err_code=PromoteInactivePawnException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the token is not a PawnToken.
        if not isinstance(pawn, PawnToken):
            return AnalysisResult.completed(
                PromotionApprovalManagerReport.deny_promotion(
                    TypeError(
                        f"Expected type PawnToken for promotion. "
                        f"Got {type(pawn).__name__} instead."
                    )
                )
            )
        # Handle the case that, the pawn_token has already been promoted.
        if pawn.is_promoted:
            return AnalysisResult.completed(
                PromotionApprovalManagerReport.deny_promotion(
                    PawnDoublePromotionException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=PawnDoublePromotionException.MSG,
                        err_code=PawnDoublePromotionException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the is not on its promotion row..
        if pawn.current_position.row != pawn.team.enemy_rank_row:
            return AnalysisResult.completed(
                PromotionApprovalManagerReport.deny_promotion(
                    PawnPromotionRowException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        var=pawn.designation,
                        msg=PawnPromotionRowException.MSG,
                        err_code=PawnPromotionRowException.ERR_CODE,
                    )
                )
            )
        # --- Send the work product. ---#
        return AnalysisResult.completed(
            PromotionApprovalManagerReport.approve_promotion(pawn)
        )
