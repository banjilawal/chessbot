from chess.board import Board
from chess.piece import Piece
from chess.square import Square
from chess.system import Event


class PromotionEvent(Event[Piece, Square, Board]):
    pass