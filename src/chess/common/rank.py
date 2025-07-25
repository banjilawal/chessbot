from abc import ABC, abstractmethod
from typing import List, Optional

from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.common.piece import Piece, Label
from chess.game.record.turn_record import TurnRecord
from chess.motion.quadrant import Quadrant
from chess.motion.search_pattern import SearchPattern
from chess.motion.walk import Walk


class Rank(ABC):
    _id: int
    _name: str
    _walk: Walk
    _members: dict[Label, Piece]
    _quadrants: List[Quadrant]
    _search_pattern: SearchPattern

    def __init__(
            self,
            rank_id,
            name: str,
            walk: Walk,
            quadrants: List[Quadrant],
            members: List[Piece],
            search_pattern: SearchPattern
     ):
        self._id = rank_id
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
    def id(self) -> id:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def quadrants(self) -> List[Quadrant]:
        return self._quadrants.copy()

    @property
    def members(self) -> [Label, Piece]:
        return self._members.copy()


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












