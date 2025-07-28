
from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.motion.search.search_pattern import SearchPattern
from chess.rank.knight import Knight
from chess.motion.logic.knight_reachable import KnightReachable
from typing import List


class KnightSearchPattern(SearchPattern):

    @staticmethod
    def search(rank: 'Knight', origin: Coordinate, board: Board) -> List[Coordinate]:
        if origin is None or board is None:
            return []

        destinations: List[Coordinate] = []

        for quadrant in rank.territories:
            delta = quadrant.delta
            # Try both L-shaped offsets for this quadrant
            candidate_1 = origin.shift(delta.x * 2, delta.y)
            candidate_2 = origin.shift(delta.x, delta.y * 2)

            for candidate in [candidate_1, candidate_2]:
                if not board.coordinate_is_valid(candidate):
                    continue
                piece = board.get_chess_piece_by_coordinate(origin)
                if not board.square_is_empty_or_contains_enemy(candidate, piece.player):
                    continue
                if KnightReachable.is_reachable(origin, candidate):
                    destinations.append(candidate)

        return destinations
