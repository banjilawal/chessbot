from chess.common.rank import Rank


class QueenRank(Rank):
    def __init__(self, movement_strategy: 'QueenMovement'):
        super().__init__(self, movement_strategy)