from typing import List, Union

from game.board.board_square import GameBoardSquare


class GameFigure:
    def __init__(
        self,
        id: int,
        length: int,
        width: int,
        color: str = None
    ):
        if id < 1:
            raise ValueError("piece id cannot be less than 1.")
        if length < 1:
            raise ValueError("piece length cannot be less than 1.")
        if width < 1:
            raise ValueError("piece width cannot be less than 1.")

        self._id = id
        self._width = width
        self._length = length
        self._occupied_squares: List[GameBoardSquare] = None  # Assuming this will be populated later
        self._color = color

    @property
    def id(self):
        return self._id

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def set_occupied_squares(self, squares):
        for square in squares:
            self.add_square(square)

    def add_square(self, square: 'GameBoardSquare'):
        if square is None:
            raise ValueError("square cannot be None.")
        if self._occupied_squares is None:
            self._occupied_squares: List['GameBoardSquare'] = []
        if square in self._occupied_squares:
            raise ValueError("square already occupied.")
        if square.occupant is not None:
            raise ValueError("square already occupied.")

        square.occupant = self
        self.occupied_squares = self._occupied_squares + [square]

        self._occupied_squares.append(square)

    @property
    def occupied_squares(self):
        return self._occupied_squares

    def area(self):
        return self.width * self.length

    def remove_square(self, square: 'GameBoardSquare'):
        if square is None:
            raise ValueError("square cannot be None.")
        if self._occupied_squares is None:
            raise ValueError("piece has no occupied squares.")
        if square not in self._occupied_squares:
            raise ValueError("square is not in the list.")
        if square.occupant is not self:
            raise ValueError("square is not occupied by this piece.")
        square.occupant = None
        self._occupied_squares.remove(square)
        self.occupied_squares = self._occupied_squares

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, GameFigure):
            return (self.id == other.id
                    and self.width == other.width
                    and self.length == other.length)
        else:
            return False

    def __hash__(self):
        return hash((self.id, self.width, self.length))

    def __repr__(self):
        return f"GamePiece(id:{self.id} width:{self.width} length:{self.length})"

    def find_square_by_id(self, square_id: int) -> Union['GameBoardSquare', None]:
        # Import GameBoardSquare here to avoid circular import
        from game.board.board_square import GameBoardSquare

        for i in range(len(self._occupied_squares)):
            if self._occupied_squares[i].id == square_id:  # Fixed: used square_id instead of id
                return self._occupied_squares[i]
        return None