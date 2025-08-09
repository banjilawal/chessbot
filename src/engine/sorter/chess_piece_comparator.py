
from chess.token.piece import ChessPiece


class ChessPieceComparator:

    @staticmethod
    def compare(a: ChessPiece, b: ChessPiece):
        return a.rank.capture_value - b.rank.capture_value