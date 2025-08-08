from dataclasses import dataclass


from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.coordinate.coordinate_stack import CoordinateStack
from chess.map.map_service import MapService

from chess.team.element.mobility_status import MobilityStatus

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from chess.rank.rank import Rank
    # from chess.geometry.coordinate.coordinate_stack import CoordinateStack

@dataclass(frozen=True)
class RankTag:
    member_id: int
    rank: 'Rank'


class ChessPiece:
    _id: int
    _name: str
    _team: 'Team'
    _captor: 'ChessPiece'
    _rank: 'Rank'
    _coordinate_stack: CoordinateStack
    _status: MobilityStatus

    def __init__(self, chess_piece_id: int, name: str, rank: 'Rank', team: 'Team'):
        if not chess_piece_id:
            raise ValueError("Cannot create a chess_piece with an empty id.")
        if chess_piece_id < 0:
            raise ValueError("Cannot create a chess_piece with a negative id.")
        if rank is None:
            raise ValueError("Cannot create a chess_piece with an null interfaces.")

        self._team = team
        self._name = name
        self._id = chess_piece_id
        self._status = MobilityStatus.FREE
        self._rank = rank
        self._coordinate_stack = CoordinateStack()
        team.chess_pieces.append(self)


    @property
    def id(self) -> int:
        return self._id


    @property
    def name(self) -> str:
        return self._name


    @property
    def team(self) -> 'Team':
        return self._team


    @property
    def rank(self) -> 'Rank':
        return self._rank


    @property
    def captor(self) -> 'ChessPiece':
        return self._captor


    @property
    def status(self) -> MobilityStatus:
        return self._status


    @property
    def coordinate_stack(self) -> CoordinateStack:
        return self._coordinate_stack


    @status.setter
    def status(self, status: MobilityStatus):
        if self._status != status:
            self._status = status


    @captor.setter
    def captor(self, captor: 'ChessPiece'):
        self._captor = captor


    def capture_prisoner(self, enemy: 'ChessPiece'):
        if enemy is None:
            raise Exception("Cannot captue a nonexistent enemy")
        if enemy.team == self._team:
            raise Exception("Illegal capture of friendly")
        if enemy.captor is not None:
            raise Exception("Double capture is not allowed")
        if enemy is self:
            raise Exception("Cannot capture self")

        enemy.captor = self
        enemy.status = MobilityStatus.PRISONER



    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, ChessPiece):
            return False
        if isinstance(other, ChessPiece):
            return  self._id == other.id
        return False


    def __hash__(self):
        return hash((self.id, self.rank))

    def __str__(self):
        location_str = f"current_coord:{self._coordinate_stack.current_coordinate()}"
        if self._status == MobilityStatus.PRISONER:
            location_str = f"prisoner"
        return f"ChessPiece[id:{self._id} name:{self._name} status:{self._status.name} {location_str}]"

    def is_enemy(self, chess_piece: 'ChessPiece'):
        if chess_piece is None:
            print(f"{self._name} cannot be an enemy of a null chess_piece.")
            return False
        return self._team == chess_piece.team

