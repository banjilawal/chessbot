# src/logic/token/service/operation/promotion/promoter.py

"""
Module: logic.token.service.operation.promotion.promoter
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations
from copy import deepcopy

from logic.schema import SchemaService
from logic.rank import King, Pawn, Rank, RankService
from logic.system import LoggingLevelRouter, UpdateResult
from logic.token import (
    PawnAlreadyPromotedException, PawnPromotionRowException, PawnToken, PromoteInactivePawnException,
    PromoteToPawnException, PromotionException, PromotionState, PromotionToKingException, TokenValidation
)


class PawnPromotionProcess:
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
                    token_validator: TokenValidation
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
    def execute(
            cls,
            rank: Rank,
            pawn_token: PawnToken,
            rank_service: RankService = RankService(),
            schema_service: SchemaService = SchemaService(),
            token_validator: TokenValidation = TokenValidation(),
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
            rank_service: RankService
            schema_service: SchemaService
            token_validator: TokenValidation
        Returns:
            UpdateResult[PawnToken]
        Raises:
            PromotionException
            PromoteInactivePawnException
            PawnAlreadyPromotedException
        """
        method = f"{cls.__class__.__name__}.promote"
        
        # Handle the case that, the token is not certified safe.
        token_validation_result = token_validator.verify_actionable_token(pawn_token)
        if token_validation_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PromotionException(
                    mthd=method,
                    title=cls.__name__,
                    op=PromotionException.OP,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    rslt_type=PromotionException.RSLT_TYPE,
                    ex=token_validation_result.exception
                )
            )
        # Handle the case that. the token is wrong type.
        if not isinstance(pawn_token, PawnToken):
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PromotionException(
                    mthd=method,
                    title=cls.__name__,
                    op=PromotionException.OP,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    rslt_type=PromotionException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected type PawnToken for promotion. "
                        f"Got {type(pawn_token).__name__} instead."
                    )
                )
            )
        # Handle the case that, the pawn_token is not actionable.
        if not pawn_token.is_active:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PromotionException(
                    mthd=method,
                    op=PromotionException.OP,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    rslt_type=PromotionException.RSLT_TYPE,
                    ex=PromoteInactivePawnException(
                        var=pawn_token.designation,
                        msg=PromoteInactivePawnException.MSG,
                        err_code=PromoteInactivePawnException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the pawn_token has already been promoted.
        if pawn_token.is_promoted:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PromotionException(
                    mthd=method,
                    op=PromotionException.OP,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    rslt_type=PromotionException.RSLT_TYPE,
                    ex=PawnAlreadyPromotedException(
                        var=pawn_token.designation,
                        msg=PawnAlreadyPromotedException.MSG,
                        err_code=PawnAlreadyPromotedException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, an enemy_rank_row test fails.
        enemy_rank_row_test_results = cls._run_enemy_rank_row_tests(
            pawn_token=pawn_token,
            schema_service=schema_service,
        )
        if enemy_rank_row_test_results.is_failure:
            return enemy_rank_row_test_results
        
        # Handle the case that, a rank_promotable test fails.
        promotable_rank_verification_result = cls._run_promotable_rank_tests(
            rank=rank,
            pawn=pawn_token,
            rank_service=rank_service,
        )
        if promotable_rank_verification_result.is_failure:
            return promotable_rank_verification_result
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
            PromotionException
            PromoteToPawnException
            PromoteToKingException
        """
        method = f"{cls.__class__.__name__}. _run_promotable_rank_tests"
        
        # Handle the case that, the rank does not pass a validation check.
        validation_result = rank_service.validation.execute(rank)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PromotionException(
                    mthd=method,
                    op=PromotionException.OP,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    rslt_type=PromotionException.RSLT_TYPE,
                    ex=validation_result.exception
                )
            )
        # Handle the case that, the higher rank is a King's.
        if isinstance(rank, King):
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PromotionException(
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
        # Handle the case that, the new is still a Pawn's.
        if isinstance(rank, Pawn):
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PromotionException(
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
        # --- Send the work product. ---#
        return UpdateResult.update_success(original=pawn_token, updated=pawn_token)

    @classmethod
    @LoggingLevelRouter.monitor
    def _run_enemy_rank_row_tests(
            cls,
            pawn_token: PawnToken,
            schema_service: SchemaService = SchemaService(),
    ) -> UpdateResult[PawnToken]:
        """
        Runs the exception that verifies the pawn_token is on its enemy's rank row.
        
        Action:
            1.  Send an exception chain in the ValidationResult if:
                    *   Searching the schema for the rank row is not completed.
                    *   The pawn is not on the enemy's rank_row.
            2.  Otherwise, send the success result.
        Args:
            pawn_token: Pawn
            schema_service: SchemaService
        Returns:
            ValidationResult[int]
        Raises:
            PromotionException
            PawnPromotionRowException
        """
        method = f"{cls.__class__.__name__}._run_enemy_rank_row_tests"
        
        # Search for the enemy's home row.
        enemy_schema_search_result = schema_service.enemy_schema(pawn_token.team.schema)
        
        # Handle the case that, the no work is produced.
        if enemy_schema_search_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PromotionException(
                    mthd=method,
                    op=PromotionException.OP,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    rslt_type=PromotionException.RSLT_TYPE,
                    ex=enemy_schema_search_result.exception
                )
            )
        # Handle the case that the pawn_token is not on the enemy's rank row.
        if pawn_token.current_position.row != enemy_schema_search_result.payload[0].rank_row:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pawn_token,
                exception=PromotionException(
                    mthd=method,
                    op=PromotionException.OP,
                    msg=PromotionException.MSG,
                    err_code=PromotionException.ERR_CODE,
                    rslt_type=PromotionException.RSLT_TYPE,
                    ex=PawnPromotionRowException(
                        var=pawn_token.designation,
                        msg=PromotionException.MSG,
                        err_code=PromotionException.ERR_CODE,
                    )
                )
            )
        # --- Send the work product. ---#
        return UpdateResult.update_success(original=pawn_token, updated=pawn_token)
