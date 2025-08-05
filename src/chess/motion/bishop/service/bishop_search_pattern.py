
from typing import List

from chess.geometry.board.board import ChessBoard
from chess.geometry.coordinate.coordinate import Coordinate
from chess.motion.bishop.service.bishop_reachable import BishopReachable
from chess.motion.abstract.search_pattern import SearchPattern
from chess.team.model.piece import ChessPiece
from chess.system_config import ROW_SIZE, COLUMN_SIZE


class BishopSearchPattern(SearchPattern):
    def __init__(self):
        super().__init__()

    def _perform_search(self, piece: ChessPiece, board: ChessBoard) -> List[Coordinate]:
        origin = piece.current_coordinate()
        destinations: List[Coordinate] = []
        quadrants = piece.rank.territories
        print(f"{piece.label} at {origin} will search {len(quadrants)} quadrants for potential destinations")

        for quadrant in quadrants:
            delta = quadrant.delta
            current = origin.shift(delta)

            while board.coordinate_is_valid(current):
                if not BishopReachable.is_reachable(origin, current):
                    break

                occupant = board.find_chess_piece(current)
                if occupant is None:
                    destinations.append(current)
                elif piece.is_enemy(occupant):
                    print(f"{piece.label} found enemy {occupant.label} at {current} adding the target")
                    destinations.append(current)
                    break
                else:
                    print(f"{piece.label} cannot occupy {current} friendly {occupant.label} lives there")
                    break  # Blocked by friendly chess_piece

                next_row = current.row + delta.delta_row
                next_column = current.column + delta.delta_column

                if 0 <= next_row < ROW_SIZE and 0 <=  next_column < COLUMN_SIZE:
                    current = current.shift(delta)
                else:
                    break
                current = current.shift(delta)
        return destinations






