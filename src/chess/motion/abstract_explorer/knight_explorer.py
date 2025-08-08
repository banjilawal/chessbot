# from chess.geometry.obsolete_board.obsolete_board import ObsoleteChessBoard
# from chess.geometry.coordinate.coordinate import Coordinate
#
# from chess.team.element.chess_piece import ChessPiece
# from chess.motion.walk.knight_walk import KnightWalk
# from typing import List
#
#
# class KnightMoveGenerator(MoveGenerator):
#     def __init__(self):
#         super().__init__()
#
#     def _perform_search(self, chess_piece: ChessPiece, obsolete_board: ObsoleteChessBoard) -> List[Coordinate]:
#         origin = chess_piece.current_coordinate()
#         destinations: List[Coordinate] = []
#         quadrants = chess_piece.rank.territories
#         print(f"{chess_piece.label} at {origin} will search {len(quadrants)} quadrants for potential destinations")
#
#         for quadrant in  quadrants:
#             delta = quadrant.delta
#             # Try both L-shaped offsets for this quadrant
#             candidate_1 = origin.shift(delta.delta_column * 2, delta.delta_row)
#             candidate_2 = origin.shift(delta.delta_column, delta.delta_row * 2)
#
#             for candidate in [candidate_1, candidate_2]:
#                 if not obsolete_board.coordinate_is_valid(candidate):
#                     continue
#                 chess_piece = obsolete_board.find_chess_piece(origin)
#                 if not obsolete_board.square_is_empty_or_contains_enemy(candidate, chess_piece.player):
#                     continue
#                 if KnightWalk.is_walkable(origin, candidate):
#                     occupant = obsolete_board.find_chess_piece(candidate)
#                     if occupant is None:
#                         destinations.append(candidate)
#                     elif chess_piece.is_enemy(occupant):
#                         print(f"{chess_piece.label} found enemy {occupant.label} at {candidate} adding the target")
#                         destinations.append(candidate)
#                         break
#                     else:
#                         print(f"{chess_piece.label} cannot occupy {candidate} friendly {occupant.label} lives there")
#                         break  # Blocked by friendly chess_piece
#                     destinations.append(candidate)
#         return destinations
