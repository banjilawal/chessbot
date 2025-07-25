from chess.rank.rank import Rank


class CastleRank(Rank):
    def __init__(self, movement_strategy: 'CastleSearchPattern'):
        super().__init__(self, movement_strategy)