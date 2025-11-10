# src/chess/environment/validator

"""
Module: chess.environment.validator
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.1
"""
from typing import cast

from chess.board import (
    Board, BoardSearchContext, BoardSquareSearch, BoardValidator,
    SquareInvariantBreachException
)
from chess.board.search.context.builder import BoardSearchContextBuilder
from chess.enviroment import (
    PieceDoesNotOwnCurrentSquareException, PieceNotOnRosterCannotActException,
    NullTurnSceneException, TurnScene
)
from chess.enviroment.exception import (
    ActorAndScenePropCoordMismatchException, CheckmatedKingCannotActException,
    PieceNotOnBoardCannotActException, PieceWithNoStartingPlacementException
)
from chess.king import KingPiece
from chess.pawn import ActorNotOnBoardException, ActorPlacementRequiredException, CapturedPieceCannotActException
from chess.piece import CombatantPiece, Piece, PieceValidator
from chess.square import Square
from chess.system import IdValidator, LoggingLevelRouter, Validator, ValidationResult


class TurnSceneValidator(Validator[TurnScene]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate) -> ValidationResult[TurnScene]:
        """"""
        method = "TurnSceneValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullTurnSceneException(f"{method}: {NullTurnSceneException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, TurnScene):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected TurnScene object received {candidate.__class__.__name__} instead")
                )
            
            turn_scene = cast(TurnScene, candidate)
            
            id_validation = IdValidator.validate(turn_scene.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)

            board_validator = BoardValidator.validate(turn_scene.board)
            if board_validator.is_failure():
                return ValidationResult.failure(board_validator.exception)
              
            actor_validation = cls._actor_validation_helper(piece=turn_scene.actor, board=turn_scene.board)
            if actor_validation.is_failure():
                return ValidationResult.failure(actor_validation.exception)
            
            actor = turn_scene.actor
            board = turn_scene.board
            
            if turn_scene.square is None:
                square_validation = cls._actor_square_validation_helper(actor=actor, board=board)
                if square_validation.is_failure():
                    return ValidationResult.failure(square_validation.exception)
                return ValidationResult.success(turn_scene)
            
            if turn_scene.square is not None and turn_scene.actor_square.coord != actor.coord:
                return ValidationResult.failure(
                    ActorAndScenePropCoordMismatchException(
                        f"{method}: {ActorAndScenePropCoordMismatchException.DEFAULT_MESSAGE}"
                    )
                )
            
            if turn_scene.square is not None and turn_scene.square.occupant == actor:
                return ValidationResult.success(turn_scene)

        except Exception as e:
            return ValidationResult.failure(e)
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _actor_square_validation_helper(cls, actor: Piece, board: Board) -> ValidationResult[Square]:
        """"""
        method = "TurnScene._actor_square_validation_helper"
        
        try:
            search_context_build = BoardSearchContextBuilder.build(coord=actor.current_position)
            if search_context_build.is_failure():
                return ValidationResult.failure(search_context_build.exception)
            search_context = cast(BoardSearchContext, search_context_build.payload)
            
            search_result = BoardSquareSearch.search(board=board, search_context=search_context)
            if search_result.is_failure():
                return ValidationResult.failure(search_result.exception)
            
            if search_result.is_empty():
                return ValidationResult.failure(
                    SquareInvariantBreachException(f"{method}: {SquareInvariantBreachException.DEFAULT_MESSAGE}")
                )
            
            actor_square = cast(Square, search_result.payload)
            
            if actor_square.occupant is None:
                actor_square.occupant = actor
            
            if actor_square.occupant != actor:
                return ValidationResult.failure(
                    PieceDoesNotOwnCurrentSquareException(
                        f"{method}: {PieceDoesNotOwnCurrentSquareException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(actor_square)
        except Exception as e:
            return ValidationResult.failure(e)
        
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _actor_validation_helper(cls, piece: Piece, board: Board) -> ValidationResult[PieceValidator]:
        """"""
        method = "TurnSceneValidator._actor_validation_helper"
        
        try:
            piece_validation = PieceValidator.validate(piece)
            if piece_validation.is_failure():
                return ValidationResult.failure(piece_validation.exception)
            
            if piece not in board.pieces:
                return ValidationResult.failure(
                    PieceNotOnBoardCannotActException(
                        f"{method}: {PieceNotOnBoardCannotActException.DEFAULT_MESSAGE}"
                    )
                )
            
            if isinstance(piece, KingPiece) and cast(KingPiece, piece).is_checkmated:
                return ValidationResult.failure(
                    CheckmatedKingCannotActException(
                        f"{method}: {CheckmatedKingCannotActException.DEFAULT_MESSAGE}"
                    )
                )
            
            if isinstance(piece, CombatantPiece):
                combatant_piece = cast(CombatantPiece, piece)
                team = combatant_piece.team
                
                if combatant_piece.captor is not None:
                    return ValidationResult.failure(
                        CapturedPieceCannotActException(
                            f"{method}: {CapturedPieceCannotActException.DEFAULT_MESSAGE}"
                        )
                    )
                
                if combatant_piece not in team.roster:
                    return ValidationResult.failure(
                        PieceNotOnRosterCannotActException(
                            f"{method}: {PieceNotOnRosterCannotActException.DEFAULT_MESSAGE}"
                        )
                    )
            
            if piece.current_position is None or piece.positions.is_empty():
                return ValidationResult.failure(
                    PieceWithNoStartingPlacementException(
                        f"{method}: {PieceWithNoStartingPlacementException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(piece)
        except Exception as e:
            return ValidationResult.failure(e)
        