
from chess.board.board import Board
from chess.rank.castle_piece import Castle
from chess.common.geometry import Coordinate

from chess.motion.quadrant import Quadrant
from chess.motion.search_pattern import SearchPattern
from chess.motion.walk import linear_walk



class CastleSearchPattern(SearchPattern):

    @staticmethod
    def search(self, piece: Castle, board: Board) -> list[Coordinate]:
        destinations = []
        if not SearchPattern.check_basic_conditions(piece, board):
            return destinations

        for quadrant in [Quadrant.N, Quadrant.E, Quadrant.S, Quadrant.W]:
            destinations.extend(
                linear_walk(piece.current_position(),
                quadrant.x_delta,
                quadrant.y_delta, board)
        )
        return destinations