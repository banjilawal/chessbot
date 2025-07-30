from abc import abstractmethod, ABC
from typing import Optional, List, Dict, TYPE_CHECKING

from chess.geometry.board import ChessBoard
from chess.common.game_color import GameColor
from chess.geometry.coordinate import Coordinate
from chess.geometry.quadrant import Quadrant

from chess.piece.piece import ChessPiece, Label
from chess.game.record.turn_record import TurnRecord

if TYPE_CHECKING:
    from chess.geometry.board import ChessBoard
    from chess.piece.piece import ChessPiece

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
        return self._captives.copy()


    @property
    def chess_pieces(self) -> List[ChessPiece]:
        return self._chess_pieces


    @property
    def home_quadrant(self) -> Quadrant:
        return self._home_quadrant




    @abstractmethod
    def request_move(self, piece: 'ChessPiece', destination: Coordinate, board: 'ChessBoard') -> Optional[TurnRecord]:
        pass





    # @staticmethod
    # def occupy_destination(self, chess_piece: ChessPiece, destination: Coordinate, chess_board: ChessBoard):
    #    if chess_piece is None:
    #        print("Bishop is None")
    #        return None
    #    if chess_piece.current_position() is None:
    #        print("Bishop current position is None.")
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