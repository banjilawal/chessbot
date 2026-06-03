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
from model import Pawn, PawnToken, PromotionState, Rank
from report import PromotionPermission
from result import MethodResultType, UpdateResult
from util import LoggingLevelRouter
from validation import RankValidator


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
                    pawn_token: PawnToken,
                    rank_validator: RankService,
                    schema_service: SchemaService,
                    token_validator: TokenValidator
            ) -> UpdateResult[PawnToken]
        
        -   _run_promotable_rank_tests(
                    rank: Rank,
                    rank_validator: RankService
            ) -> ValidationResult[int]
        
        -    _run_enemy_rank_row_tests(
                    pawn_token: PawnToken,
                    schema_service: SchemaService
            ) -> ValidationResult[int]:
            
    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            rank: Rank,
            pawn_token: PawnToken,
            rank_validator: RankValidator | None = None,
            promotion_analyzer: PawnPromotionAnalyzer | None = None,
    ) -> UpdateResult[PawnToken]:
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
            pawn_token: PawnToken
            rank_validator: RankValidator
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
        if rank_validator is None:
            rank_validator = RankValidator()
        if promotion_analyzer is None:
            promotion_analyzer = PawnPromotionAnalyzer()
            
        analysis_result = promotion_analyzer.analyze(pawn_token)
        # Handle the case that, the promotion permission evaluation is not completed.
        if analysis_result.is_failure:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    cls_name=cls.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=analysis_result.exception
                )
            )
        permission = cast(PromotionPermission, analysis_result.payload)
        # Handle the case that, the pawn is not granted promotion permission.
        if permission.is_denied:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    cls_name=cls.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=permission.exception
                )
            )
        # Handle the case that, a rank_promotable test fails.
        elevation_test_result = cls._run_rank_elevation_tests(
            rank=rank,
            pawn=pawn_token,
            rank_validator=rank_validator,
        )
        if elevation_test_result.is_failure:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    cls_name=cls.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=elevation_test_result.exception
                )
            )
        #--- Integrity and consistency checks are passed. Do the promotion work. ---#

        # Make a deepcopy of the original pawn_token.
        pre_update_pawn_token = deepcopy(pawn_token)
        # Set the new rank and update state.
        pawn_token.set_new_rank(rank)
        pawn_token.promotion_state = PromotionState.PROMOTED
        
        # --- Send the work product. ---#
        UpdateResult.update_success(original=pre_update_pawn_token, updated=pawn_token)

    @classmethod
    @LoggingLevelRouter.monitor
    def _run_rank_elevation_tests(
            cls,
            rank: Rank,
            pawn_token: PawnToken,
            rank_validator: RankValidator,
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
            rank_validator: RankService
        Returns:
            ValidationResult[int]
        Raises:
            PawnPromoterException
            PromoteToPawnException
            PromoteToKingException
        """
        method = f"{cls.__class__.__name__}. _run_promotable_rank_tests"
        
        # Handle the case that, the rank does not pass a validation check.
        validation_result = rank_validator.validate(rank)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=validation_result.exception
                )
            )
        # Handle the case that, the higher rank is a King's.
        if isinstance(rank, King):
            # Send the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
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
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PawnPromoterException.MSG,
                    err_code=PawnPromoterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.UPDATE_RESULT,
                    ex=PromoteToPawnException(
                        msg=PromoteToPawnException.MSG,
                        err_code=PromoteToPawnException.ERR_CODE,
                    )
                )
            )
        # --- Send the work product. ---#
        return UpdateResult.update_success(original=pawn_token, updated=pawn_token)