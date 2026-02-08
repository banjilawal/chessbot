# src/chess/token/service/service.py

"""
Module: chess.token.service.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from chess.rank import King, Knight, Queen, Rank, RankService, Rook
from chess.rank.model.concrete.bishop import Bishop
from chess.square import SquareContext
from chess.system import DeletionResult, EntityService, InsertionResult, LoggingLevelRouter, id_emitter
from chess.coord import Coord, CoordService, DuplicateCoordPushException, PoppingEmtpyCoordStackException
from chess.token import (
    OverMoveUndoLimitException, PawnToken, PromotionState, Token, TokenAlreadyDeployedOnBoardException, TokenBoardState,
    TokenValidator,
    TokenDeploymentFailedException, TokenFactory, TokenReadinessAnalyzer, TokenOpeningSquareNotFoundException,
    TokenServiceException,
)


class TokenService(EntityService[Token]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Token microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Token state by providing single entry and exit points to Token
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   formation_service (FormationService)

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    SERVICE_NAME = "TokenService"
    _readiness_analyzer: TokenReadinessAnalyzer
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: TokenFactory = TokenFactory(),
            validator: TokenValidator = TokenValidator(),
            readiness_analyzer: TokenReadinessAnalyzer = TokenReadinessAnalyzer(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (TokenFactory)
            *   validator (TokenValidator)

        # RETURNS:
        None

        # RAISES:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._readiness_analyzer = readiness_analyzer
    
    @property
    def builder(self) -> TokenFactory:
        """get TokenFactory"""
        return cast(TokenFactory, self.entity_builder)
    
    @property
    def validator(self) -> TokenValidator:
        """get TokenValidator"""
        return cast(TokenValidator, self.entity_validator)
    
    @property
    def readiness_analyzer(self) -> TokenReadinessAnalyzer:
        return self._readiness_analyzer
        
    @LoggingLevelRouter.monitor
    def pop_coord_from_token(self, token) -> DeletionResult[Coord]:
        """
        # ACTION:
            1.  If the token fails validation returns the exception in the DeletionResult.
            2.  If the token has not been activated with an opening item return the exception in the DeletionResult.
            3.  If the token has an empty coord stack return the exception in the DeletionResult.
            4.  If a new coord has not been pushed since the last undo send and exception in the DeletionResult.
                Else, forward the results of token.positions.pop_coord() to the caller.
        # PARAMETERS:
            *   token (Token)
        # RETURN:
            *   DeletionResult[Coord] containing either:
                    - On failure: Exception
                    - On success: Coord in the payload.
        # RAISES:
            *   TokenServiceException
            *   OverMoveUndoLimitException
            *   TokenOpeningSquareNotFoundException
            *   PoppingEmtpyCoordStackException
        """
        method = "TokenService.pop_coord_from_token"
        
        validation = self.validator.validate(token)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenServiceException.ERROR_CODE}",
                    ex=validation.exception
                )
            )
        # Handle the case that the opening item is null which implies there are no moves to undo.
        if token.opening_square_name is None:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenServiceException.ERROR_CODE}",
                    ex=TokenOpeningSquareNotFoundException(
                        f"{method}: {TokenOpeningSquareNotFoundException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the token has no positions that can be removed.
        if token.positions.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenServiceException.ERROR_CODE}",
                    ex=PoppingEmtpyCoordStackException(
                        f"{method}: {PoppingEmtpyCoordStackException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that an attempt is made to undo more than one turn.
        if token.previous_coord == token.current_address:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenServiceException.ERROR_CODE}",
                    ex=OverMoveUndoLimitException(f"{method}: {OverMoveUndoLimitException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the coord stack pop operation fails.
        pop_result = token.positions.pop()
        if token.previous_coord == token.current_address:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenServiceException.ERROR_CODE}",
                    ex=pop_result.exception
                )
            )
        # Otherwise return the successful pop operation's data to the caller in the DeletionResult.
        return pop_result
    
    @LoggingLevelRouter.monitor
    def push_coord_to_token(
            self,
            token: Token,
            position: Coord,
            coord_service: CoordService = CoordService()
    ) -> InsertionResult:
        """
        # ACTION:
            1.  If the token or coord fail their validations return the exception in the InsertionResult.
            2.  If the position is already the current position return the exception in the InsertionResult.
            3.  If the pushing the position to the token's coord stack fails encapsulate the exception then
                send the exception chain in the InsertionResult.'
        # PARAMETERS:
            *   token (Token)
            *   coord (Coord)
            *   coord_service (CoordService)
        # RETURN:
            *   InsertionResult[Coord] containing either:
                    - On failure: Exception
                    - On success: Coord in the payload.
        # RAISES:
            *   TokenServiceException
            *   CoordAlreadyToppingStackException
        """
        method = "TokenService.push_coord_to_token"
        
        # Handle the case that the token is not certified safe.
        token_validation = self.validator.validate(token)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenService.ERROR_CODE}",
                    ex=token_validation.exception
                )
            )
        # Handle the case that the position is not certified safe.
        position_validation = coord_service.validate(position)
        if position_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenService.ERROR_CODE}",
                    ex=token_validation.exception
                )
            )
        # Handle the case that the token is already the current position
        if position == token.current_position:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenServiceException.ERROR_CODE}",
                    ex=DuplicateCoordPushException(
                        f"{method}: {DuplicateCoordPushException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that adding the coord to the token's position history fails.
        insertion_result = token.positions.push(item=position)
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenServiceException.ERROR_CODE}",
                    ex=insertion_result.exception
                )
            )
        # If the coord was successfully pushed onto the token's coord stack forward insertion result.
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def promote_pawn(
            self,
            pawn: PawnToken,
            new_rank: Rank,
            rank_service: RankService = RankService()
    ) -> InsertionResult:
        """
        # ACTION:
            1.  If the token is not a free pawn or it has been promoted send an exception chain to the
                InsertionResult.
            2.  If the rank fails validation send an exception chain to the InsertionResult.
            3.  Update the pawn's rank and promotion state then send the success InsertionResult.
        # PARAMETERS:
            *   pawn (PawnToken)
            *   new_rank (Rank)
            *   rank_service (RankService)
        # RETURN:
            *   InsertionResult[bool] containing either:
                    - On failure: Exception
                    - On success: True.
        # RAISES:
            *   TokenServiceException
            *   CoordAlreadyToppingStackException
        """
        method = "TokenService.promote_pawn"
        
        # Handle the case that the token is not certified safe.
        pawn_validation = self.validator.verify_actionable_token(pawn)
        if pawn_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenService.ERROR_CODE}",
                    ex=pawn_validation.exception
                )
            )
        # Handle the case that the token is not a pawn
        if not isinstance(pawn, PawnToken):
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenService.ERROR_CODE}",
                    ex=PawnPromotionFailedException(
                        message=f"{method}: {PawnPromotionFailedException.ERROR_CODE}",
                        ex=f"{method}: Expected type PawnToken for promotion. Got {type(pawn).__name__} instead."
                    )
                )
            )
        # Handle the case that the pawn has already been promoted.
        if pawn.is_promoted:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenService.ERROR_CODE}",
                    ex=PawnPromotionFailedException(
                        message=f"{method}: {PawnPromotionFailedException.ERROR_CODE}",
                        ex=PawnAlreadyPromotedException(f"{method}: {PawnAlreadyPromotedException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # Handle the case that the rank is not certified as safe.
        rank_validation = rank_service.validate(new_rank)
        if rank_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenService.ERROR_CODE}",
                    ex=PawnPromotionFailedException(
                        message=f"{method}: {PawnPromotionFailedException.ERROR_CODE}",
                        ex=rank_validation.exception
                    )
                )
            )
        # Handle the case that the new rank is King.
        if isinstance(new_rank, King):
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenService.ERROR_CODE}",
                    ex=PawnPromotionFailedException(
                        message=f"{method}: {PawnPromotionFailedException.ERROR_CODE}",
                        ex=CannotPromotePawnToKingException(
                            f"{method}: {CannotPromotePawnToKingException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that new_rank is still a Pawn rank.
        if pawn.rank == new_rank:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenService.ERROR_CODE}",
                    ex=PawnPromotionFailedException(
                        message=f"{method}: {PawnPromotionFailedException.ERROR_CODE}",
                        ex=NewRankSameAsCurrentRankException(NewRankSameAsCurrentRankException.DEFAULT_MESSAGE)
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
        
        
    
    @LoggingLevelRouter.monitor
    def deploy_on_board(self,token: Token,) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the token or coord fail their validations return the exception in the InsertionResult.
            2.  If the position is already the current position return the exception in the InsertionResult.
            3.  If the pushing the position to the token's coord stack fails encapsulate the exception then
                send the exception chain in the InsertionResult.'
        # PARAMETERS:
            *   token (Token)
        # RETURN:
            *   InsertionResult[bool] containing either:
                    - On failure: Exception
                    - On success: True.
        # RAISES:
            *   TokenServiceException
            *   CoordAlreadyToppingStackException
        """
        method = "TokenService.deploy_on_board"
        
        # Handle the case that the token is not certified safe.
        token_validation = self.validator.validate(token)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenService.ERROR_CODE}",
                    ex=TokenDeploymentFailedException(
                        message=f"{method}: {TokenDeploymentFailedException.ERROR_CODE}",
                        ex=token_validation.exception
                    )
                )
            )
        # Handle the case that the token has already been placed on the board.
        if token.board_state != TokenBoardState.NEVER_BEEN_PLACED:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenService.ERROR_CODE}",
                    ex=TokenDeploymentFailedException(
                        message=f"{method}: {TokenDeploymentFailedException.ERROR_CODE}",
                        ex=TokenAlreadyDeployedOnBoardException(f"{method}:")
                    )
                )
            )
        # Find the square where the token gets formed.
        square_search_result = token.team.board.squares.search(
            context=SquareContext(token.opening_square_name)
        )
        # Handle the case that the search is not completed.
        if square_search_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenService.ERROR_CODE}",
                    ex=TokenDeploymentFailedException(
                        message=f"{method}: {TokenDeploymentFailedException.ERROR_CODE}",
                        ex=square_search_result.exception
                    )
                )
            )
        # Handle the case the square is not found.
        if square_search_result.is_empty:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenService.ERROR_CODE}",
                    ex=TokenDeploymentFailedException(
                        message=f"{method}: {TokenDeploymentFailedException.ERROR_CODE}",
                        ex=TokenOpeningSquareNotFoundException(
                            f"{method}: {TokenOpeningSquareNotFoundException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Run the occupation process on the opening square. ---#
        occupation_result = token.team.board.squares.add_token_to_square(
            token=token,
            square=square_search_result.payload[0],
        )
        # Handle the case that occupying the opening square fails.
        if occupation_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenServiceException(
                    message=f"{method}: {TokenService.ERROR_CODE}",
                    ex=TokenDeploymentFailedException(
                        message=f"{method}: {TokenDeploymentFailedException.ERROR_CODE}",
                        ex=occupation_result.exception
                    )
                )
            )
        # --- Assure that token.board_state has been updated. ---#
        if token.board_state == TokenBoardState.NEVER_BEEN_PLACED:
            token.board_state = TokenBoardState.DEPLOYED_ON_BOARD
            
        # Send the success result to the caller.
        return InsertionResult.success()
