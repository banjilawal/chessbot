
from typing import List
from chess.geometry.board.coordinate import Coordinate
from chess.geometry.board import ChessBoard
from chess.geometry.quadrant import Quadrant
from chess.motion.search.search_pattern import SearchPattern
from chess.rank.pawn import Pawn
from chess.motion.logic.pawn_reachable import PawnReachable


class PawnSearchPattern(SearchPattern):

    def _perform_search(self, pawn: Pawn, board: ChessBoard) -> List[Coordinate]:
        origin = pawn.current_position()
        destinations: List[Coordinate] = []
        quadrants = pawn.rank.territories
        print(f"{pawn.label} at {origin} will search {len(quadrants)} quadrants for potential destinations")

        destinations = []
        origin = pawn.current_position()
        if origin is None or not SearchPattern.validate_search_parameters(pawn, board):
            return destinations


        for quadrant in quadrants:
            candidate = origin.shift(quadrant.delta)
            if not board.coordinate_is_valid(candidate):
                continue

            # Use PawnReachable to decide if move is valid
            if quadrant == Quadrant.N:
                # For forward moves, make sure model is empty and pawn can advance
                if (not board.coordinate_is_occupied(candidate) and
                    PawnReachable.can_advance(pawn, candidate)):
                    destinations.append(candidate)

                    # Check two-step forward only if first step is valid and no pieces blocking
                    if len(pawn.position_history) == 1:
                        two_step = candidate.shift(quadrant.delta)
                        if (board.coordinate_is_valid(two_step) and
                            not board.coordinate_is_occupied(two_step) and
                            PawnReachable.can_advance(pawn, two_step)):
                            destinations.append(two_step)

            else:
                # For diagonal quadrants, only add if there's an enemy chess_piece and pawn can attack
                if (board.coordinate_is_occupied(candidate) and
                    PawnReachable.can_attack(pawn, candidate, board)):
                    destinations.append(candidate)

        return destinations

