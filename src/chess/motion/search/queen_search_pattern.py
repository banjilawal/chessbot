from typing import List

from chess.geometry.board import Board
from chess.geometry.coordinate import Coordinate
from chess.motion.search.bishop_search_pattern import BishopSearchPattern
from chess.motion.search.castle_search_pattern import CastleSearchPattern
from chess.motion.search.search_pattern import SearchPattern
from chess.piece.piece import Piece


class QueenSearchPattern(SearchPattern):

    @staticmethod
    def search(piece: Piece, board: Board) -> List[Coordinate]:
        if not SearchPattern.check_basic_conditions(piece, board):
            return []

        bishop_destinations = BishopSearchPattern.search(piece, board)
        castle_destinations = CastleSearchPattern.search(piece.rank, piece.current_position(), board)

        return bishop_destinations + castle_destinations
