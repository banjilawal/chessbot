from chess.common.rank import Rank


class BishopRank(Rank):
    def __init__(self, movement_strategy: 'BishopMovement'):
        super().__init__(movement_strategy)