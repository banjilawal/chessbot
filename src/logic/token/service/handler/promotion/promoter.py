# src/logic/token/service/handler/promotion/handler.py

"""
Module: logic.token.service.handler.promotion.handler
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations
from copy import deepcopy

from logic.schema import SchemaService
from logic.rank import King, Pawn, Rank, RankService
from logic.system import LoggingLevelRouter, UpdateResult, ValidationResult
from logic.token import (
    PawnPromotionRowException, PromoteInactivePawnException, PromoteToPawnException, PromotionState,
    PromotionToKingException, PawnAlreadyPromotedException, PawnPromoterException, PromotionException,
    PawnToken, TokenValidator,
)


class PawnPromoter:
    """
    # ROLE: Update Handler, Consistency, Integrity Maintenance, Lifecycle Management

    # RESPONSIBILITIES:
    1.  Ensure integrity and consistency are maintained during the pawn's promotion lifecycle.

    # PARENT:
    None

    # PROVIDES:
    None

    Attributes:
    None

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
    None
    
    # LOCAL METHODS:

    # INHERITED METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def promote(
            cls,
            rank: Rank,
            pawn: PawnToken,
            rank_service: RankService = RankService(),
            schema_service: SchemaService = SchemaService(),
            token_validator: TokenValidator = TokenValidator(),
    ) -> UpdateResult[PawnToken]:
        """
        Action:
            1.  If the token is not a free pawn or it has been promoted send an exception chain to the
                InsertionResult.
            2.  If the rank fails validation send an exception chain to the InsertionResult.
            3.  Update the pawn's rank and promotion state then send the success InsertionResult.

        Args:
            rank: Rank
            pawn: PawnToken
            rank_service: RankService
            schema_service: SchemaService
            token_validator: TokenValidator

        Returns:
            UpdateResult[PawnToken]

        Raises:
            TokenServiceException
            CoordAlreadyToppingStackException
        """
        method = f"{cls.__class__.__name__}.promote"
        
        # Handle the case that, the token is not certified safe.
        token_validation_result = token_validator.verify_actionable_token(pawn)
        if token_validation_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    ex=PromotionException(
                        mthd=method,
                        op=PromotionException.OP,
                        msg=PromotionException.MSG,
                        err_code=PromotionException.ERR_CODE,
                        rslt_type=PromotionException.RSLT_TYPE,
                        ex=token_validation_result.exception
                    )
                )
            )
        # Handle the case that. the token is wrong type.
        if not isinstance(pawn, PawnToken):
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    ex=PromotionException(
                        mthd=method,
                        op=PromotionException.OP,
                        msg=PromotionException.MSG,
                        err_code=PromotionException.ERR_CODE,
                        rslt_type=PromotionException.RSLT_TYPE,
                        ex=TypeError(
                            f"Expected type PawnToken for promotion. Got {type(pawn).__name__} instead."
                        )
                    )
                )
            )
        # Handle the case that, the pawn is not actionable.
        if not pawn.is_active:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    ex=PromotionException(
                        mthd=method,
                        op=PromotionException.OP,
                        msg=PromotionException.MSG,
                        err_code=PromotionException.ERR_CODE,
                        rslt_type=PromotionException.RSLT_TYPE,
                        ex=PromoteInactivePawnException(
                            var=pawn.designation,
                            msg=PromoteInactivePawnException.MSG,
                            err_code=PromoteInactivePawnException.ERR_CODE,
                        )
                    )
                )
            )

        # Handle the case that, the pawn has already been promoted.
        if pawn.is_promoted:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    ex=PromotionException(
                        mthd=method,
                        op=PromotionException.OP,
                        msg=PromotionException.MSG,
                        err_code=PromotionException.ERR_CODE,
                        rslt_type=PromotionException.RSLT_TYPE,
                        ex=PawnAlreadyPromotedException(
                            var=pawn.designation,
                            msg=PawnAlreadyPromotedException.MSG,
                            err_code=PawnAlreadyPromotedException.ERR_CODE,
                        )
                    )
                )
            )
        # Handle the case that, the pawn is not on its enemy's ran row.
        on_enemy_rank_row_verification_result = cls._verify_on_enemy_rank_row(
            pawn=pawn,
            schema_service=schema_service,
        )
        if on_enemy_rank_row_verification_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn,
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    ex=PromotionException(
                        mthd=method,
                        op=PromotionException.OP,
                        msg=PromotionException.MSG,
                        err_code=PromotionException.ERR_CODE,
                        rslt_type=PromotionException.RSLT_TYPE,
                        ex=on_enemy_rank_row_verification_result.exception
                    )
                )
            )
        # --- Integrity and consistency checks are passed. Start the promotion. ---#

        # Make a deepcopy of the original pawn.
        pre_update_pawn = deepcopy(pawn)
        
        # Set the new rank and update state.
        pawn.set_new_rank(rank)
        pawn.promotion_state = PromotionState.PROMOTED
        
        # --- Send the success product ---#
        UpdateResult.update_success(
            original=pre_update_pawn,
            updated=pawn,
        )

    @classmethod
    @LoggingLevelRouter.monitor
    def _verify_rank_is_promotable(
            cls,
            rank,
            rank_service: RankService,
    ) -> ValidationResult[int]:
        """
        Action:
            Verify the rank is safe, and not a Pawn or King
        Args:
            rank: Rank
            rank_service: RankService
        Returns:
            ValidationResult[int]
        Raises:
            PromotionException
            PawnPromoterException
            PromoteToPawnException
            PromoteToKingException
        """
        method = f"{cls.__class__.__name__}. _verify_rank_is_promotable"
        
        # Handle the case that, the rank is not certified as safe.
        validation_result = rank_service.validator.validate(rank)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    ex=PromotionException(
                        mthd=method,
                        op=PromotionException.OP,
                        msg=PromotionException.MSG,
                        err_code=PromotionException.ERR_CODE,
                        rslt_type=PromotionException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
            )
        # Handle the case that, the higher rank is a King's.
        if isinstance(rank, King):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    ex=PromotionException(
                        mthd=method,
                        op=PromotionException.OP,
                        msg=PromotionException.MSG,
                        err_code=PromotionException.ERR_CODE,
                        rslt_type=PromotionException.RSLT_TYPE,
                        ex=PromotionToKingException(
                            msg=PromotionToKingException.MSG,
                            err_code=PromotionToKingException.ERR_CODE,
                        )
                    )
                )
            )
        # Handle the case that, the new is still Pawn rank.
        if isinstance(rank, Pawn):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    ex=PromotionException(
                        mthd=method,
                        op=PromotionException.OP,
                        msg=PromotionException.MSG,
                        err_code=PromotionException.ERR_CODE,
                        rslt_type=PromotionException.RSLT_TYPE,
                        ex=PromoteToPawnException(
                            msg=PromoteToPawnException.MSG,
                            err_code=PromoteToPawnException.ERR_CODE,
                        )
                    )
                )
            )
        return ValidationResult.success(1)

    @classmethod
    @LoggingLevelRouter.monitor
    def _verify_on_enemy_rank_row(
            cls,
            pawn: PawnToken,
            schema_service: SchemaService,
    ) -> ValidationResult[int]:
        """
        Action:
            Verify the token is on its enemy's rank row.
        Args:
            pawn: Pawn
        Returns:
            ValidationResult[int]
        Raises:
            PromotionException
            PawnPromoterException
            PawnPromotionRowException
        """
        method = f"{cls.__class__.__name__}._verify_pawn_on_enemy_rank_row"
        
        # Search for the enemy's home row.
        enemy_schema_search_result = schema_service.enemy_schema(pawn.team.schema)
        
        # Handle the case that, the no work is produced.
        if enemy_schema_search_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    ex=PromotionException(
                        mthd=method,
                        op=PromotionException.OP,
                        msg=PromotionException.MSG,
                        err_code=PromotionException.ERR_CODE,
                        rslt_type=PromotionException.RSLT_TYPE,
                        ex=enemy_schema_search_result.exception
                    )
                )
            )
        # Handle the case that the pawn is not on the enemy's rank row.
        if pawn.current_position.row != enemy_schema_search_result.payload[0].rank_row:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                exception=PawnPromoterException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    ex=PromotionException(
                        mthd=method,
                        op=PromotionException.OP,
                        msg=PromotionException.MSG,
                        err_code=PromotionException.ERR_CODE,
                        rslt_type=PromotionException.RSLT_TYPE,
                        ex=PawnPromotionRowException(
                            var=pawn.designation,
                            msg=PromotionException.MSG,
                            err_code=PromotionException.ERR_CODE,
                        )
                    )
                )
            )
        return ValidationResult.success(1)