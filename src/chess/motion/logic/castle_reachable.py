from typing import TYPE_CHECKING, List

from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.geometry.quadrant import Quadrant
from chess.motion.search.search_pattern import SearchPattern
from chess.piece.piece import Piece
from chess.system_config import ROW_SIZE


class CastleReachable(SearchPattern):
    def __init__(self):
        super().__init__()

    def _perform_search(self, piece: Piece, board: Board) -> List[Coordinate]:
        destinations = []
        origin = piece.current_position()
        for quadrant in [Quadrant.N, Quadrant.E, Quadrant.S, Quadrant.W]:
            x_delta = quadrant.x_delta
            y_delta = quadrant.y_delta
            next_coord = origin.shift(x_delta, y_delta)

            while next_coord.column < ROW_SIZE and next_coord.row < ROW_SIZE:

                occupant = board.get_piece_by_coordinate(next_coord)
                if occupant is not None:
                    if not piece.is_enemy(occupant):
                        break
                    else:
                        destinations.append(next_coord)
                        break
                else:
                    destinations.append(next_coord)
                next_coord = next_coord.shift(x_delta, y_delta)

        return destinations
