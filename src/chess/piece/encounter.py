from typing import TYPE_CHECKING, List

from chess.coord import Coord

if TYPE_CHECKING:
    from chess.piece.piece import Piece

class Encounter:
    _id: int
    _name: str
    _team_id: int
    _ransom: int
    _rank_name: str
    _coord: Coord


    def __init__(self, discovery: 'Piece'):
        self._id = discovery.id
        self._name = discovery.name
        self._ransom = discovery.rank.ransom
        self._rank_name = discovery.rank.name
        self._team_id = discovery.team.id
        self._coord = discovery.current_position

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def team_id(self):
        return self._team_id

    @property
    def rank_name(self) -> str:
        return self._rank_name

    @property
    def ransom(self):
        return self._ransom

    @property
    def coord(self) -> Coord:
        return self._coord

    def __eq__(self, other):
        """We have to use the coord because the id """
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance('Encounter', other):
            return False
        return self._id == other.id and self._coord == other.coord


    def __str__(self):
        return (
            f"Encounter[id:{self._id} "
            f"name:{self._name} "
            f"rank:{self._rank_name} "
            f"value:{self._ransom} "
            f"coord:{self._coord}"
        )











