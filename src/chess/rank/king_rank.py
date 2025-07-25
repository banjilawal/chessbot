from chess.rank.rank import Rank


class KingRank(Rank):
    def __init__(self, movement_strategy: 'KingSearchPattern'):
        super().__init__(movement_strategy)