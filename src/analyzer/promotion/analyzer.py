# src/analyzer/promotion/analyzer.py

"""
Module: analyzer.promotion.analyzer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from copy import deepcopy
from typing import cast

from logic.rank import King, Pawn, Rank, RankService

from analyzer import Analyzer, TokenFreedomAnalyzer
from model.catalog import SchemaService
from report import TokenFreedomReport
from report.promote.report import PromotionApprovalReport
from result import AnalysisResult
from util import LoggingLevelRouter, UpdateResult
from model.token import (
    PawnAlreadyPromotedException, PawnPromotionRowException, PawnToken, PromoteInactivePawnException,
    PromoteToPawnException, PawnPromotionAnalyzerException, PromotionState, PromotionToKingException, TokenValidator,
)


class PawnPromotionAnalyzer(Analyzer):
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
        
        -   _run_promotable_rank_tests(
                    rank: Rank,
                    rank_service: RankService
            ) -> ValidationResult[int]
        
        -    _run_enemy_rank_row_tests(
                    pawn_token: PawnToken,
                    schema_service: SchemaService
            ) -> ValidationResult[int]:
            
    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(
            cls,
            pawn: PawnToken,
            token_validator: TokenValidator | None = None,
            token_freedom_analyzer: TokenFreedomAnalyzer | None = None,
    ) -> AnalysisResult[PromotionApprovalReport]:
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
            PawnAlreadyPromotedException
            PawnPromotionRowException
            TypeError
        """
        method = f"{cls.__class__.__name__}.promote"
        
        # --- Supply any missing dependencies. ---#
        if token_freedom_analyzer is None:
            token_freedom_analyzer = TokenFreedomAnalyzer()
        if token_validator is None:
            token_validator = TokenValidator()
            
        analysis_result = token_freedom_analyzer.analyze(
            token=pawn,
            token_validator=token_validator
        )
        # Handle the case that, the freedom analysis is not completed.
        if analysis_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                PawnPromotionAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=PawnPromotionAnalyzerException.OP,
                    msg=PawnPromotionAnalyzerException.MSG,
                    err_code=PawnPromotionAnalyzerException.ERR_CODE,
                    mthd_rslt_type=PawnPromotionAnalyzerException.MTHD_RSLT,
                    ex=analysis_result.exception
                )
            )
        activity_report = cast(TokenFreedomReport, analysis_result.payload)
        
        # Handle the case that, the token is not free.
        if activity_report.token_is_not_free:
            return AnalysisResult.completed(
                PromotionApprovalReport.deny_promotion(
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
                PromotionApprovalReport.deny_promotion(
                    TypeError(
                        f"Expected type PawnToken for promotion. "
                        f"Got {type(pawn).__name__} instead."
                    )
                )
            )
        # Handle the case that, the pawn_token has already been promoted.
        if pawn.is_promoted:
            return AnalysisResult.completed(
                PromotionApprovalReport.deny_promotion(
                    PawnAlreadyPromotedException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=PawnAlreadyPromotedException.MSG,
                        err_code=PawnAlreadyPromotedException.ERR_CODE,
                    )
                )
            )
        if pawn.current_position.row != pawn.team.enemy_rank_row:
            return AnalysisResult.completed(
                PromotionApprovalReport.deny_promotion(
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
        return AnalysisResult.completed(PromotionApprovalReport.approve_promotion(pawn=pawn))


    @classmethod
    @LoggingLevelRouter.monitor
    def _run_promotable_rank_tests(
            cls,
            rank: Rank,
            pawn_token: PawnToken,
            rank_service: RankService,
    ) -> UpdateResult[PawnToken]:
        """
        Runs the exception that assures the rank instance can be used safely.
        
        Action:
            1.  Send an exception chain in the ValidationResult if:
                    *   The rank does not pass a validation check.
                    *   It's not a Pawn or King.
            2.  Otherwise, send the success result.
        Args:
            rank: Rank
            rank_service: RankService
        Returns:
            ValidationResult[int]
        Raises:
            PawnPromotionAnalyzerException
            PromoteToPawnException
            PromoteToKingException
        """
        method = f"{cls.__class__.__name__}. _run_promotable_rank_tests"
        
        # Handle the case that, the rank does not pass a validation check.
        validation_result = rank_service.validator.validate(rank)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PawnPromotionAnalyzerException(
                    cls_mthd=method,
                    op=PawnPromotionAnalyzerException.OP,
                    msg=PawnPromotionAnalyzerException.MSG,
                    err_code=PawnPromotionAnalyzerException.ERR_CODE,
                    mthd_rslt_type=PawnPromotionAnalyzerException.MTHD_RSLT,
                    ex=validation_result.exception
                )
            )
        # Handle the case that, the higher rank is a King's.
        if isinstance(rank, King):
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PawnPromotionAnalyzerException(
                    cls_mthd=method,
                    op=PawnPromotionAnalyzerException.OP,
                    msg=PawnPromotionAnalyzerException.MSG,
                    err_code=PawnPromotionAnalyzerException.ERR_CODE,
                    mthd_rslt_type=PawnPromotionAnalyzerException.MTHD_RSLT,
                    ex=PromotionToKingException(
                        msg=PromotionToKingException.MSG,
                        err_code=PromotionToKingException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the new is still a Pawn's.
        if isinstance(rank, Pawn):
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PawnPromotionAnalyzerException(
                    cls_mthd=method,
                    op=PawnPromotionAnalyzerException.OP,
                    msg=PawnPromotionAnalyzerException.MSG,
                    err_code=PawnPromotionAnalyzerException.ERR_CODE,
                    mthd_rslt_type=PawnPromotionAnalyzerException.MTHD_RSLT,
                    ex=PromoteToPawnException(
                        msg=PromoteToPawnException.MSG,
                        err_code=PromoteToPawnException.ERR_CODE,
                    )
                )
            )
        # --- Send the work product. ---#
        return UpdateResult.update_success(original=pawn_token, updated=pawn_token)
