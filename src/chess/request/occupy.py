from typing import cast

from chess.board.square import Square
from chess.request.base import Request
from chess.token.model.base import Piece


class OccupationRequest(Request):

    def __init__(self, request_id: int, piece: Piece, square: Square):
        super().__init__(request_id=request_id, client=piece, resource=Square)


    @property
    def id(self):
        return self._id


    @property
    def piece(self):
        return cast(self._client, Piece)


    @property
    def square(self):
        return cast(self._resource, Square)


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, OccupationRequest):
            return self._id == other.id