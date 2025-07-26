from abc import ABC, abstractmethod
from typing import Optional

from chess.queen.queen_search_pattern import QueenSearchPattern
from chess.common.piece import Piece
from chess.rank.rank import PawnRank, QueenRank, Rank


class RankPromotable(ABC):

    @abstractmethod
    def promote(self, new_rank: PawnRank) -> Optional[Piece]:
        pass

class PromotablePiece(Piece, RankPromotable):
    def __init__(self, piece_id: int, label: str, team: 'Team', rank: 'Rank'):
        super().__init__(piece_id, label, team, rank)

    def add_position(self, coordinate: Coordinate) -> None:
        super.add_position(coordinate)
        if coordinate.row == self.team.home.get_enemy_home().first_home_row():
            self.promote(self, QueenRank(QueenSearchPattern))

    def promote(self, new_rank: Rank) -> Optional[Piece]:
        if new_rank is None:
            print("new_rank cannot be null or empty.")
            return None
        if self.rank == QueenRank:
            print("Pawn is already promoted")
            return None
        if new_rank != QueenRank:
            print("New rank must be Queen")
            return None
        return PromotablePiece(
            piece_id=self.id,
            label=self.name,
            team=self.team,
            rank=QueenRank(QueenSearchPattern())
        )


class Pawn(PromotablePiece):
    pass

class King(PromotablePiece):
    pass