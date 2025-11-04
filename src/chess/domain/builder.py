# src/chess/domain/builder.py

"""
Module: chess.domain.builder
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""

from chess.board import Board
from chess.piece import BoardActorValidator, Piece
from chess.domain import Domain
from chess.system import Builder, BuildResult, LoggingLevelRouter, id_emitter


class DomainBuilder(Builder[Domain]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, piece: Piece, board: Board) -> BuildResult[Board]:
        """"""
        method = "DomainBuilder.build"
        
        try:
            board_actor_validation = BoardActorValidator.validate(piece, board)
            if board_actor_validation.is_failure():
                return BuildResult.failure(board_actor_validation.exception)
            
            return BuildResult.success(payload=Domain(id=id_emitter.domain_id, piece=piece))
        except Exception as e:
            return BuildResult.failure(e)
