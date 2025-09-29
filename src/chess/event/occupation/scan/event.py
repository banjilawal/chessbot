from chess.piece import Piece
from chess.square import Square
from  chess.event.occupation import OccupationEvent

class ScanEvent(OccupationEvent):
    _subject: Piece

    def __init__(self, event_id: int, actor: Piece, subject: Piece, destination_square: Square):
        super().__init__(event_id=event_id, actor=actor, destination_square=destination_square)
        self._subject = subject

    @property
    def observer(self) -> Piece:
        return self.actor

    @property
    def subject(self) -> Piece:
        return self._subject

    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, ScanEvent):
                return self._subject.id == other.subject.id
        return False