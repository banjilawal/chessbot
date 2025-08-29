from typing import List, TYPE_CHECKING

from chess.common.color import GameColor
from chess.geometry.quadrant import Quadrant

from chess.token.mobility_status import MobilityStatus

if TYPE_CHECKING:
    from chess.owner.base import Owner
    from chess.token.model import Piece


class Team:
    _id: int
    _letter: str
    _owner: 'Owner'
    _color: GameColor
    _back_row_index: int
    _pawn_row_index: int
    _home_quadrant: Quadrant
    _pieces: List['Piece']

    def __init__(
        self,
        team_id: int,
        letter: str,
        team_color: GameColor,
        back_row_index: int,
        pawn_row_index: int,
        home_quadrant: Quadrant,
        owner: 'Owner'
    ):
        self._id = team_id
        self._letter = letter
        self._color = team_color
        self._back_row_index = back_row_index
        self._pawn_row_index = pawn_row_index
        self._home_quadrant = home_quadrant
        self._pieces = []


        if owner is not None and self != owner.team_stack.current_team():
            owner.team_stack.push_team(self)
        self._owner = owner

        #
        # print("Team owner is", owner.id) if owner is not None else print("Team owner is None")


    @property
    def id(self) -> int:
        return self._id


    @property
    def letter(self) -> str:
        return self._letter


    @property
    def owner(self) -> 'Owner':
        return self._owner


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
    def pieces(self) -> List['Piece']:
        return self._pieces


    @owner.setter
    def owner(self, owner: 'Owner'):
        if owner == self.owner:
            raise ValueError("Cannot set owner to the same owner.")
        if owner is not None and self != owner.team_stack.current_team():
            owner.team_stack.push_team(self)
        self._owner = owner


    def free_pieces(self) -> List['Piece']:
        matches: List['Piece'] = []

        for piece in self._pieces:
            if piece.status == MobilityStatus.FREE and piece not in matches:
                matches.append(piece)
        return matches


    def blocked_pieces(self) -> List['Piece']:
        matches: List['Piece'] = []

        for piece in self._pieces:
            if (
                piece.status == MobilityStatus.BLOCKED_FROM_MOVING and
                piece not in matches
            ):
                matches.append(piece)
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


    def find_piece(self, piece_id: int):
        for piece in self._pieces:
            if piece.id == piece_id:
                return piece
        return None


    def find_piece_name(self, name):
        for piece in self._pieces:
            if name.upper() == piece.name.upper():
                return piece
        return None


    def enemy_back_row_index(self):
        if self.back_rank_index == 0:
            return 7
        else:
            return 0


    def __str__(self):
        return (
            f"owner name: {self._owner} "
            f"Team id:{self._id} "
            f"color:{self._color}  "
            f"rank_row:{self._back_row_index} "
            f"pawn_row:{self._pawn_row_index} "
            f"home:{self._home_quadrant}]"
        )