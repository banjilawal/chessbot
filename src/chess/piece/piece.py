from abc import ABC
from typing import TYPE_CHECKING, Optional, cast

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.name import NameValidationException

from assurance.exception.validation.team import SideValidationException
from assurance.validators.id import IdValidator
from assurance.validators.name import NameValidator

from assurance.validators.side import SideValidator
from chess.piece.exception.null.null_piece import NullPieceException
from chess.geometry.coord import Coord

from chess.side.team import Side
from chess.piece.coord_stack import CoordStack
from chess.piece.encounter import Encounter, EncounterLog


if TYPE_CHECKING:
    from chess.rank.rank import Rank
    # from assurance.validators.rank import RankValidator



class Piece(ABC):
    _id: int
    _name: str
    _side: 'Side'
    _rank: 'Rank'
    _captor: 'Piece'
    _jersey: int
    _current_position: Coord
    # _status: MobilityStatus
    _encounters: EncounterLog
    _positions: CoordStack


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

        side_validation = SideValidator.validate(side)
        if not side_validation.is_success():
            raise SideValidationException(f"{method}: {SideValidationException.DEFAULT_MESSAGE}")

        side = cast(Side, side_validation.payload)

        self._id = cast(int, id_validation.payload)
        self._name = cast(str, name_validation.payload)
        self._rank = rank #cast(rank_validation.payload, Rank)

        self._jersey = len(side.roster)
        self._side = side

        # self._status = MobilityStatus.FREE

        self._encounters = EncounterLog()
        self._positions = CoordStack()
        self._current_position = self._positions.current_coord

        if self not in side.roster:
            side.add_to_roster(self)

    @property
    def id(self) -> int:
        return self._id


    @property
    def name(self) -> str:
        return self._name


    @property
    def jersey(self) -> int:
        return self._jersey


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
    def positions(self) -> CoordStack:
        return self._positions


    @property
    def current_position(self) -> Optional[Coord]:
        return self._positions.current_coord


    @property
    def encounters(self) -> EncounterLog:
        return self._encounters


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


    def is_enemy(self, piece: 'Piece') -> bool:
        method = f"{self.__class__.__name__}.is_enemy"
        try:
            if piece is None:
                raise NullPieceException(f"{method}: {NullPieceException.DEFAULT_MESSAGE}")

            return self._side != piece.side
        except NullPieceException as e:
            raise e



    def record_encounter(self, piece: 'Piece'):
        method = "Piece.add_observation"

        if piece is None:
            raise NullPieceException(f"{method}: {NullPieceException.DEFAULT_MESSAGE}")
        if piece is self:
            raise MappingSelfException(f"{method}: {MappingSelfException.DEFAULT_MESSAGE}")

        self._encounters.add_encounter(Encounter(piece))


    def __str__(self):
        return (
            f"Piece[id:{self._id} "
            f"name:{self._name} "
            f"rank:{self._rank.name} "
            f"side:{self._side.profile.name} "
            f"position:{self._positions.current_coord} "
            f"moves:{self._positions.size()}]"
        )


