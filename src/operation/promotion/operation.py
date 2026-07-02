# src/operation/promotion/operation.py

"""
Module: operation.promotion.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from copy import deepcopy
from typing import cast

from err import PawnPromoterException
from model import PawnToken, PromotionState, Rank
from permitter import PromotionPermitter
from report import PromotionApproval
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
                    permitter: PromotionPermitter,
            ) -> UpdateResult[PawnToken]
            
    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            rank: Rank,
            pawn: PawnToken,
            permitter: PromotionPermitter | None = None,
    ) -> UpdateResult[PawnToken]:
        """
        Executes the promotion transaction.
        
        Action:
            1.  Send the unmodified pawn along with an exception chain in the UpdateResult if:
                    -   The promotion_approval_manager sends a denial report.
                    -   The promotion_rank_analyzer approves the new rank.
            2.  Otherwise:
                    -   Make a deepcopy of pawn to pre_update_pawn.
                    -   Elevate the pawn to its new rank.
                    -   Update pawn.PromotionState
            3.  Send the success result containing, the finished work product.
        Args:
            rank: Rank
            pawn: PawnToken
            permitter: PromotionPermitter
        Returns:
            UpdateResult[PawnToken]
        Raises:
            PawnPromoterException
        """
        method = f"{cls.__class__.__name__}.promote"
        
        # --- Supply any missing dependencies. ---#
        if permitter is None:
            permitter = PromotionPermitter()
            
        permission_analysis_result = permitter.execute(
            pawn=pawn,
            rank=rank,
        )
        # Handle the case that, the promotion permission evaluation is not completed.
        if permission_analysis_result.is_failure:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=permission_analysis_result.exception
                )
            )
        promotion_permission = cast(PromotionApproval, permission_analysis_result.payload)
        # Handle the case that, the pawn is not granted promotion permission.
        if promotion_permission.is_denied:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=promotion_permission.exception
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