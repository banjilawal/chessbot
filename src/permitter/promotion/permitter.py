# src/permitter/promotion/permitter.py

"""
Module: permitter.promotion.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

# =========== PERMITTER.PUSH PACKAGE ===========#

from __future__ import annotations
from typing import cast

from analyzer import TokenReadinessAnalyzer
from err import (
    PawnDoublePromotionException, PawnPromotionRowException, PromoteInactivePawnException,
    PromoteToKingException, PromoteToPawnException, PromotionPermitterException
)
from model import King, Pawn, PawnToken, Rank
from permitter import OperationPermitter
from report import PromotionApproval, TokenReadinessReport
from result import AnalysisResult, MethodResultType
from util import LoggingLevelRouter
from validator import RankValidator, TokenValidator


class PromotionPermitter(OperationPermitter):
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
    def analyze(
            cls,
            rank: Rank,
            pawn: PawnToken,
            rank_validator: RankValidator | None = None,
            token_validator: TokenValidator | None = None,
            token_freedom_analyzer: TokenReadinessAnalyzer | None = None,
    ) -> AnalysisResult[PromotionApproval]:
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
            rank: Rank
            pawn: PawnToken
            rank_validator: RankValidator
            token_validator: TokenValidator
            token_freedom_analyzer: TokenFreedomAnalyzer
        Returns:
            AnalysisResult[PromotionReport]
        Raises:
            PromotionPermitterException
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
        if rank_validator is None:
            rank_validator = RankValidator()
        
        # Handle the case that, the candidate is flagged by the rank_validator.
        rank_validation_result = rank_validator.execute(rank)
        if rank_validation_result.is_failure:
            return AnalysisResult.failure(
                PromotionPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PromotionPermitterException.MSG,
                    err_code=PromotionPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=rank_validation_result.exception
                )
            )
        freedom_analysis_result = token_freedom_analyzer.analyze(
            token=pawn,
            token_validator=token_validator
        )
        # Handle the case that, the freedom analysis is not completed.
        if freedom_analysis_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                PromotionPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PromotionPermitterException.MSG,
                    err_code=PromotionPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=freedom_analysis_result.exception
                )
            )
        report = cast(TokenReadinessReport, freedom_analysis_result.payload)
        
        # Handle the case that, the token is not free.
        if report.token_is_not_ready:
            # Send the exception chain on failure.
            return AnalysisResult.completed(
                PromotionApproval.deny(
                    PromotionPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=PromotionPermitterException.MSG,
                        err_code=PromotionPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=PromoteInactivePawnException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=PromoteInactivePawnException.MSG,
                            err_code=PromoteInactivePawnException.ERR_CODE,
                        )
                    )
                )
            )
        # Handle the case that, the token is not a PawnToken.
        if not isinstance(pawn, PawnToken):
            # Send the exception chain on failure.
            return AnalysisResult.completed(
                PromotionApproval.deny(
                    PromotionPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=PromotionPermitterException.MSG,
                        err_code=PromotionPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=TypeError(
                            f"Expected type PawnToken for promotion. "
                            f"Got {type(pawn).__name__} instead."
                        )
                    )
                )
            )
        # Handle the case that, the pawn_token has already been promoted.
        if pawn.is_promoted:
            # Send the exception chain on failure.
            return AnalysisResult.completed(
                PromotionApproval.deny(
                    PromotionPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=PromotionPermitterException.MSG,
                        err_code=PromotionPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=PawnDoublePromotionException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=PawnDoublePromotionException.MSG,
                            err_code=PawnDoublePromotionException.ERR_CODE,
                        )
                    )
                )
            )
        # Handle the case that, the is not on its promotion row..
        if pawn.current_position.row != pawn.team.enemy_rank_row:
            return AnalysisResult.completed(
                PromotionApproval.deny(
                    PromotionPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=PromotionPermitterException.MSG,
                        err_code=PromotionPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=PawnPromotionRowException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            var=pawn.designation,
                            msg=PawnPromotionRowException.MSG,
                            err_code=PawnPromotionRowException.ERR_CODE,
                        )
                    )
                )
            )

        # Handle the case that, the higher rank is a King's.
        if isinstance(rank, King):
            # Send the exception chain on failure.
            return AnalysisResult.completed(
                PromotionApproval.deny(
                    PromotionPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=PromotionPermitterException.MSG,
                        err_code=PromotionPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=PromoteToKingException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=PromoteToKingException.MSG,
                            err_code=PromoteToKingException.ERR_CODE,
                        ),
                    )
                )
            )
        # Handle the case that, the new rank is still a Pawn's.
        if isinstance(rank, Pawn):
            # Send the exception chain on failure.
            return AnalysisResult.completed(
                PromotionApproval.deny(
                    PromotionPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=PromotionPermitterException.MSG,
                        err_code=PromotionPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=PromoteToPawnException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=PromoteToPawnException.MSG,
                            err_code=PromoteToPawnException.ERR_CODE,
                        ),
                    )
                )
            )
        # --- Send the work product. ---#
        return AnalysisResult.completed(
            PromotionApproval.approve(pawn=pawn, rank=rank)
        )
