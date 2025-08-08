#
# from typing import List
#
# from chess.geometry.obsolete_board.obsolete_board import ObsoleteChessBoard
#
# from chess.geometry.coordinate.coordinate import Coordinate
# from chess.team.element.piece import ChessPiece
#
#
# class KingMoveGenerator(MoveGenerator):
#
#     def _perform_search(self, piece: ChessPiece, obsolete_board: ObsoleteChessBoard) -> List[Coordinate]:
#         origin = piece.current_coordinate()
#         destinations: List[Coordinate] = []
#         quadrants = piece.rank.territories
#         print(f"{piece.label} at {origin} will search {len(quadrants)} quadrants for potential destinations")
#
#
#         queen_destinations = QueenMoveGenerator.search(piece, obsolete_board)
#
#         # Filter only coordinates that are one step away (Chebyshev distance == 1)
#         destinations = [
#             coordinate for coordinate in queen_destinations
#             if max(abs(coordinate.row - origin.row), abs(coordinate.column - origin.column)) == 1
#         ]
#
#         return destinations
