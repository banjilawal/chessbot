from abc import ABC
from typing import TYPE_CHECKING, Optional, cast

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.name import NameValidationException
from assurance.exception.validation.rank.rank_validation_exception import RankValidationException
from assurance.exception.validation.team import TeamValidationException
from assurance.validators.id import IdValidator
from assurance.validators.name import NameValidator
from assurance.validators.rank import RankValidator
from assurance.validators.team import TeamValidator
from chess.exception.null.piece import NullPieceException
from chess.exception.piece import MappingSelfException
from chess.geometry.coord import Coordinate
from chess.team.model import Team
from chess.token.model.map import Record, ObservationChart
from chess.token.model.mobility_status import MobilityStatus
from chess.token.model.coord import CoordinateStack

if TYPE_CHECKING:
    from chess.rank.base import Rank
    # from chess.geometry.coordinate.coordinate_stack import CoordinateStack

    """"
    
    """


class Piece(ABC):
    _id: int
    _name: str
    _team: 'Team'
    _rank: 'Rank'
    _captor: 'Piece'
    _current_position: Coordinate
    _status: MobilityStatus
    _observations: ObservationChart
    _positions: CoordinateStack


    def __init__(self, piece_id: int, name: str, rank: 'Rank', team: 'Team'):
        method = "Piece.__init__"

        id_validation = IdValidator.validate(piece_id)
        if not id_validation.is_success():
            raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

        name_validation = NameValidator.validate(name)
        if not name_validation.is_success():
            raise NameValidationException(
                f"{method}: {NameValidationException.DEFAULT_MESSAGE}"
            )

        rank_validation = RankValidator.validate(rank)
        if not rank_validation.is_success():
            raise RankValidationException(f"{method}: {RankValidationException.DEFAULT_MESSAGE}")

        team_validation = TeamValidator.validate(team)
        if not team_validation.is_success():
            raise TeamValidationException(
                f"{method}: {TeamValidationException.DEFAULT_MESSAGE}"
            )
        team = cast(team_validation.payload, Team)

        self._id = cast(id_validation.payload, int)
        self._name = cast(name_validation.payload, str)
        self._rank = cast(rank_validation.payload, Rank)

        if self not in team.pieces:
            team.pieces.append(self)
        self._team = team

        self._status = MobilityStatus.FREE

        self._observations = ObservationChart()
        self._positions = CoordinateStack()
        self._current_position = self._positions.current_coordinate


    @property
    def id(self) -> int:
        return self._id


    @property
    def name(self) -> str:
        return self._name


    @property
    def team(self) -> 'Team':
        return self._team


    @property
    def rank(self) -> 'Rank':
        return self._rank


    @property
    def status(self) -> MobilityStatus:
        return self._status


    @property
    def positions(self) -> CoordinateStack:
        return self._positions


    @property
    def current_position(self) -> Optional[Coordinate]:
        return self._positions.current_coordinate


    @property
    def observations(self) -> ObservationChart:
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
        return self._team != piece.team


    def add_observation(self, piece: 'Piece'):
        method = "Piece.add_observation"

        if piece is None:
            raise NullPieceException(f"{method}: {NullPieceException.DEFAULT_MESSAGE}")
        if piece is self:
            raise MappingSelfException(f"{method}: {MappingSelfException.DEFAULT_MESSAGE}")

        self._observations.add_record(Record(piece))


    def __str__(self):
        return (
            f"ChessPiece[id:{self._id} "
            f"name:{self._name} "
            f"total_positions:{self._positions.size()} "
            f"current_position: {self._positions.current_coordinate} "
            f"status:{self._status.name}"
        )





