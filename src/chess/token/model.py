from abc import ABC
from typing import TYPE_CHECKING, Optional, cast

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.name import NameValidationException

from assurance.exception.validation.team import SideValidationException
from assurance.validators.id import IdValidator
from assurance.validators.name import NameValidator

from assurance.validators.side import SideValidator
from chess.exception.null.piece import NullPieceException
from chess.exception.piece import MappingSelfException, PrisonerReleaseException, NullCaptorException
from chess.geometry.coord import Coordinate
from chess.team.model import Side
from chess.token.coord import CoordinateStack
from chess.token.encounter import Encounter, EncounterLog


if TYPE_CHECKING:
    from chess.rank.base import Rank
    # from assurance.validators.rank import RankValidator
    # from chess.geometry.coordinate.coordinate_stack import CoordinateStack

    """"
    
    """


class Piece(ABC):
    _id: int
    _name: str
    _side: 'Side'
    _rank: 'Rank'
    _captor: 'Piece'
    _current_position: Coordinate
    # _status: MobilityStatus
    _observations: EncounterLog
    _positions: CoordinateStack


    def __init__(self, piece_id: int, name: str, rank: 'Rank', side: 'Side'):
        method = "Piece.__init__"

        id_validation = IdValidator.validate(piece_id)
        if not id_validation.is_success():
            raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

        name_validation = NameValidator.validate(name)
        if not name_validation.is_success():
            raise NameValidationException(
                f"{method}: {NameValidationException.DEFAULT_MESSAGE}"
            )

        # rank_validation = RankValidator.validate(rank)
        # if not rank_validation.is_success():
        #     raise RankValidationException(f"{method}: {RankValidationException.DEFAULT_MESSAGE}")

        team_validation = SideValidator.validate(side)
        if not team_validation.is_success():
            raise SideValidationException(
                f"{method}: {SideValidationException.DEFAULT_MESSAGE}"
            )
        side = cast(team_validation.payload, Side)

        self._id = cast(id_validation.payload, int)
        self._name = cast(name_validation.payload, str)
        # self._rank = cast(rank_validation.payload, Rank)

        if self not in side.pieces:
            side.pieces.append(self)
        self._side = side

        # self._status = MobilityStatus.FREE

        self._observations = EncounterLog()
        self._positions = CoordinateStack()
        self._current_position = self._positions.current_coordinate


    @property
    def id(self) -> int:
        return self._id


    @property
    def name(self) -> str:
        return self._name


    @property
    def side(self) -> 'Side':
        return self._side


    @property
    def rank(self) -> 'Rank':
        return self._rank


    # @property
    # def status(self) -> MobilityStatus:
    #     return self._status


    @property
    def positions(self) -> CoordinateStack:
        return self._positions


    @property
    def current_position(self) -> Optional[Coordinate]:
        return self._positions.current_coordinate


    @property
    def observations(self) -> EncounterLog:
        return self._observations


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Piece):
            return False
        return self._id == other.id


    def __hash__(self):
        return hash(self._id)


    def is_enemy(self, piece: 'Piece'):
        if piece is None:
            raise Exception("Cannot run is_enemy() state on a null captor.")
        return self._side != piece.side


    def add_observation(self, piece: 'Piece'):
        method = "Piece.add_observation"

        if piece is None:
            raise NullPieceException(f"{method}: {NullPieceException.DEFAULT_MESSAGE}")
        if piece is self:
            raise MappingSelfException(f"{method}: {MappingSelfException.DEFAULT_MESSAGE}")

        self._observations.add_encounter(Encounter(piece))


    def __str__(self):
        return (
            f"ChessPiece[id:{self._id} "
            f"name:{self._name} "
            f"total_positions:{self._positions.size()} "
            f"current_position: {self._positions.current_coordinate} "
            f"status:{self._status.name}"
        )



class CombatantPiece(Piece):
    _captor: Optional[Piece]

    def __init__(self, token_id: int, name: str, rank: 'Rank', side: 'Side'):
        super().__init__(token_id, name, rank, side)
        self._captor = None


    @property
    def captor(self) -> Optional[Piece]:
        return self._captor


    @captor.setter
    def captor(self, captor: Piece):
        method = "Captor.@setter.captor"

        if captor is None:
            raise NullCaptorException(f"{method}: {NullCaptorException.DEFAULT_MESSAGE}")

        if self._captor is not None:
            raise PrisonerReleaseException(f"{method}: {PrisonerReleaseException.DEFAULT_MESSAGE}")

        self._captor = captor


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, CombatantPiece):
            return self.id == other.id


