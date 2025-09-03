from typing import cast

from chess.request.validators import PromotionRequestValidator
from chess.config.rank import RankProfile
from chess.flow.base import Flow
from chess.rank.queen import Queen, PromotedQueen
from chess.request.promote import PromotionRequest
from chess.token.model import Piece


class PromotionFlow(Flow):

    @staticmethod
    def enter(request: PromotionRequest):
        permission_result = PromotionRequestValidator.validate(request)
        if not permission_result.is_success():
            raise permission_result.exception

        client = cast(Piece, permission_result.request.client)
        rank = cast(Queen, permission_result.request.resource)


        promoted_queen = PromotedQueen(
            old_rank=client.rank.name,
            name=RankProfile.QUEEN.name,
            letter=RankProfile.QUEEN.letter,
            value=RankProfile.QUEEN.capture_value,
            per_team=1,
            territories=RankProfile.QUEEN.territories,
        )

        piece = Piece(piece_id=client.id, name=client.name, side=client.side, rank=promoted_queen)
