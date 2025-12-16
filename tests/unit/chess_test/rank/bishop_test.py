import unittest



class BishopTest(unittest.TestCase):

  def test_invalid_destination_raises_error(self):
    rank = Bishop("bishop", "b", 2, 1, [Quadrant.N])
    side = Side(1, Commander(1, "coosmof"), TeamProfile.BLACK)
    piece = Piece(1, "BB-1", rank, side)
    piece.positions.push_coord(Coord(0, 0))
    board = ChessBoardBuilder.build(1)

    with self.assertRaises(BishopException) as ctx:
      piece.rank_name.walk(piece, Coord(0, 1), board)
    self.assertIsInstance(ctx.exception.__cause__, BishopWalkException)


  def test_valid_destination_passes(self):
    rank = Bishop("bishop", "b", 2, 1, [Quadrant.N])
    board = ChessBoardBuilder.build(1)
    side = Side(1, Commander(1, "player_agent"), TeamProfile.BLACK)

    piece = Piece(1, "BB-1", rank, side)
    piece.positions.push_coord(Coord(0, 0))
    piece.rank_name.walk(piece, Coord(5, 5), board)


if __name__ == "__main__":
  unittest.main()