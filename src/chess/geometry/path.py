from enum import Enum, auto
from typing import cast

from assurance.validators.coord import CoordValidator
from chess.geometry.coord import Coord


class Line(Enum):
    VERTICAL = auto(),
    DIAGONAL = auto(),
    HORIZONTAL = auto(),
    KING = auto()
    KNIGHT = auto()
    BISHOP = auto ()
    CASTLE = auto()
    QUEEN = auto()
    PAWN_OPENING = auto()
    PAWN_ADVANCE = auto()
    PAWN_ATTACK = auto()
    CURVILINEAR = auto()


class Path:
    _u: Coord
    _v: Coord
    _line: Line
    _euclid_dist: int

    def __init__(self, u: Coord, v: Coord):
        method = "Path.__init__"

        u_validation = CoordValidator.validate(u)
        if not u_validation.is_success():
            raise u_validation.exception

        v_validation = CoordValidator.validate(v)
        if not v_validation.is_success():
            raise v_validation.exception

        self._u = cast(Coord, u_validation.payload)
        self._v = cast(Coord, v_validation.payload)

        self._line = self._classify_line()
        self._euclidean_dist = self._euclidean_magnitude()


    @property
    def u(self) -> Coord:
        return self._u


    @property
    def v(self) -> Coord:
        return self._v


    @property
    def line(self) -> Line:
        return self._line


    @property
    def euclidean_dist(self):
        return self.euclidean_dist


    def _euclidean_magnitude(self) -> int:
        """
        Creates a CartesianDistance instance. _distance is calculated inside the constructor

        Args:
            p (Coord): One coord in the pair
            q (Coord): Other coord in the pair
        """

        return ((self._u.row - self._v.row) ** 2) + ((self._u.column - self._v.column) ** 2)


    def _classify_line(self) -> Line:
        method = "Path.classify_path"

        matches = {
            Line.QUEEN: self.is_queen(),
            Line.BISHOP: self.is_diagonal(),
            Line.CASTLE: self.is_castle(),
            Line.KNIGHT: self.is_knight(),
            Line.KING: self.is_king(),
            Line.PAWN_ATTACK: self.is_pawn_attack(),
            Line.PAWN_ADVANCE: self.is_pawn_advance(),
            Line.PAWN_OPENING: self.is_pawn_opening(),
        }

        # Priority order, highest first
        priority = [
            Line.KING,
            Line.QUEEN,
            Line.KNIGHT,
            Line.BISHOP,
            Line.CASTLE,
            Line.PAWN_OPENING,
            Line.PAWN_ADVANCE,
            Line.PAWN_ATTACK,
        ]

        for line in priority:
            if matches.get(line):
                return line

        # if self._is_king():
        #     return Line.KING
        #
        # if self._is_knight():
        #     return Line.KNIGHT
        #
        # if self._is_queen():
        #     return Line.QUEEN
        #
        # if self._is_castle() and not self._is_queen():
        #     return Line.CASTLE
        #
        # if self._is_bishop() and not self._is_queen():
        #     print(f"diagonal => {self._u}, {self._v}")
        #     return Line.BISHOP
        #
        # if self._is_pawn_opening() and not self._is_bishop:
        #     return Line.PAWN_OPENING
        #
        # if self._is_pawn_advance():
        #     return Line.PAWN_ADVANCE
        #
        # if self._is_pawn_attack():
        #     return Line.PAWN_ATTACK


        return Line.CURVILINEAR


    def is_vertical(self):
        return self._u.row != self._v.row and self._u.column == self._v.column


    def is_horizontal(self):
        return self._u.row == self._v.row and self._u.column != self._v.column


    def is_diagonal(self):
        return (
            self._u != self._v and
            abs(self._v.row - self._u.row) == abs(self._v.column - self._u.column)
        )


    def _is_bishop(self):
        return  not (self.is_vertical() or self.is_horizontal()) and self.is_diagonal()


    def is_castle(self):
        return not self.is_diagonal and (self.is_vertical() or self.is_horizontal())


    def is_queen(self):
        return self.is_diagonal() or self.is_horizontal() or self.is_vertical()


    def is_knight(self):
        row_diff = abs(self._v.row - self._u.row)
        column_diff = abs(self._v.column - self._u.column)
        return (row_diff == 2 and column_diff == 1) or (row_diff == 1 and column_diff == 2)


    def is_king(self):
        row_diff = abs(self._v.row - self._u.row)
        column_diff = abs(self._v.column - self._u.column)
        return row_diff <= 1 and column_diff <= 1 and (row_diff + column_diff) > 0


    def is_pawn_opening(self):
        return self._u.column == self._v.column and (self._v.row - self._u.row) == 2


    def is_pawn_advance(self):
        return self._u.column == self._v.column and self._v.row - self._u.row == 2


    def is_pawn_attack(self):
        row_dif = self._v.row - self._u.row
        column_diff = abs(self._v.column - self._u.column)
        return row_dif == 1 and column_diff == 1


def main():
    path = Path(u=Coord(0, 0), v=Coord(0, 5))
    print(path.line)

if __name__ == "__main__":
    main()



