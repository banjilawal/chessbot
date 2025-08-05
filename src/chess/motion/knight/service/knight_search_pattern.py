from chess.geometry.board.board import ChessBoard
from chess.geometry.coordinate.coordinate import Coordinate
from chess.motion.abstract.search_pattern import SearchPattern
from chess.team.model.piece import ChessPiece
from chess.motion.knight.service.knight_reachable import KnightReachable
from typing import List


class KnightSearchPattern(SearchPattern):
    def __init__(self):
        super().__init__()

    def _perform_search(self, piece: ChessPiece, board: ChessBoard) -> List[Coordinate]:
        origin = piece.current_coordinate()
        destinations: List[Coordinate] = []
        quadrants = piece.motion_controller.territories
        print(f"{piece.label} at {origin} will search {len(quadrants)} quadrants for potential destinations")

        for quadrant in  quadrants:
            delta = quadrant.delta
            # Try both L-shaped offsets for this quadrant
            candidate_1 = origin.shift(delta.delta_column * 2, delta.delta_row)
            candidate_2 = origin.shift(delta.delta_column, delta.delta_row * 2)

            for candidate in [candidate_1, candidate_2]:
                if not board.coordinate_is_valid(candidate):
                    continue
                piece = board.find_chess_piece(origin)
                if not board.square_is_empty_or_contains_enemy(candidate, piece.player):
                    continue
                if KnightReachable.is_reachable(origin, candidate):
                    occupant = board.find_chess_piece(candidate)
                    if occupant is None:
                        destinations.append(candidate)
                    elif piece.is_enemy(occupant):
                        print(f"{piece.label} found enemy {occupant.label} at {candidate} adding the target")
                        destinations.append(candidate)
                        break
                    else:
                        print(f"{piece.label} cannot occupy {candidate} friendly {occupant.label} lives there")
                        break  # Blocked by friendly chess_piece
                    destinations.append(candidate)
        return destinations
