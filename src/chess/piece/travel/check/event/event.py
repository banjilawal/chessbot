from typing import Optional

from chess.board import Board
from chess.system import Event
from chess.square import Square
from chess.piece import Piece, KingPiece, TravelEvent


class KingCheckEvent(TravelEvent):
    _enemy_king: KingPiece
    
    def __init__(
        self,
        id: int,
        actor: Piece,
        enemy_king: KingPiece,
        enemy_square: Square,
        execution_environment: Board,
        parent: Optional[Event] = None
    ):
        super().__init__(
            id=id,
            actor=actor,
            parent=parent,
            destination_square=enemy_square,
            execution_environment=execution_environment
        )
        self._enemy_king = enemy_king
    
    @property
    def enemy_square(self) -> Square:
        return self.destination_square
    
    @property
    def enemy_king(self) -> KingPiece:
        return self._enemy_king
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, KingCheckEvent):
                return True
        return False
