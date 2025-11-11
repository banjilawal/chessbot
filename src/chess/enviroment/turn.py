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
from chess.system import Scene


class TurnScene(Scene[Piece, Board, Square]):
    """
    # ROLE:

    # RESPONSIBILITIES:

    # PROVIDES:
        `TurnScene`

    # ATTRIBUTES:
        `id` (`int`)
        `actor` (`Piece`): Moves, attacks, gets captured, or checkmated.
        `stage`: (`Board`): Environment where `actor` operates.
        `prop`: (`Square`): Space `actor` occupies on `Stage`
    """
    
    def __init__(self, id: int, actor: Piece, board: Board, actor_square: Optional[Square]=None):
        """
        # ACTION:
        Constructs a new `TurnScene`.

        # PARAMETERS:
            * `id` (`int`):
            * `actor` (`Piece`): Moves, attacks, gets captured, or checkmated  on `Board`.
            * `board` (`Board`): Where `actor` performs operation.
            * `actor_square` (`Square`):

        # RETURNS:
            `None`

        # RAISES:
            `None`
        """
        super().__init__(actor=actor, stage=board, prop=actor_square)
        
        
    @property
    def board(self) -> Board:
        """Convenience wrapper stage."""
        return self._stage
    
    @property
    def actor_square(self) -> Optional[Square]:
        """Convenience wrapper prop."""
        return self._prop
    
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, TurnScene):
                return self.actor.id == other.actor.id
        return False
        
