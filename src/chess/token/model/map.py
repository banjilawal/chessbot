from typing import TYPE_CHECKING, List

from chess.exception.null.record import NullRecordException
from chess.geometry.coord import Coordinate

if TYPE_CHECKING:
    from chess.token.model import Piece


class Record:
    _team_id: int
    _piece_id: int
    _piece_name: str
    _rank_id: int
    _location: Coordinate


    def __init__(self, piece: 'Piece'):
        self._piece_id = piece.id
        self._piece_name = piece.name
        self._rank_id = piece.rank.id
        self._team_id = piece.team.id
        self._location = piece.current_coordinate


    @property
    def team_id(self):
        return self.team_id


    @property
    def rank_id(self):
        return self.team_id


    @property
    def piece_id(self) -> int:
        return self._piece_id


    @property
    def piece_name(self) -> str:
        return self._piece_name


    @property
    def piece_location(self) -> Coordinate:
        return self._location


class ObservationChart:
    _items: List[Record]

    def __init__(self):
        self._items = []


    @property
    def items(self) -> List[Record]:
        return self._items


    def add_record(self, record: Record):
        method = "RecordList.add_record"

        if record is None:
            raise NullRecordException(f"{method}: {NullRecordException.DEFAULT_MESSAGE}")

        if record not in self._items:
            self._items.append(record)


    def reset(self):
        self._items.clear()








