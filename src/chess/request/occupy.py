from chess.board.square import Square
from chess.request.base import Request
from chess.token.model import Piece


class OccupationRequest(Request):

    def __init__(self, request_id: int, piece: Piece, square: Square):
        super().__init__(request_id=request_id, client=piece, resource=square)

    @property
    def id(self):
        return self._id

    @property
    def piece(self):
        return self._client

    @property
    def square(self):
        return self._resource

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, OccupationRequest):
            return False
        return self.id == other.id