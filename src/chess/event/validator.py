from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

from chess.common import ExecutionContext, Result
from chess.event import Event

T = TypeVar('T', bound=Event)


class EventValidator(ABC, Generic[T]):



    """
    Validates an entity being passed as parameter meets:
        - Is not null.
        - Its fields meet the specifications for the domain.
    Unmet requirements raise an team_exception for their specific failure. Any validator failure
    is wrapped in a ValidationException.

    For performance and single source of truth Validator has:
        - No fields
        - only static method validate
    subclasses must implement validate.
    """

    @classmethod
    @abstractmethod
    def validate(cls, t: T, context: Optional[ExecutionContext]) -> Result[T]:
        """
        Validates an object passed to a function or declared in a module meets domain requirements.
         Args:
             t (Generic[T]): The object to validate.
             context (ExecutionContext): The context in which the object is being validated.
         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
                        ValidationException otherwise.
        Raises:
            ValidationException: if t fails any requirement checks.
         """
        pass