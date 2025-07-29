from typing import TYPE_CHECKING, List

from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.geometry.quadrant import Quadrant
from chess.motion.search.search_pattern import SearchPattern
from chess.piece.piece import Piece
from chess.system_config import ROW_SIZE


class CastleSearchPattern(SearchPattern):
    def __init__(self):
        super().__init__()

    def _perform_search(self, piece: Piece, board: Board) -> List[Coordinate]:
        destinations: List[Coordinate] = []
        origin = piece.current_position()

        if origin is None:
            return destinations

        for quadrant in [Quadrant.N, Quadrant.E, Quadrant.S, Quadrant.W]:
            delta = quadrant.delta
            current = origin.shift(delta)

            while board.coordinate_is_valid(current):
                occupant = board.get_piece_by_coordinate(current)

                if occupant is None:
                    destinations.append(current)
                elif piece.is_enemy(occupant):
                    destinations.append(current)
                    break
                else:
                    break  # blocked by friendly piece

                next_row = current.row + delta.y
                next_col = current.column + delta.x

                if 0 <= next_row <= 7 and 0 <= next_col <= 7:
                    try:
                        current = Coordinate(next_row, next_col)
                    except ValueError:
                        break  # Just in case coordinate constructor has guards
                else:
                    break  # next move would go out of bounds

        return destinations


