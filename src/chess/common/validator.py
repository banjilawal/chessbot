from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.result import Result

T = TypeVar('T')

"""Super class for entity validators."""
class Validator(ABC, Generic[T]):
    """
    Validates an entity being passed as parameter meets:
        - Is not null.
        - Its fields meet the specifications for the domain.
    Unmet requirements raise an exception for their specific failure. Any validator failure
    is wrapped in a ValidationException.

    For performance and single source of truth Validator has:
        - No fields
        - only static method validate
    subclasses must implement validate.
    """

    @staticmethod
    @abstractmethod
    def validate(t: Generic[T]) -> Result[T]:
        """
        Validates an object passed to a function or declared in a module meets domain requirements.

         Args:
             t (Generic[T]): The object to validate.

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
                        ValidationException otherwise.

        Raises:
            ValidationException: if t fails any requirement checks.
         """
        pass