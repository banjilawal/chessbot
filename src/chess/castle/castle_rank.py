from chess.common.rank import Rank


class CastleRank(Rank):
    def __init__(self, movement_strategy: 'CastleMovement'):
        super().__init__(self, movement_strategy)