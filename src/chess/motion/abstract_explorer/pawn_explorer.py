#
# from typing import List
#
# from chess.geometry.obsolete_board.obsolete_board import ObsoleteChessBoard
# from chess.geometry.coordinate.coordinate import Coordinate
# from chess.geometry.quadrant import Quadrant
# from chess.motion.rank.promotable.pawn_motion_controller import PawnRank
# from chess.motion.walk.pawn_walk import PawnWalk
#
#
# class PawnMoveGenerator(MoveGenerator):
#
#     def _perform_search(self, pawn: PawnRank, obsolete_board: ObsoleteChessBoard) -> List[Coordinate]:
#         origin = pawn.current_position()
#         destinations: List[Coordinate] = []
#         quadrants = pawn.motion.territories
#         print(f"{pawn.label} at {origin} will search {len(quadrants)} quadrants for potential destinations")
#
#         destinations = []
#         origin = pawn.current_position()
#         if origin is None or not MoveGenerator.validate_search_parameters(pawn, obsolete_board):
#             return destinations
#
#
#         for quadrant in quadrants:
#             candidate = origin.shift(quadrant.delta)
#             if not obsolete_board.coordinate_is_valid(candidate):
#                 continue
#
#             # Use PawnWalk to decide if move is valid
#             if quadrant == Quadrant.N:
#                 # For forward moves, make sure element is empty and chess_piece can advance
#                 if (not obsolete_board.coordinate_is_occupied(candidate) and
#                     PawnWalk.can_advance(pawn, candidate)):
#                     destinations.append(candidate)
#
#                     # Check two-step forward only if first step is valid and no pieces blocking
#                     if len(pawn.position_history) == 1:
#                         two_step = candidate.shift(quadrant.delta)
#                         if (obsolete_board.coordinate_is_valid(two_step) and
#                             not obsolete_board.coordinate_is_occupied(two_step) and
#                             PawnWalk.can_advance(pawn, two_step)):
#                             destinations.append(two_step)
#
#             else:
#                 # For diagonal quadrants, only add if there's an enemy chess_piece and chess_piece can attack
#                 if (obsolete_board.coordinate_is_occupied(candidate) and
#                     PawnWalk.can_attack(pawn, candidate, obsolete_board)):
#                     destinations.append(candidate)
#
#         return destinations
#
