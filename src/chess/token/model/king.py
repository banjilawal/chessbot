from chess.rank.base import Rank
from chess.rank.king import KingRank
from chess.team.model import Team
from chess.token.model.base import Piece


class KingPiece(Piece):
    def __init__(self, token_id: int, name: str, team: Team, rank: Rank=KingRank()):
        super().__init__(token_id, name, rank, team)


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, KingPiece):
            return self.id == other.id