from chess.rank.rank import Rank


class PawnRank(Rank):
    def __init__(self, movement_strategy: 'PawnSearchPattern'):
        super().__init__(movement_strategy)