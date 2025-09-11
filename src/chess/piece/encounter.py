from typing import TYPE_CHECKING, List

from chess.piece.exception.null.null_encounter import NullEncounterException
from chess.coord import Coord

if TYPE_CHECKING:
    from chess.piece.piece import Piece


class Encounter:
    _side_id:int
    _piece_id:int
    _piece_name:str
    _rank_value:int
    _rank_name:str
    _location:Coord


    def __init__(self, piece:'Piece'):
        self._piece_id = piece.id
        self._piece_name = piece.name
        self._rank_value = piece.rank.value
        self._rank_name = piece.rank.name
        self._side_id = piece.team.id
        self._location = piece.current_coord


    @property
    def side_id(self):
        return self.side_id


    @property
    def rank_value(self):
        return self._rank_value
    


    @property
    def piece_id(self) -> int:
        return self._piece_id


    @property
    def piece_name(self) -> str:
        return self._piece_name


    @property
    def piece_location(self) -> Coord:
        return self._location


class EncounterLog:
    _items:List[Encounter]

    def __init__(self):
        self._items = []


    @property
    def items(self) -> List[Encounter]:
        return self._items


    def add_encounter(self, record:Encounter):
        method = "RecordList.add_record"

        if record is None:
            raise NullEncounterException(f"{method}:{NullEncounterException.DEFAULT_MESSAGE}")

        if record not in self._items:
            self._items.append(record)


    def reset(self):
        self._items.clear()








