from typing import cast

from chess.rank.queen import Queen
from chess.request.base import Request
from chess.token.model import Piece


class PromotionRequest(Request):

    def __init__(self, req_id: int, piece: Piece, rank: Queen = Queen()):
        super().__init__(req_id=req_id, client=piece, resource=rank)


    @property
    def id(self):
        return self._id


    @property
    def piece(self) -> Piece:
        return cast(self._client, Piece)


    @property
    def rank(self) -> Queen:
        return cast(self._client, Queen)


    def __eq__(self, other):

        if not super().__eq__(other):
            return False

        if isinstance(other, PromotionRequest):
            return self._id == other.id