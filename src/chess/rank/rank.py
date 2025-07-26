from abc import ABC, abstractmethod
from typing import List, Optional

from chess.geometry.board import Board
from chess.geometry.quadrant import Quadrant
from chess.piece.piece import Piece, Label
from chess.game.record.turn_record import TurnRecord
from chess.motion.search_pattern import SearchPattern
from chess.motion.walk import Walk
from chess.rank.rank_value import RankConfig


class Rank(ABC):
    _capture_value: int
    _members: List[Piece]
    _territories: List[Quadrant]

    def __init__(self, name: str, capture_value: int, territories: List[Quadrant]):
        self._capture_value = capture_value
        self._name = name
        self._members = []
        self._territories = territories


    @property
    def value(self) -> int:
        return self._capture_value

    @property
    def name(self) -> str:
        return self._name

    @property
    def quadrants(self) -> List[Quadrant]:
        return self._territories.copy()

    @property
    def members(self) -> [Label, Piece]:
        return self._members.copy()

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Rank):
            return False
        return self._name == other.name


    @abstractmethod
    def move(self, piece: Piece, board: Board, destination: Coordinate) -> Optional[TurnRecord]:
        pass

    @abstractmethod
    def walk(self) -> List[Coordinate]:
        pass

    @abstractmethod
    def search_pattern(self) -> List[Coordinate]:
        pass

    @abstractmethod
    def explore(self, piece: Piece, board: Board): List[Coordinate]

    @abstractmethod
    def select_destination(self):
        pass


class PromotableRank(Rank):

    @abstractmethod
    def promote(self, piece) -> TurnRecord:
        pass

    @abstractmethod
    def is_promoted(self) -> bool:
        pass











