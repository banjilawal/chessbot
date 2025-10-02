from chess.board import Board
from chess.square import Square
from chess.piece import Piece, CombatantPiece
from chess.event.occupation import OccupationEvent

class AttackEvent(OccupationEvent):
    _board: Board
    _actor_square: Square
    _enemy: CombatantPiece


    def __init__(
        self,
        event_id: int,
        actor: Piece,
        enemy: CombatantPiece,
        actor_square: Square,
        destination_square: Square
    ):
        super().__init__(event_id=event_id, actor=actor, destination_square=destination_square)
        self._enemy = enemy
        self._actor_square = actor_square

    @property
    def enemy(self) -> CombatantPiece:
        return self._enemy

    @property
    def actor_square(self) -> Square:
        return self._actor_square

    @property
    def destination_square(self) -> Square:
        return super().destination_square

    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, AttackEvent):
                return self._id == other.id
        return False