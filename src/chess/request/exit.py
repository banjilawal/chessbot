from chess.request.base import Request
from chess.token.model import Piece


class ExitRequest(Request):

    def __init__(self, request_id: int, piece: Piece):
        super().__init__(request_id=request_id, client=None)


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
        if not super().__eq__(other):
            return False

        if isinstance(other, ExitRequest):
            return self._id == other.id