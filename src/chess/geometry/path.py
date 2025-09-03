from enum import Enum, auto
from typing import cast

from assurance.validators.coord import CoordinateValidator
from chess.geometry.coord import Coordinate


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
    _u: Coordinate
    _v: Coordinate
    _line: Line
    _euclid_dist: int

    def __init__(self, u: Coordinate, v: Coordinate):
        method = "Path.__init__"
        u_validation = CoordinateValidator.validate(u)
        if not u_validation.is_success():
            raise u_validation.exception

        v_validation = CoordinateValidator.validate(v)
        if not v_validation.is_success():
            raise v_validation.exception

        self._u = cast(u_validation.payload, Coordinate)
        self._v = cast(v_validation.payload, Coordinate)

        self._line = self._classify_line()
        self._euclidean_dist = self._euclidean_magnitude()


    @property
    def u(self) -> Coordinate:
        return self._u


    @property
    def v(self) -> Coordinate:
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
            p (Coordinate): One coordinate in the pair
            q (Coordinate): Other coordinate in the pair
        """

        return ((self._u.row - self._v.row) ** 2) + ((self._u.column - self._v.column) ** 2)


    def _classify_line(self) -> Line:
        method = "Path.classify_path"

        if self._is_pawn_opening():
            return Line.PAWN_OPENING

        if self._is_pawn_advance():
            return Line.PAWN_ADVANCE

        if self._is_pawn_attack():
            return Line.PAWN_ATTACK

        if self._is_knight():
            return Line.KNIGHT

        if self._is_queen():
            return Line.QUEEN

        if self._is_king():
            return Line.KING

        if self._is_castle():
            return Line.CASTLE

        if self._is_bishop():
            return Line.BISHOP

        return Line.CURVILINEAR


    def _is_vertical(self):
        return self._u.row != self._v.row and self._u.column == self._v.column


    def _is_horizontal(self):
        return self._u.row == self._v.row and self._u.column != self._v.column


    def _is_diagonal(self):
        return (
            self._u != self._v and
            abs(self._v.row - self._u.row) == abs(self._v.column - self._u.column)
        )


    def _is_bishop(self):
        return self._is_diagonal()


    def _is_castle(self):
        return self._is_vertical() or self._is_horizontal()


    def _is_queen(self):
        return self._is_bishop() or self._is_castle()


    def _is_knight(self):
        row_diff = abs(self._v.row - self._u.row)
        column_diff = abs(self._v.column - self._u.column)
        return (row_diff == 2 and column_diff == 1) or (row_diff == 1 and column_diff == 2)


    def _is_king(self):
        return (
            abs(self._v.row - self._u.row) == 1 and abs(self._v.column - self._u.column) == 1
        )


    def _is_pawn_opening(self):
        return self._u.column == self._v.column and self._v.row - self._u.row == 2


    def _is_pawn_advance(self):
        return self._u.column == self._v.column and self._v.row - self._u.row == 2


    def _is_pawn_attack(self):
        row_dif = self._v.row - self._u.row
        column_diff = abs(self._u.column - self._v.column)
        return row_dif == 1 and column_diff == 1



