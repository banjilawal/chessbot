from chess.board.element.square import Square


class SquareComparator:
    _a: Square
    _b: Square

    def __init__(self, a: Square, b: Square):
        self_a = a
        self_b = b

    @property
    def a(self) -> Square:
        return self._a

    @property
    def b(self) -> Square:
        return self._b


    def compare(self, a, b) -> int:
        return