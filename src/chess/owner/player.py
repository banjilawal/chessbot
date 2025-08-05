from abc import ABC
from typing import List, TYPE_CHECKING

from chess.common.game_color import GameColor
from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.line.quadrant import Quadrant

if TYPE_CHECKING:
    from chess.team.model.piece import ChessPiece

class Player(ABC):
    _id: int
    _name: str
    _color: GameColor
    _captives: List['ChessPiece']
    _home_quadrant: Quadrant
    _chess_pieces: List['ChessPiece']

    def __init__(self, player_id: int, name: str, color: GameColor):
        self._id = player_id
        self._name = name
        self._color = color
        self._captives = []
        self._chess_pieces = []


    @property
    def id(self) -> int:
        return self._id


    @property
    def name(self) -> str:
        return self._name


    @property
    def color(self) -> GameColor:
        return self._color


    @property
    def captives(self) -> List['ChessPiece']:
        return self._captives


    @property
    def chess_pieces(self) -> List['ChessPiece']:
        return self._chess_pieces


    @property
    def home_quadrant(self) -> Quadrant:
        return self._home_quadrant


    def move_chess_piece(self, chess_piece: 'ChessPiece', destination: Coordinate, board: 'ChessBoard'):
        chess_piece.forward_move_request(board, destination)





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