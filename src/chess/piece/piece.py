from dataclasses import dataclass


from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.coordinate.coordinate_stack import CoordinateStack

from chess.piece.mobility_status import MobilityStatus

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from chess.motion.abstract.motion_controller import MotionController
    from chess.team.team import Team
    from chess.geometry.board.board import ChessBoard
    # from chess.geometry.coordinate.coordinate_stack import CoordinateStack

@dataclass(frozen=True)
class RankTag:
    member_id: int
    rank: 'MotionController'


class ChessPiece:
    _id: int
    _name: str
    _team: 'Team'
    _rank: 'MotionController'
    _coordinate_stack: CoordinateStack
    _status: MobilityStatus

    def __init__(self, chess_piece_id: int, name: str, rank: 'MotionController', team: 'Team'):
        if not chess_piece_id:
            raise ValueError("Cannot create a chess_piece with an empty id.")
        if chess_piece_id < 0:
            raise ValueError("Cannot create a chess_piece with a negative id.")
        if rank is None:
            raise ValueError("Cannot create a chess_piece with an null abstract.")

        self._id = chess_piece_id
        self._team = team
        self._rank = rank
        self._name = name
        self._status = MobilityStatus.FREE
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
    def rank(self) -> 'MotionController':
        return self._rank


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

    def forward_move_request(self, chess_board: 'ChessBoard', destination: Coordinate):
        return self._rank.delegate_move_excution(piece=self, board=chess_board, destination=destination)


    def explore_destinations(self, board: 'ChessBoard') -> List[Coordinate]:

        print(f"Everything is fine with {self._name} calling MotionController.explore for the list")
        return self._rank.explore(self, board)


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, ChessPiece):
            return False
        if isinstance(other, ChessPiece):
            return  self._id == other.id and self._rank == other.rank
        return False


    def __hash__(self):
        return hash((self.id, self.rank))

    def __str__(self):
        return f"{self._id} {self._name} {self._status.name} stack_size:{self._coordinate_stack} + current:{self._coordinate_stack.current_coordinate()}"

    def is_enemy(self, chess_piece: 'ChessPiece'):
        if chess_piece is None:
            print(f"{self._name} cannot be an enemy of a null chess_piece.")
            return False
        return self._team == chess_piece.team

