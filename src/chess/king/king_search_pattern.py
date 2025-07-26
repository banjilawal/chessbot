from chess.geometry.board import Board
from chess.common.piece import Piece
from chess.geometry.coordinate import Coordinate
from chess.motion.search_pattern import SearchPattern


class KingSearchPattern(SearchPattern):


    @staticmethod
    def search(piece: Piece, board: Board) -> list[Coordinate]:
        pass