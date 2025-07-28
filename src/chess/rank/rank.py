from abc import ABC, abstractmethod
from typing import List, Optional

from chess.geometry.board import Board
from chess.geometry.coordinate import Coordinate
from chess.geometry.quadrant import Quadrant
from chess.motion.motion import Motion
from chess.piece.piece import Piece, Label
from chess.game.record.turn_record import TurnRecord


class Rank(ABC):
    _name: str
    _acronym: str
    _motion: Motion
    _capture_value: int
    _members: List[Piece]
    _territories: List[Quadrant]

    def __init__(
        self, 
        name: str, 
        acronym: str, 
        motion: Motion, 
        capture_value: int, 
        territories: List[Quadrant]
    ):
        self._name = name
        self._members = []
        self._motion = motion
        self._acronym = acronym
        self._capture_value = capture_value
        self._territories = territories


    @property
    def name(self) -> str:
        return self._name


    @property
    def acronym(self) -> str:
        return self._acronym
    
    @property
    def motion(self):
        return self._motion


    @property
    def capture_value(self) -> int:
        return self._capture_value

    @property
    def territories(self) -> List[Quadrant]:
        return self._territories.copy()

    @property
    def members(self) -> [Piece]:
        return self._members

    @property
    def acronym(self) -> str:
        return self._acronym

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Rank):
            return False
        return self._name == other.name

    def __hash__(self):
        return hash(self._name)

    def __str__(self):
        return (f"{self._name}, value:{self._acronym}, {self._capture_value} "
                f"num_members:{len(self._members)} num_territories:{len(self._territories)}")


    @abstractmethod
    def move(self, piece: Piece, board: Board, destination: Coordinate) -> Optional[TurnRecord]:
        pass


    @abstractmethod
    def explore(self, piece: Piece, board: Board): List[Coordinate]



class PromotableRank(Rank):

    @abstractmethod
    def promote(self, piece) -> TurnRecord:
        pass

    # @abstractmethod
    # def is_promoted(self) -> bool:
    #     pass

    # def promote(self, piece: Piece) -> Piece:
    #     pass
        # if piece is None:
        #     raise ValueError("Cannot promote null piece cannot be null.")
        #     print("new_rank cannot be null or empty.")
        #     return None
        # return Piece(
        #     piece_id=self.id,
        #     label=self.name,
        #     team=self.team,
        #     rank=QueenRank(QueenSearchPattern())
        # )









