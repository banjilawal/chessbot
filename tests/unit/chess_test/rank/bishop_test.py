import unittest

from chess.competitor.commander import Commander
from chess.team.team_profile import TeamProfile
from chess.creator.entity.builder.chess_board_builder import ChessBoardBuilder

from chess.exception.rank_exception import BishopException
from chess.exception.walk import BishopWalkException
from chess.coord import Coord
from chess.geometry.quadrant import Quadrant
from chess.rank.bishop import Bishop
from chess.side.team import Side
from chess.piece.piece import Piece


class BishopTest(unittest.TestCase):

    def test_invalid_destination_raises_error(self):
        rank = Bishop("bishop", "b", 2, 1, [Quadrant.N])
        side = Side(1, Commander(1, "coosmof"), TeamProfile.BLACK)
        piece = Piece(1, "BB-1", rank, side)
        piece.positions.push_coord(Coord(0, 0))
        board = ChessBoardBuilder.build(1)

        with self.assertRaises(BishopException) as ctx:
            piece.rank.walk(piece, Coord(0, 1), board)
        self.assertIsInstance(ctx.exception.__cause__, BishopWalkException)


    def test_valid_destination_passes(self):
        rank = Bishop("bishop", "b", 2, 1, [Quadrant.N])
        board = ChessBoardBuilder.build(1)
        side = Side(1, Commander(1, "commander"), TeamProfile.BLACK)

        piece = Piece(1, "BB-1", rank, side)
        piece.positions.push_coord(Coord(0, 0))
        piece.rank.walk(piece, Coord(5, 5), board)


if __name__ == "__main__":
    unittest.main()