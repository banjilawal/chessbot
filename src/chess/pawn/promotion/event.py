# src/chess/travel/promotion/factory.py

"""
Module: chess.travel.promotion.event
Author: Banji Lawal
Created: 2025-10-16
version: 1.0.0
"""

from typing import Optional

from chess.board import Board
from chess.rank import Queen, Rank
from chess.system import Event
from chess.square import Square
from chess.piece import OccupationEvent, Piece, TravelEvent


class PromotionEvent(TravelEvent[Piece, Square, Board]):
    """"""
    _new_rank: Rank
    
    def __init__(
            self,
            id: int,
            actor: Piece,
            actor_square: Square,
            execution_environment: Board,
            parent: Optional[Event] = None,
            new_rank: Rank = Queen
    ):
        super().__init__(
            id=id,
            actor=actor,
            parent=parent,
            actor_square=actor_square,
            execution_environment=execution_environment
        )
        self._new_rank = new_rank
        
    @property
    def new_rank(self) -> Rank:
        return self._new_rank