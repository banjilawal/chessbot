from typing import Generic

from assurance.validation.specification import Specification, T
from chess.exception.exception import NegativeIdException
from chess.exception.null_exception import IdNullException


class IdSpecification(Specification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> bool:
        method = "IdSpecification.is_satisfied_by"

        """
        Validates that the provided identifier is a non-negative integer.
        Raises exceptions if the identifier is
        """

        if t is None:
            raise IdNullException(f"{method} IdNullException.default_message")
        if not isinstance(t, int):
            raise TypeError(f"{method} Expected an integer, got {type(t).__name__}")
        entity_id = int(t)
        if entity_id < 0:
            raise NegativeIdException("{method} NegativeIdException.default_message")

        return True