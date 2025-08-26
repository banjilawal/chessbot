from chess.board.square import Square
from chess.token.piece import ChessPiece


class CoordinateBinding:
    _square: Square
    _chess_piece: ChessPiece


    def __init__(self, square: Square, chess_piece: ChessPiece):
        self._square = square
        self._chess_piece = chess_piece

    @property
    def square(self) -> Square:
        return self._square

    @property
    def chess_piece(self) -> ChessPiece:
        return self._chess_piece