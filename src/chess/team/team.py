from typing import List, TYPE_CHECKING

from chess.common.game_color import GameColor
from chess.geometry.quadrant import Quadrant
from chess.owner.owner import Owner
from chess.token.mobility_status import MobilityStatus

if TYPE_CHECKING:
    from chess.token.chess_piece import ChessPiece


class Team:
    _id: int
    _letter: str
    _owner: Owner
    _color: GameColor
    _back_row_index: int
    _pawn_row_index: int
    _home_quadrant: Quadrant
    _chess_pieces: List['ChessPiece']

    def __init__(
        self,
        team_id: int,
        letter: str,
        team_color: GameColor,
        back_row_index: int,
        pawn_row_index: int,
        home_quadrant: Quadrant,
        owner: Owner = None
    ):
        self._id = team_id
        self._letter = letter
        self._color = team_color
        self._back_row_index = back_row_index
        self._pawn_row_index = pawn_row_index
        self._home_quadrant = home_quadrant
        self._chess_pieces = []
        self._owner = owner

        if owner is not None:
            owner.team_stack.push_team(self)


    @property
    def id(self) -> int:
        return self._id


    @property
    def letter(self) -> str:
        return self._letter


    @property
    def owner(self) -> Owner:
        return self._owner


    @owner.setter
    def owner(self, owner: Owner):
        self._owner = owner
        if owner is not None:
            owner.team_stack.push_team(self)



    @property
    def color(self) -> GameColor:
        return self._color


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
    def chess_pieces(self) -> List['ChessPiece']:
        return self._chess_pieces


    def free_chess_pieces(self) -> List['ChessPiece']:
        matches: List['ChessPiece'] = []

        for chess_piece in self._chess_pieces:
            if chess_piece.status == MobilityStatus.FREE and chess_piece not in matches:
                matches.append(chess_piece)
        return matches


    def blocked_chess_pieces(self) -> List['ChessPiece']:
        matches: List['ChessPiece'] = []

        for chess_piece in self._chess_pieces:
            if (
                chess_piece.status == MobilityStatus.BLOCKED_FROM_MOVING and
                chess_piece not in matches
            ):
                matches.append(chess_piece)
        return matches


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
        return (f"Team id:{self._id} color:{self._color}  rank_row:{self._back_row_index} "
                f"pawn_row:{self._pawn_row_index} home:{self._home_quadrant}")