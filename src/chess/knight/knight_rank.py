from chess.common.rank import Rank


class KnightRank(Rank):
    def __init__(self, movement_strategy: 'KnightMovement'):
        super().__init__(movement_strategy)