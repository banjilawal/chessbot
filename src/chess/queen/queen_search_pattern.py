from chess.geometry.board import Board
from chess.machine.search.search_pattern import SearchPattern


class QueenSearchPattern(SearchPattern):

    @staticmethod
    def search(piece: Queen, board: Board) -> list[Coordinate]:
        pass