# src/logic/token/service/handler/promotion/handler.py

"""
Module: logic.token.service.handler.promotion.handler
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from logic.rank import King, Knight, Queen, Rank, RankService, Rook
from logic.rank.model.concrete.bishop import Bishop
from logic.square import SquareContext
from logic.system import DeletionResult, IntegrityService, InsertionResult, LoggingLevelRouter, id_emitter
from logic.coord import Coord, CoordService, DuplicateCoordPushException, PoppingEmtpyCoordStackException
from logic.token import (
    CannotPromotePawnToKingException, NewRankSameAsCurrentRankException, OverMoveUndoLimitException,
    PawnAlreadyPromotedException,
    PawnPromotionException, PawnToken,
    PromotionState, Token, TokenBoardState,
    TokenValidator,
    TokenDeploymentException, TokenFactory, TokenReadinessAnalyzer, TokenOpeningSquareNotFoundException,
    TokenServiceException,
)
from logic.token.service.detector import TokenCollisionDetector


class PawnPromotionHandler:
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer, Computation, Transformer,.

    # LOCAL RESPONSIBILITIES:

    # INHERITED RESPONSIBILITIES:
    None

    # PARENT:
    None

    # PROVIDES:
    None

    Attributes:
        SERVICE_NAME: str
        collision_detector: TokenCollisionDetector
        readiness_analyzer: TokenReadinessAnalyzer

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
        *   id (int)
        *   name (str)
        *   builder (TokenBuilder) = TokenBuilder()
        *   validator (TokenValidator) = TokenValidator()
        *   collision_detector: TokenCollisionDetector = TokenCollisionDetector(),
        *   readiness_analyzer: TokenReadinessAnalyzer = TokenReadinessAnalyzer(),

    Methods:
        push_coord_to_token(token: Token, position: Coord, coord_service: CoordService) -> InsertionResult:

        *   promote_pawn(
                    self,
                    pawn: PawnToken,
                    new_rank: Rank,
                    rank_service: RankService = RankService()
            ) -> UpdateResult[PawnToken]:

        *   deploy_on_board(self,token: Token) -> InsertionResult[bool]:
        *   pop_coord_from_token(self, token) -> DeletionResult[Coord]:

    # INHERITED METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def promote(
            cls,
            pawn: PawnToken,
            new_rank: Rank,
            rank_service: RankService = RankService(),
            token_validator: TokenValidator = TokenValidator(),
    ) -> InsertionResult:
        """
        Action:
            1.  If the token is not a free pawn or it has been promoted send an exception chain to the
                InsertionResult.
            2.  If the rank fails validation send an exception chain to the InsertionResult.
            3.  Update the pawn's rank and promotion state then send the success InsertionResult.

        Args:
            pawn: PawnToken
            new_rank: Rank
            rank_service: RankService
            token_validator: TokenValidator

        Returns:
            UpdateResult

        Raises:
            TokenServiceException
            CoordAlreadyToppingStackException
        """
        method = f"{cls.__class__.__name__}.promote"
        
        # Handle the case that, the token is not certified safe.
        pawn_validation = token_validator.verify_actionable_token(pawn)
        if pawn_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    msg=f"{method}: {TokenService.ERR_CODE}",
                    ex=pawn_validation.exception
                )
            )
        # Handle the case that, the token is not a pawn
        if not isinstance(pawn, PawnToken):
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {TokenService.ERR_CODE}",
                    ex=PawnPromotionException(
                        msg=f"{method}: {PawnPromotionException.ERR_CODE}",
                        ex=TypeError(
                            f"{method}: Expected type PawnToken for promotion. Got {type(pawn).__name__} instead."
                        )
                    )
                )
            )
        # Handle the case that, the pawn has already been promoted.
        if pawn.is_promoted:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {TokenService.ERR_CODE}",
                    ex=PawnPromotionException(
                        msg=f"{method}: {PawnPromotionException.ERR_CODE}",
                        ex=PawnAlreadyPromotedException(f"{method}: {PawnAlreadyPromotedException.MSG}")
                    )
                )
            )
        # Handle the case that, the rank is not certified as safe.
        rank_validation = rank_service.validate(new_rank)
        if rank_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {TokenService.ERR_CODE}",
                    ex=PawnPromotionException(
                        msg=f"{method}: {PawnPromotionException.ERR_CODE}",
                        ex=rank_validation.exception
                    )
                )
            )
        # Handle the case that, the new rank is King.
        if isinstance(new_rank, King):
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {TokenService.ERR_CODE}",
                    ex=PawnPromotionException(
                        msg=f"{method}: {PawnPromotionException.ERR_CODE}",
                        ex=CannotPromotePawnToKingException(
                            f"{method}: {CannotPromotePawnToKingException.MSG}"
                        )
                    )
                )
            )
        # Handle the case that, new_rank is still a Pawn rank.
        if pawn.rank == new_rank:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {TokenService.ERR_CODE}",
                    ex=PawnPromotionException(
                        msg=f"{method}: {PawnPromotionException.ERR_CODE}",
                        ex=NewRankSameAsCurrentRankException(NewRankSameAsCurrentRankException.MSG)
                    )
                )
            )
        # --- Conduct promotion steps. ---#
        pawn.set_new_rank(new_rank)
        
        # Match the promotion state to the rank
        if isinstance(new_rank, Bishop):
            pawn.promotion_state = PromotionState.PROMOTED_TO_BISHOP
        if isinstance(new_rank, Knight):
            pawn.promotion_state = PromotionState.PROMOTED_TO_KNIGHT
        if isinstance(new_rank, Rook):
            pawn.promotion_state = PromotionState.PROMOTED_TO_ROOK
        if isinstance(new_rank, Queen):
            pawn.promotion_state = PromotionState.PROMOTED_TO_QUEEN
        
        # Send the success result to the caller.
        return InsertionResult.success()