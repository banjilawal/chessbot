from abc import ABC, abstractmethod
from typing import Optional

from chess.motion.movement.queen_movement import QueenMovement
from chess.piece.chess_piece import Piece
from chess.piece.rank import PawnRank, QueenRank


class RankPromotable(ABC):

    @abstractmethod
    def promote(self, new_rank: PawnRank) -> Optional[Piece]:
        pass

class PromotablePiece(Piece, RankPromotable):
    def __init__(self, chess_piece_id: int, name: str, team: 'Team', rank: 'Rank'):
        super().__init__(chess_piece_id, name, team, rank)

    def add_position(self, coordinate: Coordinate) -> None:
        super.add_position(coordinate)
        if coordinate.row == self.team.home.get_enemy_home().first_home_row():
            self.promote(self, QueenRank(QueenMovement))

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
            chess_piece_id=self.id,
            name=self.name,
            team=self.team,
            rank=QueenRank(QueenMovement())
        )


class Pawn(PromotablePiece):
    pass

class King(PromotablePiece):
    pass