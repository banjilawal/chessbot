
from typing import List
from chess.motion.search.search_pattern import SearchPattern
from chess.motion.search.queen_search_pattern import QueenSearchPattern
from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.piece.piece import ChessPiece


class KingSearchPattern(SearchPattern):

    def _perform_search(self, piece: ChessPiece, board: Board) -> List[Coordinate]:
        origin = piece.current_position()
        destinations: List[Coordinate] = []
        quadrants = piece.rank.territories
        print(f"{piece.label} at {origin} will search {len(quadrants)} quadrants for potential destinations")


        queen_destinations = QueenSearchPattern.search(piece, board)

        # Filter only coordinates that are one step away (Chebyshev distance == 1)
        destinations = [
            coordinate for coordinate in queen_destinations
            if max(abs(coordinate.row - origin.row), abs(coordinate.column - origin.column)) == 1
        ]

        return destinations
