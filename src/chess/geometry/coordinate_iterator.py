from chess.geometry.board import ChessBoard
from chess.geometry.board.coordinate import Coordinate, Delta


class CoordinateIterator:
    def __init__(self, origin: Coordinate, delta: Delta, board: ChessBoard):
        self.current = origin
        self.delta = delta
        self.board = board
        self.first_move = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.first_move:
            self.first_move = False
            next_pos = self.current.shift(self.delta)
        else:
            next_pos = self.current.shift(self.delta)

        if self.board.coordinate_is_valid(next_pos):
            self.current = next_pos
            return self.current
        else:
            raise StopIteration