from chess.bishop.bishop import Bishop
from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.common.rank import Rank
from chess.motion.logic.diagonal_pattern import DiagonalPattern
from chess.motion.logic.vertical_pattern import VerticalPatern


class BishopRank(Rank):
    def __init__(self, movement_strategy: 'BishopSearchPattern'):
        super().__init__(movement_strategy)

    @staticmethod
    def occupy_destination(self, piece: Bishop, destination: Coordinate, board: Board):
       if piece is None:
           print("Bishop is None")
           return None
       if piece.current_position() is None:
           print("Bishop current position is None.")

           return None
       if board is None:
           print("Board is None")
           return None
       if not board.coordinate_is_valid(destination):
           print("Destination is not valid")
           return None
       if not DiagonalPattern.points_match_pattern(piece.current_position(), destination):
           print("points are not in diagonal pattern")
           return
       board.capture_square(piece, destination)