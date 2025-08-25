from typing import Generic

from assurance.validation.specification import Specification, T
from chess.exception.base.negative_id_exception import NegativeIdException
from chess.exception.null.id_null import IdNullException


class IdSpecification(Specification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> bool:
        method = "IdSpecification.is_satisfied_by"

        """
        Validates an Id meets specifications:
            - Not null
            - Not 0 or negative (is positive)
            
        Any validation error will have be encapsulated in a IdValidationException

        Args
            t (Coordinate): generic to be validated

        Returns:
            bool: True if if passes meets specifications. In testing only ever returns
                true.

        Raises:
            IdNullException: if t is null
            TypeError: if t is not int
            

            RowOutOfBoundsException: If coordinate.row is outside the range 
                (0, ROW_SIZE - 1) inclusive

            ColumnOutOfBoundsException: If coordinate.column is outside the range
                (0, COLUMN_SIZE - 1) inclusive.
                
            CoordinateValidationException: Wraps any
                (NullCoordinate, TypeError, RowOutOfBounds or ColumnOutOfBoundsException)
        """

        if t is None:
            raise IdNullException(f"{method} IdNullException.default_message")
        if not isinstance(t, int):
            raise TypeError(f"{method} Expected an integer, got {type(t).__name__}")
        entity_id = int(t)
        if entity_id < 0:
            raise NegativeIdException("{method} NegativeIdException.default_message")

        return True