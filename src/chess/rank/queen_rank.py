from chess.rank.rank import Rank


class QueenRank(Rank):
    def __init__(self, movement_strategy: 'QueenSearchPattern'):
        super().__init__(self, movement_strategy)