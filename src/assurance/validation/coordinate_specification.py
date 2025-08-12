from typing import Generic

from assurance.validation.specification import Specification, T
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.exception.null_exception import NullCoordinateException
from chess.geometry.coordinate.coordinate import Coordinate, RowOutOfBoundsException


class CoordinateSpecification(Specification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> bool:
        method = "CoordinateSpecification.is_satisfied_by"

        """
        """

        if t is None:
            raise NullCoordinateException(f"{method} NullCoordinateException.default_message")
        if not isinstance(t, Coordinate):
            raise TypeError(f"{method} Expected a Coordinate, got {type(t).__name__}")

        coordinate: Coordinate = t
        if coordinate.row < 0 or coordinate.row >= ROW_SIZE:
            raise RowOutOfBoundsException(f"{method} {RowOutOfBoundsException.default_message}")

        if coordinate.column < 0 or coordinate.column >= COLUMN_SIZE:
            raise RowOutOfBoundsException(f"{method} {RowOutOfBoundsException.default_message}")

        return True