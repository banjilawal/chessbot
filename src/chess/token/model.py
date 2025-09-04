from abc import ABC
from typing import TYPE_CHECKING, Optional, cast

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.name import NameValidationException

from assurance.exception.validation.team import SideValidationException
from assurance.validators.id import IdValidator
from assurance.validators.name import NameValidator

from assurance.validators.side import SideValidator
from chess.creator.builder.side import SideBuilder
from chess.creator.emit import id_emitter
from chess.exception.null.piece import NullPieceException
from chess.exception.piece import MappingSelfException, PrisonerReleaseException, NullCaptorException
from chess.geometry.coord import Coord

from chess.side.model import Side
from chess.token.coord import CoordStack
from chess.token.encounter import Encounter, EncounterLog


if TYPE_CHECKING:
    from chess.rank.base import Rank
    # from assurance.validators.rank import RankValidator

    """"
    
    """


class Piece(ABC):
    _id: int
    _name: str
    _side: 'Side'
    _rank: 'Rank'
    _captor: 'Piece'
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


        self._side = side

        # self._status = MobilityStatus.FREE

        self._encounters = EncounterLog()
        self._positions = CoordStack()
        self._current_position = self._positions.current_coord

        if self not in side.pieces:
            side.pieces.append(self)

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


    def is_enemy(self, piece: 'Piece'):
        if piece is None:
            raise Exception("Cannot run is_enemy() state on a null captor.")
        return self._side != piece.side


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


class KingPiece(Piece):

    def __init__(self, piece_id: int, name: str, rank: 'Rank', side: 'Side'):
        super().__init__(piece_id, name, rank, side)


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, KingPiece):
            return self.id == other.id



class CombatantPiece(Piece):
    _captor: Optional[Piece]

    def __init__(self, piece_id: int, name: str, rank: 'Rank', side: 'Side'):
        super().__init__(piece_id, name, rank, side)
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



def main():
    from chess.rank.pawn import Pawn
    piece = CombatantPiece(piece_id=id_emitter.piece_id, name="BB-1", side=SideBuilder.build().payload, rank=Pawn())
    print(piece)


if __name__ == "__main__":
    main()


