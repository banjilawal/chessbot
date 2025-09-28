from abc import ABC
from typing import Optional

from assurance.exception.empty.result import EmptyEventOutcomeConstructorException
from assurance.exception.event import ConflictingEventStateException

from chess.operation.null_occupation_request import NullRequestException
from chess.operation import Directive




class OperationResult:
    """
    Result of an operation that changes an entity' state.

    Use factory methods to create instances:
    - OperationResult.success()
    - OperationResult.failed()
    - OperationResult.rolled_back()

    Direct constructor usage is not recommended.
    """

    _id: int
    _directive: Directive
    _exception: Optional[Exception]
    _was_rolled_back: bool

    def __init__(
        self,
        result_id: int,
        directive: Directive,
        exception: Optional[Exception] = None,
        was_rolled_back: bool = False
    ):
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "OperationResult.__init__"

        self._id = result_id
        self._directive = directive
        self._exception = exception
        self._was_rolled_back = was_rolled_back


    @property
    def id(self):
        return self._id

    @property
    def directive(self) -> Optional[Directive]:
        return self._directive

    @property
    def exception(self) -> Optional[Exception]:
        return self._exception

    @property
    def was_rolled_back(self) -> bool:
        return self._was_rolled_back

    def is_success(self) -> bool:
        method = f"{self.__class__.__name__}.is_success"
        """True if operation success condition was true after the state change"""

        return self._exception is None and not self._was_rolled_back


    def is_processing(self) -> bool:
        method = f"{self.__class__.__name__}.is_processing"
        """True if operation still processing, has not changed state"""

        return self._event is None and self._exception is None and not self._was_rolled_back


    def is_failed(self) -> bool:
        method = f"{self.__class__.__name__}.is_failed"
        """True if raised an team_exception before the state changed"""

        return not (self._exception  is None and self._was_rolled_back)


    @classmethod
    def success(cls, outcome_id: int, request: Action, event: Event) -> 'OperationResult':
        method = f"{cls.__class__.__name__}.success"
        """Create a successful outcome"""

        return cls(
            op_result_id=outcome_id,
            request=request,
            event=event,
            exception=None,
            was_rolled_back=False
        )


    @classmethod
    def processing(cls, outcome_id: int, request: Action) -> 'OperationResult':
        method = f"{cls.__class__.__name__}.processing"

        """Create a processing outcome"""
        return cls(
            op_result_id=outcome_id,
            request=request,
            event=None,
            exception=None,
            was_rolled_back=False
        )


    @classmethod
    def failed(cls, outcome_id: int, request: Action, exception: Exception) -> 'OperationResult':
        method = f"{cls.__class__.__name__}.failed"
        """Create a failed outcome"""

        return cls(
            op_result_id=outcome_id,
            request=request,
            event=None,
            exception=exception,
            was_rolled_back=False
        )


    @classmethod
    def roll_back(cls, outcome_id: int, request: Action, event: Event) -> 'OperationResult':
        method = f"{cls.__class__.__name__}.rolled_back"
        """Create a rolled back outcome"""

        return cls(
            op_result_id=outcome_id,
            request=request,
            event=event,
            exception=None,
            was_rolled_back=True
        )





