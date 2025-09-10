from typing import List, Optional

from chess.arena.model import Arena
from chess.board.board import Board
from chess.competitor.commander import Commander


class ArenaRepo:
    _arenas: List[Arena]

    def __init__(self):
        self._arenas = []


    def __len__(self):
        return len(self._arenas)


    def add_arena(self, arena: Arena):
        if arena not in self._arenas:
            self._arenas.append(arena)


    def arena_by_id(self, arena_id: int) -> Optional[Arena]:
        for arena in self._arenas:
            if arena.id == arena_id:
                return arena
        return None


    def arenas_by_team_owner(self, owner: Commander) -> List[Arena]:
        matches: List[Arena] = []

        for arena in self._arenas:
            if arena.white_owner == owner or arena.black_owner == owner and arena not in matches:
                matches.append(arena)
        return matches


    def arenas_by_chess_board(self, chess_board: Board) -> List[Arena]:
        matches: List[Arena] = []

        for arena in self._arenas:
            if arena.chess_board == chess_board and arena not in matches:
                matches.append(arena)
        return matches


