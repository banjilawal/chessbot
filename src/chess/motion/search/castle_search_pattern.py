from typing import TYPE_CHECKING, List

from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.geometry.quadrant import Quadrant
from chess.motion.search.search_pattern import SearchPattern
from chess.piece.piece import Piece


class CastleSearchPattern(SearchPattern):
    def __init__(self):
        super().__init__()

    def _perform_search(self, piece: Piece, board: Board) -> List[Coordinate]:
        destinations = []
        origin = piece.current_position()

        for quadrant in [Quadrant.N, Quadrant.E, Quadrant.S, Quadrant.W]:
            delta = quadrant.delta
            next_coord = origin

            while True:
                try:
                    next_coord = next_coord.shift(delta)
                except ValueError:
                    # Went off the board — stop searching in this direction
                    break

                occupant = board.get_piece_by_coordinate(next_coord)

                if occupant is None:
                    destinations.append(next_coord)
                elif piece.is_enemy(occupant):
                    destinations.append(next_coord)
                    break
                else:
                    # Blocked by friendly piece
                    break

        return destinations



