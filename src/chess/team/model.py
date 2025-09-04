from typing import List, TYPE_CHECKING, cast, Sequence, Optional

from assurance.validators.id import IdValidator
from assurance.validators.competitor import CompetitorValidator
from chess.config.game import SideProfile
from chess.exception.null.side_profile import NullSideProfileException
from chess.exception.stack import BrokenRelationshipException

if TYPE_CHECKING:
    from chess.competitor.model import Competitor
    from chess.token.model import Piece, CombatantPiece


class Side:
    _id: int
    _controller: 'Competitor'
    _profile: SideProfile
    _pieces: list['Piece']

    def __init__(self, team_id: int, controller: 'Competitor', profile: SideProfile):
        method = "Team.__init__"

        if profile is None:
            raise NullSideProfileException(f"{method}: {NullSideProfileException.DEFAULT_MESSAGE}")

        id_validation = IdValidator.validate(team_id)
        if not id_validation.is_success():
            raise id_validation.exception
        team_id = cast(id_validation.payload, int)

        competitor_validation = CompetitorValidator.validate(controller)
        if not competitor_validation.is_success():
            raise competitor_validation.exception

        from chess.competitor.model import Competitor
        controller = cast(Competitor, competitor_validation.payload)

        self._id = team_id
        self._controller = controller
        self._profile = profile
        self._pieces = []


        if self not in controller.sides_played.items:
            controller.sides_played.push_side(self)

        if self not in controller.sides_played.items:
            raise BrokenRelationshipException(f"{method}: {BrokenRelationshipException.DEFAULT_MESSAGE}")


    @property
    def id(self) -> int:
        return self._id


    @property
    def controller(self) -> 'Competitor':
        return self._controller


    @property
    def profile(self) -> SideProfile:
        return self._profile


    @property
    def pieces(self) -> Sequence['Piece']:
        """
        Returns a read-only view of the stack's contents. The returned sequence is safe to
        iterate and index, but mutating it will not affect the original stack.
        """

        return self._pieces.copy()


    def free_pieces(self) -> List['Piece']:
        matches: List['Piece'] = []

        for piece in self._pieces:

            from chess.token.model import Piece, CombatantPiece
            if isinstance(piece, CombatantPiece):
                combatant = cast(piece, CombatantPiece)
                if combatant.captor in None:
                    matches.append(combatant)

        return matches


    def captured_pieces(self) -> List['Piece']:
        matches: List['Piece'] = []

        for piece in self._pieces:

            from chess.token.model import Piece, CombatantPiece
            if isinstance(piece, CombatantPiece):
                combatant = cast(piece, CombatantPiece)
                if combatant.captor is not None:
                    matches.append(combatant)

        return matches


    def find_piece(self, piece_id: int) -> Optional['Piece']:
        for piece in self._pieces:
            if piece.id == piece_id:
                return piece
        return None


    def find_piece_name(self, name):
        for piece in self._pieces:
            if name.upper() == piece.name.upper():
                return piece
        return None


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Side):
            return False
        return self._id == other.id


    def __hash__(self):
        return hash(self._id)


    def __str__(self):
        return f"Team[id:{self._id} competitor:{self._controller.name} {self._profile}"