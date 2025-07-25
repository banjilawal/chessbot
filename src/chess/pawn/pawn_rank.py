from chess.common.rank import Rank


class PawnRank(Rank):
    def __init__(self, movement_strategy: 'PawnMovement'):
        super().__init__(movement_strategy)