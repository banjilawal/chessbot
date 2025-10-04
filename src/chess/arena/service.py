from typing import Optional, List

from chess.arena.arena import Arena
from chess.arena.repo import ArenaRepo
from chess.board.board import Board
from chess.competitor.commander import Commander


class ArenaService:
    _repo: ArenaRepo

    def __init__(self, repo: ArenaRepo):
        self._repo = repo


    def size(self) -> int:
        return self._repo.__len__()


    def find_arena_by_id(self, arena_id: int) -> Optional[Arena]:
        return self._repo.arena_by_id(arena_id)


    def filter_arenas_by_team_owner(self, owner: Commander) -> List[Arena]:
        return self._repo.arenas_by_team_owner(owner)


    def filter_arenas_by_chess_board(self, chess_board: Board) -> List[Arena]:
        return self._repo.arenas_by_chess_board()

