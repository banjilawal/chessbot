#
# from typing import List
#
# from chess.geometry.board.board import ChessBoard
#
# from chess.geometry.coordinate.coordinate import Coordinate
# from chess.team.model.piece import ChessPiece
#
#
# class KingMoveGenerator(MoveGenerator):
#
#     def _perform_search(self, piece: ChessPiece, board: ChessBoard) -> List[Coordinate]:
#         origin = piece.current_coordinate()
#         destinations: List[Coordinate] = []
#         quadrants = piece.motion_controller.territories
#         print(f"{piece.label} at {origin} will search {len(quadrants)} quadrants for potential destinations")
#
#
#         queen_destinations = QueenMoveGenerator.search(piece, board)
#
#         # Filter only coordinates that are one step away (Chebyshev distance == 1)
#         destinations = [
#             coordinate for coordinate in queen_destinations
#             if max(abs(coordinate.row - origin.row), abs(coordinate.column - origin.column)) == 1
#         ]
#
#         return destinations
