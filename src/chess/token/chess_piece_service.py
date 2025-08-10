from typing import List, Optional

from chess.owner.model.owner import Owner
from chess.team.team import Team
from chess.token.chess_piece import ChessPiece
from chess.token.chess_piece_repo import ChessPieceRepo


class ChessPieceService:
    _repo: ChessPieceRepo

    def __init__(self, repo: ChessPieceRepo):
        self._repo = repo


    def size(self) -> int:
        return self._repo.__len__()


    def add_chess_piece(self, chess_piece: ChessPiece):
        self._repo.add(chess_piece)


    def find_chess_piece_by_id(self, chess_piece_id: int) -> Optional[ChessPiece]:
        return self._repo.find(chess_piece_id)


    def find_by_team(self, team: Team) -> List[ChessPiece]:
        return self._repo.filter_by_team(team)