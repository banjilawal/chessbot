from typing import List

from chess.geometry.coordinate.coordinate import Coordinate
from chess.team.element.piece import ChessPiece


class ScoutReport:
    _id: int
    _scout: ChessPiece
    _locations: List[Coordinate]

    def __init__(self, scout_report_id: int, scout: ChessPiece, locations: List[Coordinate]):
        self._scout = scout
        self._locations = locations
        self._id = scout_report_id

    @property
    def id(self) -> int:
        return self._id

    @property
    def scout(self) -> ChessPiece:
        return self._scout

    @property
    def locations(self) -> List[Coordinate]:
        return self._locations


    def __eq__(self, other) -> bool:
        if other is self: return True
        if other is None: return False
        if not isinstance(other, ScoutReport): return False
        return self._id == other.id


    def __hash__(self) -> int:
        return hash(self._id, self._scout.id)


    def __str__(self) -> str:
        return (f"ScoutReport(id:{self._id} "
                f"scout:{self._scout.name} "
                f"number_of_locations:{len(self._locations)}"
        )