from chess.piece import Piece
from chess.square import Square
from chess.transaction import Event


class OccupationEvent(Event[Piece,Square]):

    def __init__(self, event_id: int, actor: Piece, destination_square: Square):
        super().__init__(event_id=event_id, actor=actor, resource=destination_square)

    @property
    def subject(self) -> Square:
        return self.resource

    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        if isinstance(other, OccupationEvent):
            return self._id == other.id