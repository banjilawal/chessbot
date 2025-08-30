from abc import ABC
from typing import cast

from assurance.validators.request.promote import PromotionRequestValidator
from chess.config.rank import RankConfig
from chess.flow.base import Flow
from chess.rank.queen import QueenRank, PromotedQueen
from chess.request.promote import PromotionRequest
from chess.token.model import Piece
from chess.walk.queen import QueenWalk


class PromotionFlow(Flow, ABC):

    @staticmethod
    def enter_flow(request: PromotionRequest):
        permission_result = PromotionRequestValidator.validate(request)
        if not permission_result.is_success():
            raise permission_result.exception

        client = cast(permission_result.request.client, Piece)
        rank = cast(permission_result.request.resource, QueenRank)

        promoted_queen = PromotedQueen(
            old_rank=client.rank,
            name=RankConfig.QUEEN.name,
            letter=RankConfig.QUEEN.letter,
            capture_value=RankConfig.QUEEN.capture_value,
            number_per_team=1,
            territories=RankConfig.QUEEN.territories,
            walk=QueenWalk(),
        )

        piece = Piece(piece_id=client.id, name=client.name, team=client.team, rank=promoted_queen)
