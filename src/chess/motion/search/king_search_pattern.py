
from typing import List
from chess.motion.search.search_pattern import SearchPattern
from chess.motion.search.queen_search_pattern import QueenSearchPattern
from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.piece.piece import Piece


class KingSearchPattern(SearchPattern):

    @staticmethod
    def search(piece: Piece, board: Board) -> List[Coordinate]:
        if not SearchPattern.validate_search_parameters(piece, board):
            return []

        origin = piece.current_position()
        all_queen_moves = QueenSearchPattern.search(piece, board)

        # Filter only coordinates that are one step away (Chebyshev distance == 1)
        king_moves = [
            coord for coord in all_queen_moves
            if max(abs(coord.row - origin.row), abs(coord.column - origin.column)) == 1
        ]

        return king_moves
