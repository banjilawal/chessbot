# src/chess/environment/turn.py

"""
Module: chess.environment.turn
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.1
"""


from typing import Optional

from chess.piece import Piece
from chess.board import Board
from chess.square import Square
from chess.enviroment.scene import Scene


class TurnScene(Scene[Piece, Board, Square]):
    
    def __init__(self, id: int, actor: Piece, board: Board, actor_square: Optional[Square]=None):
        super().__init__(actor=actor, stage=board, prop=actor_square)
        
        
    @property
    def board(self) -> Board:
        return self._stage
    
    @property
    def actor_square(self) -> Optional[Square]:
        return self._prop
    
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, TurnScene):
                return self.actor.id == other.actor.id
        return False
        
