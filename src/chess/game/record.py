from dataclasses import dataclass

from chess.common.geometry import Coordinate
from chess.figure.chess_piece import ChessPiece, CaptivityStatus


class CaptureRecord:
    _id: int
    _location: Coordinate
    _captor: ChessPiece
    _prisoner: ChessPiece

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
        self._location = location
        self._captor = captor
        self._prisoner = prisoner

    @property
    def id(self) -> int:
        return self._id
    @property
    def location(self) -> Coordinate:
        return self._location
    @property
    def captor(self) -> ChessPiece:
        return self._captor
    @property
    def prisoner(self) -> ChessPiece:
        return self._prisoner

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, CaptureRecord):
            return False
        if isinstance(other, CaptureRecord):
            return (
                    self.id == other.id and self.location == other.location and
                    self.captor == other.captor and self.prisoner == other.prisoner
            )
        return False

    def __hash__(self):
        return hash((self.id, self.location))




