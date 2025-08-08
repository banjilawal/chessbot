from abc import ABC
from typing import List, Optional

from chess.geometry.quadrant import Quadrant
from chess.motion.walk.walk import Walk


class Rank(ABC):
    _name: str
    _letter: str
    _walk: Walk
    # _explorer: Explorer
    _capture_value: int
    _number_per_team: int
    _territories: List[Quadrant]

    def __init__(
        self,
        name: str,
        letter: str,
        capture_value: int,
        number_per_team: int,
        territories: List[Quadrant],
        walk: Optional[Walk] = None
        # explorer:Optional[Explorer] = Explorer
    ):
        if walk is None:
            raise ValueError("Walk walk cannot be None.")
        # if explorer is None:
        #     raise ValueError("Search pattern cannot be None.")

        self._name = name
        self._walk = walk
        self._letter = letter
        # self._explorer = explorer
        self._capture_value = capture_value
        self._number_per_team = number_per_team
        self._territories = territories


    @property
    def name(self) -> str:
        return self._name


    @property
    def letter(self) -> str:
        return self._letter


    @property
    def capture_value(self) -> int:
        return self._capture_value


    @property
    def territories(self) -> List[Quadrant]:
        return self._territories.copy()


    @property
    def number_per_team(self) -> int:
        return self._number_per_team


    @property
    def walk(self) -> Walk:
        return self._walk
    #
    #
    # @property
    # def explorer(self) -> Explorer:
    #     return self._explorer


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Rank):
            return False
        return self._name.upper() == other.name.upper()


    def __hash__(self):
        return hash(self._name)


    def __str__(self):
        return (f"{self._name}, value:{self._letter}, {self._capture_value} "
                f"num_per_player:{self._number_per_team} num_territories:{len(self._territories)}")