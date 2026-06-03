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

from analyzer import PawnPromotionAnalyzer
from err import PawnPromoterException
from model import PawnToken, PromotionState, Rank
from report import PromotionApprovalReport
from result import MethodResultType, UpdateResult
from util import LoggingLevelRouter
from validation import RankElevationValidator


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
                    schema_service: SchemaService,
                    token_validator: TokenValidator
            ) -> UpdateResult[PawnToken]
            
    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            rank: Rank,
            pawn: PawnToken,
            rank_elevation_validator: RankElevationValidator | None = None,
            promotion_analyzer: PawnPromotionAnalyzer | None = None,
    ) -> UpdateResult[PawnToken]:
        """
        Executes the promotion transaction.
        
        Action:
            1.  Send the unmodified pawn along with an exception chain in the UpdateResult if:
                    *   The token is not certified as a safe, actionable PawnToken.
                    *   The pawn is already promoted.
                    *   Is not on its enemy's rank_row.
                    *   The new rank is either King or Pawn.
            2.  Otherwise:
                    *   Make a deepcopy of the pawn to pre_update_pawn.
                    *   Set the new rank
                    *   Set the pawn's promotion_state to PromotionState.PROMOTED.
            3.  Send the success result containing, the finished work product.
        Args:
            rank: Rank
            pawn: PawnToken
            rank_elevation_validator: RankElevationValidator
            promotion_analyzer: PawnPromotionAnalyzer
        Returns:
            UpdateResult[PawnToken]
        Raises:
            PawnPromoterException
            PromoteInactivePawnException
            PawnAlreadyPromotedException
        """
        method = f"{cls.__class__.__name__}.promote"
        
        # --- Supply any missing dependencies. ---#
        if rank_elevation_validator is None:
            rank_elevation_validator = RankElevationValidator()
        if promotion_analyzer is None:
            promotion_analyzer = PawnPromotionAnalyzer()
            
        analysis_result = promotion_analyzer.analyze(pawn)
        # Handle the case that, the promotion permission evaluation is not completed.
        if analysis_result.is_failure:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=analysis_result.exception
                )
            )
        permission = cast(PromotionApprovalReport, analysis_result.payload)
        # Handle the case that, the pawn is not granted promotion permission.
        if permission.is_denied:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=permission.exception
                )
            )
        # Handle the case that, a rank_promotable test fails.
        elevation_check_result = rank_elevation_validator.validate(rank)
        if elevation_check_result.is_failure:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=elevation_check_result.exception
                )
            )
        #--- Integrity and consistency checks are passed. Do the promotion work. ---#

        # Make a deepcopy of the original pawn.
        pre_update_pawn = deepcopy(pawn)
        # Set the new rank and update state.
        pawn.set_new_rank(rank)
        pawn.promotion_state = PromotionState.PROMOTED
        
        # --- Send the work product. ---#
        UpdateResult.update_success(original=pre_update_pawn, updated=pawn)