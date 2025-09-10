from chess.square import Square
from chess.piece.piece import Piece


class CoordinateBinding:
    _square: Square
    _chess_piece: Piece


    def __init__(self, square: Square, chess_piece: Piece):
        self._square = square
        self._chess_piece = chess_piece

    @property
    def square(self) -> Square:
        return self._square

    @property
    def chess_piece(self) -> Piece:
        return self._chess_piece