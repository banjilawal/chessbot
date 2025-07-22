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

