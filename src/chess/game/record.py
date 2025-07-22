from dataclasses import dataclass
from typing import Optional

from chess.common.geometry import Coordinate
from chess.figure.chess_piece import ChessPiece, CaptivityStatus
from podscape.constants import GameColor


class CaptureRecord:
    _id: int
    _location_id: int
    _captor_color: GameColor
    _captor_id: int
    _prisoner_id: int
    _prisoner_color: GameColor

    def __init__(self, record_id:int, location: Coordinate, captor: ChessPiece, prisoner: ChessPiece):
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
        self._captor_color = captor.team.color

        self._prisoner.id = prisoner.id
        self._prisoner_color = prisoner.team.color

    @property
    def id(self) -> int:
        return self._id
    @property
    def location_id(self) -> int:
        return self._location.id
    @property
    def captor_id(self) -> int:
        return self._captor_id
    @property
    def captor_color(self) -> GameColor:
        return self._captor_color
    @property
    def prisoner_id(self) -> int:
        return self._prisoner_id
    @property
    def prisoner_color(self) -> GameColor:
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


class TurnRecord:
    _id: int
    _moved_piece_id: int
    _mover_color: GameColor
    _departure_coordinate: Coordinate
    _arrival_coordinate: Coordinate
    _capture_record: Optional[CaptureRecord]

    def __init__(
            self,
            record_id: int,
            moved_piece: ChessPiece,
            departure_coordinate: Coordinate,
            arrival_coordinate: Coordinate,
            capture_record: CaptureRecord=None
     ):
        if moved_piece is None:
            print("moved_piece cannot be null or empty.")
            return
        if departure_coordinate is None:
            print("departure_coordinate cannot be null or empty.")
            return
        if arrival_coordinate is None:
            print("arrival_coordinate cannot be null or empty.")
            return
        if capture_record is not None and capture_record._captor_id != moved_piece.id:
            print("mismatch between mover and captor id.")
            return

        self._id = record_id
        self._moved_piece_id = moved_piece.piece_id
        self._mover_color = moved_piece.team.color
        self._departure_coordinate = departure_coordinate
        self._arrival_coordinate = arrival_coordinate
        self._capture_record = capture_record

    @property
    def id(self) -> int:
        return self._id
    @property
    def moved_piece_id(self) -> int:
        return self._moved_piece_id
    @property
    def mover_color(self) -> GameColor:
        return self._mover_color
    @property
    def departure_coordinate(self) -> Coordinate:
        return self._departure_coordinate
    @property
    def arrival_coordinate(self) -> Coordinate:
        return self._arrival_coordinate
    @property
    def capture_record(self) -> Optional[CaptureRecord]:
        return self._capture_record







