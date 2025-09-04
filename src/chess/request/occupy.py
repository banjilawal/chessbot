from typing import cast

from chess.board.square import Square
from chess.request.base import Request
from chess.token.model import Piece


class OccupationRequest(Request):

    def __init__(self, req_id: int, piece: Piece, square: Square):
        super().__init__(req_id=req_id, client=piece, resource=square)


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