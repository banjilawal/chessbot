from abc import ABC, abstractmethod
from typing import Optional

from chess.piece.chess_piece import ChessPiece
from chess.piece.rank import PawnRank


class RankPromotable(ABC):

    @abstractmethod
    def promote(self, new_rank: PawnRank) -> Optional[ChessPiece]:
        pass