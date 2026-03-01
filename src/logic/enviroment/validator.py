# src/logic/environment/coord_stack_validator

"""
Module: logic.environment.coord_stack_validator
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.1
"""
from typing import cast

from logic.board import (
    Board, BoardContext, BoardSquareFinder, BoardValidator,
    SquareInvariantBreachException
)
from logic.board.search.context.builder import BoardContextBuilder
from logic.enviroment import (
    PieceDoesNotOwnCurrentSquareException, PieceNotOnRosterCannotActException,
    NullTurnSceneException, TurnScene
)
from logic.enviroment.exception import (
    ActorAndScenePropCoordMismatchException, CheckmatedKingCannotActException,
    PieceNotOnBoardCannotActException, PieceWithNoStartingPlacementException
)
from logic.king import KingPiece
from logic.pawn import ActorNotOnBoardException, ActorPlacementRequiredException, CapturedPieceCannotActException
from logic.piece import CombatantPiece, Piece, PieceValidator
from logic.square import Square
from logic.system import IdValidator, LoggingLevelRouter, Validator, ValidationResult


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
                    NullTurnSceneException(f"{method}: {NullTurnSceneException.MSG}")
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
                        f"{method}: {ActorAndScenePropCoordMismatchException.MSG}"
                    )
                )
            
            if turn_scene.square is not None and turn_scene.square.occupant == actor:
                return ValidationResult.success(turn_scene)

        except Exception as e:
            return ValidationResult.failure(e)
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def actor_square_validation_helper(cls, actor: Piece, board: Board) -> ValidationResult[Square]:
        """"""
        method = "TurnScene._actor_square_validation_helper"
        
        try:
            search_context_build = BoardContextBuilder.build(coord=actor.current_position)
            if search_context_build.is_failure():
                return ValidationResult.failure(search_context_build.exception)
            search_context = cast(BoardContext, search_context_build.payload)
            
            search_result = BoardSquareFinder.search(board=board, search_context=search_context)
            if search_result.is_failure():
                return ValidationResult.failure(search_result.exception)
            
            if search_result.is_empty():
                return ValidationResult.failure(
                    SquareInvariantBreachException(f"{method}: {SquareInvariantBreachException.MSG}")
                )
            
            actor_square = cast(Square, search_result.payload)
            
            if actor_square.occupant is None:
                actor_square.occupant = actor
            
            if actor_square.occupant != actor:
                return ValidationResult.failure(
                    PieceDoesNotOwnCurrentSquareException(
                        f"{method}: {PieceDoesNotOwnCurrentSquareException.MSG}"
                    )
                )
            
            return ValidationResult.success(actor_square)
        except Exception as e:
            return ValidationResult.failure(e)
        
    
    @classmethod
    @LoggingLevelRouter.monitor
    def actor_board_validation_helper(cls, piece: Piece, board: Board) -> ValidationResult[PieceValidator]:
        """"""
        method = "TurnSceneValidator._actor_validation_helper"
        
        try:
            piece_validation = PieceValidator.validate(piece)
            if piece_validation.is_failure():
                return ValidationResult.failure(piece_validation.exception)
            
            if piece not in board.pieces:
                return ValidationResult.failure(
                    PieceNotOnBoardCannotActException(
                        f"{method}: {PieceNotOnBoardCannotActException.MSG}"
                    )
                )
            
            if isinstance(piece, KingPiece) and cast(KingPiece, piece).is_checkmated:
                return ValidationResult.failure(
                    CheckmatedKingCannotActException(
                        f"{method}: {CheckmatedKingCannotActException.MSG}"
                    )
                )
            
            if isinstance(piece, CombatantPiece):
                combatant_piece = cast(CombatantPiece, piece)
                team = combatant_piece.team
                
                if combatant_piece.victor is not None:
                    return ValidationResult.failure(
                        CapturedPieceCannotActException(
                            f"{method}: {CapturedPieceCannotActException.MSG}"
                        )
                    )
                
                if combatant_piece not in team.roster:
                    return ValidationResult.failure(
                        PieceNotOnRosterCannotActException(
                            f"{method}: {PieceNotOnRosterCannotActException.MSG}"
                        )
                    )
            
            if piece.current_position is None or piece.positions.is_empty():
                return ValidationResult.failure(
                    PieceWithNoStartingPlacementException(
                        f"{method}: {PieceWithNoStartingPlacementException.MSG}"
                    )
                )
            
            return ValidationResult.success(piece)
        except Exception as e:
            return ValidationResult.failure(e)
        