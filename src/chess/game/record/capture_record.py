import string

from chess.common.geometry import Coordinate
from chess.common.piece import Piece, CaptivityStatus
from podscape.constants import PodscapeColor


class CaptureRecord:
    _id: int
    _location_id: int
    _captor_name: string
    _captor_color: PodscapeColor
    _prisoner_name: string
    _prisoner_color: PodscapeColor

    def __init__(self, record_id:int, location: Coordinate, captor: Piece, prisoner: Piece):
        if location is None:
            raise ValueError("location cannot be null or empty.")
        if captor is None:
            raise ValueError("captor cannot be null or empty.")
        if prisoner is None:
            raise ValueError("prisoner cannot be null or empty.")
        if captor.status != CaptivityStatus.FREE:
            raise ValueError("captor must be free.")
        if prisoner.status != CaptivityStatus.PRISONER:
            raise ValueError("prisoner cannot be running free.")

        self._id = record_id
        self._location_id = location.id
        self._captor.name = captor.name
        self._captor_color = captor.team.color

        self._prisoner.name = prisoner.name
        self._prisoner_color = prisoner.team.color

    @property
    def id(self) -> int:
        return self._id

    @property
    def location_id(self) -> int:
        return self._location.id

    @property
    def captor_name(self) -> int:
        return self._captor_name

    @property
    def captor_color(self) -> PodscapeColor:
        return self._captor_color

    @property
    def prisoner_name(self) -> string:
        return self._prisoner_name

    @property
    def prisoner_color(self) -> PodscapeColor:
        return self._prisoner_color

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, CaptureRecord):
            return False
        if isinstance(other, CaptureRecord):
            return (
                    self.id == other.id and self.location.id == other.location.id and
                    self.captor.id == other.captor.id and self.prisoner.id == other.prisoner.id and
                    self.prisoner_color == other.prisoner_color
            )
        return False

    def __hash__(self):
        return hash((self.id, self.location.id, self.captor_id, self.prisoner_id))