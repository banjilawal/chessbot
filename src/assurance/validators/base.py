from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from assurance.result.base import Result

T = TypeVar('T')

class Validator(ABC, Generic[T]):

    @staticmethod
    @abstractmethod
    def validate(t: Generic[T]) -> Result[T]:
        """
        Validates the input and returns a Result object.
         On success: Result(payload=t)
         On failure: Result(exception=...)
         Args:
             t (Generic[T]): The object to validate.

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
                        ValidationException otherwise.
         """
        pass