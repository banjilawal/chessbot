from typing import cast

from chess.config.rank import RankProfile
from chess.flow.base import Flow
from chess.rank.queen_rank import Queen, PromotedQueen

from chess.system.validators.promote import PromotionRequestValidator
from chess.piece.piece import Piece


class PromotionFlow(Flow):

    @staticmethod
    def enter(request: PromotionRequest, boar=None):
        permission_result = PromotionRequestValidator.validate(request)
        if not permission_result.is_success():
            raise permission_result.exception

        client = cast(Piece, permission_result.request.client)
        rank = cast(Queen, permission_result.request.resource)


        promoted_queen = PromotedQueen(
            old_rank=client.rank.name,
            name=RankProfile.QUEEN.name,
            letter=RankProfile.QUEEN.letter,
            value=RankProfile.QUEEN.value,
            per_side=RankProfile.QUEEN.per_side,
            quadrants=RankProfile.QUEEN.quadrants,
        )

        piece = Piece(piece_id=client.id, name=client.name, side=client.side, rank=promoted_queen)
