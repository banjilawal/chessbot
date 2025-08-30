from typing import Generic, TypeVar

from chess.board.square import Square
from chess.request.base import Request
from chess.token.model import Piece

T = TypeVar('T')


class AttackRequest(Request):

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
        if not super().__eq__(other):
            return False

        if isinstance(other, AttackRequest):
            return self._id == other.id