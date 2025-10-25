from typing import Optional

from chess.board import Board
from chess.square import Square
from chess.piece import OccupationEvent, Piece

class PromotionEvent(OccupationEvent[Piece, Square, Board]):
    """"""
    
    def __init__(
            self,
            id: int,
            actor: Piece,
            actor_square: Square,
            promotion_square: Square,
            execution_environment: Board,
            parent: Optional[Event] = None
    ):
        super().__init__(
            id=id,
            actor=actor,
            parent=parent,
            actor_square=actor_square,
            destination_square=promotion_square,
            execution_environment=execution_environment
        )
        
    @property
    def promotion_square(self) -> Square:
        return self.destination_square