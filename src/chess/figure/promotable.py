from abc import ABC, abstractmethod
from typing import Optional

from chess.figure.chess_piece import ChessPiece
from chess.figure.rank import PawnRank


class RankPromotable(ABC):

    @abstractmethod
    def promote(self, new_rank: PawnRank) -> Optional[ChessPiece]:
        pass