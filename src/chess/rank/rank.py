from abc import ABC, abstractmethod
from typing import List, Optional

from chess.geometry.board import Board
from chess.piece.piece import Piece, Label
from chess.game.record.turn_record import TurnRecord
from chess.motion.search_pattern import SearchPattern
from chess.motion.walk import Walk
from chess.rank.rank_value import RankValue


class Rank(ABC):
    _name: str
    _walk: Walk
    _value: RankValue
    _members: dict[Label, Piece]
    _quadrants: List[Quadrant]
    _search_pattern: SearchPattern

    def __init__(
            self,
            name: str,
            walk: Walk,
            value,
            quadrants: List[Quadrant],
            members: List[Piece],
            search_pattern: SearchPattern
     ):
        self._value = value
        self._name = name
        self._walk = walk
        self._search_pattern = search_pattern

        self._quadrants = []
        for quadrant in quadrants:
            self._quadrants.append(quadrant)

        self._members = {}
        for member in members:
            self._members[member.label] = member

    @property
    def value(self) -> int:
        return self._value

    @property
    def name(self) -> str:
        return self._name

    @property
    def quadrants(self) -> List[Quadrant]:
        return self._quadrants.copy()

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











