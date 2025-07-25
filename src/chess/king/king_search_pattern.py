from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.common.piece import Piece
from chess.motion.search_pattern import SearchPattern


class KingSearchPattern(SearchPattern):


    @staticmethod
    def search(piece: Piece, board: Board) -> list[Coordinate]:
        pass