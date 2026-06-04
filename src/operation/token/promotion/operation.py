# src/operation/token/promotion/operation.py

"""
Module: operation.token.promotion.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from copy import deepcopy
from typing import cast

from analyzer import PawnPromotionApprovalManager, PromotionLevelAnalyzer
from err import PawnPromoterException
from model import PawnToken, PromotionState, Rank
from report import PromotionApprovalManagerReport
from result import MethodResultType, UpdateResult
from util import LoggingLevelRouter


class PawnPromoter:
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
                    pawn: PawnToken,
                    rank_elevation_validator: RankService,
            ) -> UpdateResult[PawnToken]
            
    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            rank: Rank,
            pawn: PawnToken,
            promotion_level_analyzer: PromotionLevelAnalyzer | None = None,
            promotion_approval_manager: PawnPromotionApprovalManager | None = None,
    ) -> UpdateResult[PawnToken]:
        """
        Executes the promotion transaction.
        
        Action:
            1.  Send the unmodified pawn along with an exception chain in the UpdateResult if:
                    -   The promotion_approval_manager sends a denial report.
                    -   The promotion_level_analyzer approves the new rank.
            2.  Otherwise:
                    -   Make a deepcopy of pawn to pre_update_pawn.
                    -   Elevate the pawn to its new rank.
                    -   Update pawn.PromotionState
            3.  Send the success result containing, the finished work product.
        Args:
            rank: Rank
            pawn: PawnToken
            promotion_level_analyzer: RankElevationAnalyzer
            promotion_approval_manager: PawnPromotionApprovalManager 
        Returns:
            UpdateResult[PawnToken]
        Raises:
            PawnPromoterException
            PromoteInactivePawnException
            PawnAlreadyPromotedException
        """
        method = f"{cls.__class__.__name__}.promote"
        
        # --- Supply any missing dependencies. ---#
        if promotion_level_analyzer is None:
            promotion_level_analyzer = PromotionLevelAnalyzer()
        if promotion_approval_manager is None:
            promotion_approval_manager = PawnPromotionApprovalManager()
            
        pawn_approval_analysis_result = promotion_approval_manager.analyze(pawn)
        # Handle the case that, the promotion permission evaluation is not completed.
        if pawn_approval_analysis_result.is_failure:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=pawn_approval_analysis_result.exception
                )
            )
        pawn_approval = cast(PromotionApprovalManagerReport, pawn_approval_analysis_result.payload)
        # Handle the case that, the pawn is not granted promotion permission.
        if pawn_approval.is_denied:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=pawn_approval.exception
                )
            )
        # Handle the case that, a rank_promotable test fails.
        promotion_level_analysis_result = promotion_level_analyzer.validate(rank)
        if promotion_level_analysis_result.is_failure:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=promotion_level_analysis_result.exception
                )
            )
        #--- Approvals have been granted. Do the promotion work. ---#

        # Make a deepcopy of the original pawn.
        pre_update_pawn = deepcopy(pawn)
        # Set the new rank and update state.
        pawn.set_new_rank(rank)
        pawn.promotion_state = PromotionState.PROMOTED
        
        # --- Send the work product. ---#
        UpdateResult.update_success(original=pre_update_pawn, updated=pawn)