from abc import ABC
from typing import List, TYPE_CHECKING, Optional
from chess.team.model.team import Team

# if TYPE_CHECKING:


class Owner(ABC):
    _id: int
    _name: str
    _team: Team

    def __init__(self, owner_id: int, name: str, team: Optional[Team] = None):
        self._id = owner_id
        self._name = name
        self._team = team


    @property
    def id(self) -> int:
        return self._id


    @property
    def name(self) -> str:
        return self._name


    @property
    def team(self) -> Team:
        return self._team

    @team.setter
    def team(self, team: Team):
        self._team = team

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Owner):
            return False
        return self.id == other.id



    def __str__(self):
        return f"Player[{self._id} {self._name} {self._team}]"



    # def move_chess_piece(self, chess_piece: 'ChessPiece', destination: Coordinate, board: 'ChessBoard'):
    #     chess_piece.forward_move_request(board, destination)





    # @staticmethod
    # def occupy_destination(self, chess_piece: ChessPiece, destination: Coordinate, chess_board: ChessBoard):
    #    if chess_piece is None:
    #        print("BishopMotionController is None")
    #        return None
    #    if chess_piece.current_position() is None:
    #        print("BishopMotionController current position is None.")
    #
    #        return None
    #    if chess_board is None:
    #        print("ChessBoard is None")
    #        return None
    #    if not chess_board.coordinate_is_valid(destination):
    #        print("Destination is not valid")
    #        return None
    #    if not Diagonal.points_match_pattern(chess_piece.current_position(), destination):
    #        print("points are not in diagonal pattern")
    #        return
    #    chess_board.capture_square(chess_piece, destination)