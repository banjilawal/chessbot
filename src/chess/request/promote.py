from typing import cast

from chess.rank.queen import QueenRank
from chess.request.base import Request
from chess.token.model.base import Piece


class PromotionRequest(Request):

    def __init__(self, request_id: int, piece: Piece, rank: QueenRank = QueenRank()):
        super().__init__(request_id=request_id, client=piece, resource=rank)


    @property
    def id(self):
        return self._id


    @property
    def piece(self) -> Piece:
        return cast(self._client, Piece)


    @property
    def rank(self) -> QueenRank:
        return cast(self._client, QueenRank)


    def __eq__(self, other):

        if not super().__eq__(other):
            return False

        if isinstance(other, PromotionRequest):
            return self._id == other.id