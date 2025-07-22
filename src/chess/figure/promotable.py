from abc import ABC, abstractmethod

from chess.figure.figure_rank import PawnRank


class RankPromotable(ABC):

    @abstractmethod
    def promote(self, new_rank: PawnRank):
        pass