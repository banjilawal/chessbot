from typing import List, TYPE_CHECKING, cast

from assurance.validators.id import IdValidator
from assurance.validators.owner import OwnerValidator
from chess.common.color import GameColor
from chess.config.team import TeamConfig
from chess.geometry.quadrant import Quadrant
from chess.team.piece import PieceList
from chess.token.model.combatant import CombatantPiece

from chess.token.model.mobility_status import MobilityStatus


if TYPE_CHECKING:
    from chess.owner.model import Owner
    from chess.token.model.base import Piece


class Team:
    _id: int
    _owner: 'Owner'
    _conf: TeamConfig
    _pieces: List[Piece]

    def __init__(self, team_id: int, owner: 'Owner', conf: TeamConfig):
        method = "Team.__init__"

        id_validation = IdValidator.validate(team_id)
        if not id_validation.is_success():
            raise id_validation.exception
        team_id = cast(id_validation.payload, int)

        owner_validation = OwnerValidator.validate(owner)
        if not owner_validation.is_success():
            raise owner_validation.exception
        owner = cast(owner_validation.payload, Owner)

        if owner is not None and self not in owner.team_history:
            owner.team_history.push_team(self)

        self._id = team_id
        self._owner = owner
        self._conf = conf
        self._pieces = PieceList()


        #
        # print("Team owner is", owner.id) if owner is not None else print("Team owner is None")


    @property
    def id(self) -> int:
        return self._id


    @property
    def owner(self) -> 'Owner':
        return self._owner


    @property
    def conf(self) -> TeamConfig:
        return self._conf


    @property
    def pieces(self) -> PieceList:
        return self._pieces




    def free_pieces(self) -> List['Piece']:
        matches: List['Piece'] = []

        for piece in self._pieces:
            if isinstance(piece, CombatantPiece):
                combatant = cast(piece, CombatantPiece)
                if combatant.captor in None:
                    matches.append(combatant)

        return matches


    def captured_pieces(self) -> List['Piece']:
        matches: List['Piece'] = []

        for piece in self._pieces:
            if isinstance(piece, CombatantPiece):
                combatant = cast(piece, CombatantPiece)
                if combatant.captor is not None:
                    matches.append(combatant)

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