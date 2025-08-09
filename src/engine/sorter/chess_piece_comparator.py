from chess.rank.rank import Rank
from chess.token.piece import ChessPiece


class ChessPieceComparator:

    @staticmethod
    def compare(a: ChessPiece, b: ChessPiece):
        if not a.is_enemy(b):
            return a.capture_value - b.capture_value
        return 0

class SquareOccupantComparator:
    def __init__(self, piece):
        self.piece = piece

    def compare(self, square1, square2):
        if self.piece.color == 'white':
            return square1.y - square2.y
        else:
            return square2.y - square1.y