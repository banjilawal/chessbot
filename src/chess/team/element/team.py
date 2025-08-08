from typing import List, TYPE_CHECKING

from chess.common.game_color import GameColor
from chess.geometry.quadrant import Quadrant
from chess.team.model.play_order import PlayOrder

if TYPE_CHECKING:
    from chess.team.model.piece import ChessPiece

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


    @property
    def home_quadrant(self) -> Quadrant:
        return self._home_quadrant


    @property
    def captives(self) -> List['ChessPiece']:
        return self._captives


    @property
    def chess_pieces(self) -> List['ChessPiece']:
        return self._chess_pieces


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Team):
            return False
        return self.id == other.id


    def __hash__(self):
        return hash(self.id)


    def find_chess_piece(self, piece_id: int):
        for piece in self._chess_pieces:
            if piece.id == piece_id:
                return piece
        return None


    def find_chess_piece_name(self, name):
        for piece in self._chess_pieces:
            if name.upper() == piece.name.upper():
                return piece
        return None


    def enemy_back_row_index(self):
        if self.back_rank_index == 0:
            return 7
        else:
            return 0


    def __str__(self):
        return (f"Team id:{self._id} color:{self._color} play_order{self._team_order} rank_row:{self._back_row_index} "
                f"pawn_row:{self._pawn_row_index} home:{self._home_quadrant}")








    # @staticmethod
    # def occupy_destination(self, chess_piece: ChessPiece, destination: Coordinate, chess_board: ChessBoard):
    #    if chess_piece is None:
    #        print("BishopRank is None")
    #        return None
    #    if chess_piece.current_position() is None:
    #        print("BishopRank current position is None.")
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