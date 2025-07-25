from chess.rank.rank import Rank


class KnightRank(Rank):
    def __init__(self, movement_strategy: 'KightSearchPattern'):
        super().__init__(movement_strategy)