from abc import ABC
from typing import List, TYPE_CHECKING, Optional

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.name import NameValidationException
from assurance.exception.validation.rank.rank_validation_exception import RankValidationException
from assurance.exception.validation.team import TeamValidationException
from assurance.validators.id import IdValidator
from assurance.validators.name import NameValidator
from assurance.validators.rank import RankValidator
from assurance.validators.team import TeamValidator
from chess.geometry.coordinate.coord import Coordinate
from chess.team.model import Team
from chess.token.model.obstruction import Obstruction
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
    _obstructions: List[Obstruction]
    _positions: CoordinateStack


    def __init__(self, piece_id: int, name: str, rank: 'Rank', team: 'Team'):
        method = "Piece.__init__"

        id_result = IdValidator.validate(piece_id)
        if not id_result.is_success():
            raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

        name_result = NameValidator.validate(name)
        if not name_result.is_success():
            raise NameValidationException(
                f"{method}: {NameValidationException.DEFAULT_MESSAGE}"
            )

        rank_result = RankValidator.validate(rank)
        if not rank_result.is_success():
            raise RankValidationException(f"{method}: {RankValidationException.DEFAULT_MESSAGE}")

        team_result = TeamValidator.validate(team)
        if not team_result.is_success():
            raise TeamValidationException(
                f"{method}: {TeamValidationException.DEFAULT_MESSAGE}"
            )

        self._id = id_result.payload
        self._name = name_result.payload
        self._rank = rank_result.payload
        self._team = team_result.payload

        self._obstructions = []
        self._status = MobilityStatus.FREE

        self._positions = CoordinateStack()
        team_result.payload.pieces.append(self)

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
    def obstructions(self) -> List[Obstruction]:
        return self._obstructions


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


    def add_obstruction(self, obstructor: 'Piece'):
        if obstructor is None:
            raise Exception("Cannot add null obstruction.")
        if obstructor.status != MobilityStatus.PRISONER:
            raise Exception("A prisoner is not on the chessboard it cannot be blocking")
        if obstructor is self:
            raise Exception("Cannot block self.")

        if obstructor not in self._obstructions:
            self._obstructions.append(Obstruction(obstructor))
        print("Obstruction added")


    def reset_obstruction_list(self):
        self._obstructions.clear()


    def __str__(self):
        return (
            f"ChessPiece[id:{self._id} "
            f"name:{self._name} "
            f"total_positions:{self._positions.size()} "
            f"current_position: {self._positions.current_coordinate} "
            f"status:{self._status.name}"
        )


