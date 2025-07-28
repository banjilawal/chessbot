
from typing import List
from chess.geometry.board import Board
from chess.geometry.coordinate import Coordinate
from chess.geometry.quadrant import Quadrant
from chess.motion.logic.bishop_reachable import BishopReachable
from chess.motion.search.search_pattern import SearchPattern
from chess.piece.piece import Piece


class BishopSearchPattern(SearchPattern):
    def __init__(self):
        super().__init__([])
    @staticmethod
    def search(piece: Piece, board: Board) -> List[Coordinate]:
        if not SearchPattern.check_basic_conditions(piece, board):
            return []

        origin = piece.current_position()
        territories: List[Quadrant] = piece.rank.territories
        destinations: List[Coordinate] = []

        for quadrant in territories:
            delta = quadrant.delta
            current = origin.shift(delta)

            while board.coordinate_is_valid(current):
                if not BishopReachable.is_reachable(origin, current):
                    break

                occupant = board.get_piece_by_coordinate(current)

                if occupant is None:
                    destinations.append(current)
                elif piece.is_enemy(occupant):
                    destinations.append(current)
                    break
                else:
                    break  # Blocked by friendly piece

                current = current.shift(delta)

        return destinations






