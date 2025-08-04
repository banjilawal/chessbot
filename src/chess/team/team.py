from multiprocessing.process import parent_process
from typing import Optional, List, TYPE_CHECKING

from chess.common.game_color import GameColor
from chess.geometry.quadrant import Quadrant
from chess.team.play_order import PlayOrder

if TYPE_CHECKING:
    from chess.piece.piece import ChessPiece

class Team:
    _id: int
    _letter: str
    _color: GameColor
    _team_order: PlayOrder
    _back_row_index: int
    _pawn_row_index: int
    _home_quadrant: Quadrant
    _captives: List['ChessPiece']
    _chess_pieces: List['ChessPiece']

    def __init__(
        self,
        team_id: int,
        letter: str,
        team_color: GameColor,
        team_order: PlayOrder,
        back_row_index: int,
        pawn_row_index: int,
        home_quadrant: Quadrant
    ):
        self._id = team_id
        self._letter = letter
        self._color = team_color
        self._team_order = team_order
        self._back_row_index = back_row_index
        self._pawn_row_index = pawn_row_index
        self._home_quadrant = home_quadrant
        self._captives = []
        self._chess_pieces = []


    @property
    def id(self) -> int:
        return self._id


    @property
    def letter(self) -> str:
        return self._letter


    @property
    def color(self) -> GameColor:
        return self._color


    @property
    def team_order(self) -> PlayOrder:
        return self._team_order


    @property
    def back_rank_index(self) -> int:
        return self._back_row_index


    @property
    def pawn_rank_index(self) -> int:
        return self._pawn_row_index


    @@property
    def home_quadrant(self) -> Quadrant:
        return self._home_quadrant


    @property
    def captives(self) -> List['ChessPiece']:
        return self._captives


    @property
    def chess_pieces(self) -> List['ChessPiece']:
        return self._chess_pieces








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