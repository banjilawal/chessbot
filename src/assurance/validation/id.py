from typing import Generic

from assurance.exception.validation.id_validation import IdValidationException
from assurance.result.base_result import Result
from assurance.validation.specification import Specification, T
from chess.exception.base.negative_id_exception import NegativeIdException
from chess.exception.null.id_null import IdNullException


class IdSpecification(Specification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> Result[int]:
        method = "IdSpecification.is_satisfied_by"

        """
        Validates an Id meets specifications:
            - Not null
            - Not 0 or negative (is positive)
            
        Any validation error will have be encapsulated in a IdValidationException

        Args
            t (Coordinate): generic to be validated

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
                        IdValidationException otherwise.

        Raises:
            IdNullException: if t is null
            TypeError: if t is not int
            NegativeIdException: if t is negative   
            
            IdValidationException: Wraps any
                (IdNullException, TypeError, NegativeIdException)  
        """
        try:
            if t is None:
                raise IdNullException(f"{method} {IdNullException.DEFAULT_MESSAGE}")

            if not isinstance(t, int):
                raise TypeError(f"{method} Expected an integer, got {type(t).__name__}")

            entity_id = int(t)
            if entity_id < 0:
                raise NegativeIdException("{method} NegativeIdException.default_message")

            return Result(payload=entity_id)

        except(IdNullException, TypeError, NegativeIdException) as e:
            raise IdValidationException(
                f"{method} IdSpecification: Id validation failed"
            ) from e