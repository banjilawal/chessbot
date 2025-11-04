# src/chess/domain/builder.py

"""
Module: chess.domain.builder
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""

from chess.board import Board
from chess.piece import Piece
from chess.domain import Domain
from chess.system import Builder, BuildResult


class DomainBuilder(Builder[Domain]):
    
    @classmethod
    def build(cls, piece: Piece, board: Board) -> BuildResult[Board]:
        actor_validation = Actor