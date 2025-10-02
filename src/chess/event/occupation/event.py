from typing import Optional

from chess.piece import Piece
from chess.square import Square
from chess.transaction import Event


class OccupationEvent(Event[Piece,Square]):

    def __init__(
        self,
        event_id: int,
        actor: Piece,
        destination_square: Square,
        parent: Optional[Event]=None):
        super().__init__(event_id=event_id, actor=actor, resource=destination_square, parent=parent)

    @property
    def subject(self) -> Square:
        return self.resource

    @property
    def destination_square(self) -> Square:
        return self.resource

    def __eq__(self, other) -> bool:
        if super().__eq__(other):
            if isinstance(other, OccupationEvent):
                return self._id == other.id
        return False