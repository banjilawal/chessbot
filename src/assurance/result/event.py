from abc import ABC
from enum import Enum, auto
from typing import Optional

from assurance.exception.empty.result import EmptyEventOutcomeConstructorException
from assurance.exception.event import ConflictingEventStateException
from chess.common.permit import Event
from chess.exception.null.request import NullRequestException
from chess.system.request import Request


class RequestOutcome(ABC):
    _id:int
    _request: Request
    _event: Optional[Event]
    _exception: Optional[Exception]
    _was_rolled_back: bool

    def __init__(
        self,
        outcome_id:int,
        request: Request,
        event: Optional[Event] = None,
        exception: Optional[Exception] = None,
        was_rolled_back: bool = False
    ):
        method = "RequestOutcome.__init__"

        if request is None:
            raise NullRequestException(f"{method}: {NullRequestException.DEFAULT_MESSAGE}")

        if event is None and exception is None:
            raise EmptyEventOutcomeConstructorException(
                f"{method}: {EmptyEventOutcomeConstructorException.DEFAULT_MESSAGE}"
            )

        if event is not None and exception is not None:
            raise ConflictingEventStateException(
               f"{method}: {ConflictingEventStateException.DEFAULT_MESSAGE}"
            )

        self._id = outcome_id
        self._request = request
        self._event = event
        self._exception = exception
        self._was_rolled_back = was_rolled_back


    @property
    def id(self):
        return self._id


    @property
    def request(self) -> Optional[Request]:
        return self._request


    @property
    def event(self) -> Optional[Event]:
        return self._event


    @property
    def exception(self) -> Optional[Exception]:
        return self._exception


    @property
    def was_rolled_back(self) -> bool:
        return self._was_rolled_back


    def is_success(self) -> bool:
        method = f"{self.__class__.__name__}.is_success"
        """True if operation success condition was true after the state change"""

        return self._exception is None and not (self._event is None and self._was_rolled_back)


    def is_processing(self) -> bool:
        method = f"{self.__class__.__name__}.is_processing"
        """True if operation still processing, has not changed state"""

        return self._event is None and self._exception is None and not self._was_rolled_back


    def is_failed(self) -> bool:
        method = f"{self.__class__.__name__}.is_failed"
        """True if raised an exception before the state changed"""

        return not (self._exception  is None and self._was_rolled_back)


    def is_rolled_back(self) -> bool:
        method = f"{self.__class__.__name__}.is_rolled_back"

        """True if operation completed the success condition was not met so the operation was rolled back"""
        return self._was_rolled_back


    @classmethod
    def success(cls, outcome_id: int, request: Request, event: Event) -> 'RequestOutcome':
        method = f"{cls.__class__.__name__}.success"
        """Create a successful outcome"""

        return cls(
            outcome_id=outcome_id,
            request=request,
            event=event,
            exception=None,
            rolled_back=False
        )


    @classmethod
    def proceessing(cls, outcome_id: int, request: Request) -> 'RequestOutcome':
        method = f"{cls.__class__.__name__}.processing"

        """Create a processing outcome"""
        return cls(
            outcome_id=outcome_id,
            request=request,
            event=None,
            exception=None,
            rolled_back=False
        )


    @classmethod
    def failed(cls, outcome_id: int, request: Request, exception: Exception) -> 'RequestOutcome':
        method = f"{cls.__class__.__name__}.failed"
        """Create a failed outcome"""

        return cls(
            outcome_id=outcome_id,
            request=request,
            event=None,
            exception=exception,
            rolled_back=False
        )


    @classmethod
    def roll_back(cls, outcome_id: int, request: Request, event: Event) -> 'RequestOutcome':
        method = f"{cls.__class__.__name__}.rolled_back"
        """Create a rolled back outcome"""

        return cls(
            outcome_id=outcome_id,
            request=request,
            event=event,
            exception=None,
            rolled_back=True
        )





