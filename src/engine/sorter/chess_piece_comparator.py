from chess.rank.rank import Rank





class ChessPieceComparator:

    @staticmethod
    def compare(a: Rank, b: Rank):
        return a.capture_value - b.capture_value