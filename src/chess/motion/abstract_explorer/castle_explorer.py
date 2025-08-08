# from typing import List
#
# from chess.geometry.coordinate.coordinate import Coordinate
# from chess.team.element.chess_piece import ChessPiece
#
#
# class CastleMoveGenerator(MoveGenerator):
#     def __init__(self):
#         super().__init__()
#
#     def _perform_search(self, chess_piece: ChessPiece, obsolete_board: ObsoleteChessBoard) -> List[Coordinate]:
#         origin = chess_piece.current_coordinate()
#         destinations: List[Coordinate] = []
#         quadrants = chess_piece.rank.territories
#         print(f"{chess_piece.label} at {origin} will search {len(quadrants)} quadrants for potential destinations")
#
#         for quadrant in quadrants:
#             delta = quadrant.delta
#             current = origin
#
#             while True:
#                 try:
#                     current= current.shift(delta)
#                 except ValueError:
#                     # Went off the chess_board — stop searching in this direction
#                     break
#
#                 occupant = obsolete_board.find_chess_piece(current)
#                 if occupant is None:
#                     destinations.append(current)
#                 elif chess_piece.is_enemy(occupant):
#                     print(f"{chess_piece.label} found enemy {occupant.label} at {current} adding the target")
#                     destinations.append(current)
#                     break
#                 else:
#                     print(f"{chess_piece.label} cannot occupy {current} friendly {occupant.label} lives there")
#                     break  # Blocked by friendly chess_piece
#
#         return destinations
#


