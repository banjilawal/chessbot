from chess.rank.rank import Rank
from chess.rank.rank_config import RankConfig


class RankBuilder:

    @staticmethod
    def build(config: RankConfig):
        return Rank()