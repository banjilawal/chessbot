from typing import Optional

from chess.common.geometry import Coordinate
from chess.common.piece import Piece
from chess.game.record.capture_record import CaptureRecord
from chess.game.record.promotion_record import PromotionRecord
from podscape.constants import PodscapeColor


class TurnRecord:
    _id: int
    _moved_piece_id: int
    _mover_color: PodscapeColor
    _departure_coordinate: Coordinate
    _arrival_coordinate: Coordinate
    _capture_record: Optional[CaptureRecord]
    _promotion_record: Optional[PromotionRecord]

    def __init__(
            self,
            record_id: int,
            moved_piece: Piece,
            departure_coordinate: Coordinate,
            arrival_coordinate: Coordinate,
            capture_record: CaptureRecord=None,
            promotion_record: PromotionRecord=None
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
        if capture_record is not None and capture_record.captor_id != moved_piece.id:
            print("mismatch between mover and captor id.")
            return

        self._id = record_id
        self._moved_piece_id = moved_piece.id
        self._mover_color = moved_piece.team.color
        self._departure_coordinate = departure_coordinate
        self._arrival_coordinate = arrival_coordinate
        self._capture_record = capture_record

        if capture_record is not None:
            self._capture_record = capture_record

        if promotion_record is not None:
            self.promotion_record = promotion_record

    @property
    def id(self) -> int:
        return self._id

    @property
    def moved_piece_id(self) -> int:
        return self._moved_piece_id

    @property
    def mover_color(self) -> PodscapeColor:
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

    def __eq__(self, obj):
        if self is obj:
            return True
        if obj is None:
            return False
        if not isinstance(obj, TurnRecord):
            return False
        return (
                self.id == obj.id and self.moved_piece_id == obj.moved_piece_id and
                self.mover_color == obj.mover_color and self.departure_coordinate == obj.departure_coordinate and
                self.arrival_coordinate == obj.arrival_coordinate and self.capture_record == obj.capture_record
        )









