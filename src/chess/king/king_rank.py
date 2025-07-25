from chess.common.rank import Rank


class KingRank(Rank):
    def __init__(self, movement_strategy: 'KingMovement'):
        super().__init__(movement_strategy)