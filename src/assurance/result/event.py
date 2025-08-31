from abc import ABC
from typing import Optional

from assurance.exception.empty.result import EmptyEventOutcomeConstructorException
from assurance.exception.event import ConflictingEventStateException
from chess.common.permit import Event
from chess.exception.null.request import NullRequestException
from chess.request.base import Request



class RequestOutcome(ABC):
    _request: Request
    _event: Optional[Event]
    _exception: Optional[Exception]

    def __init__(
        self,
        request: Request,
        event: Optional[Event] = None,
        exception: Optional[Exception] = None
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

        self._request = request
        self._event = event
        self._exception = exception


    @property
    def request(self) -> Optional[Request]:
        return self._request


    @property
    def event(self) -> Optional[Event]:
        return self._event


    @property
    def exception(self) -> Optional[Exception]:
        return self._exception


    def is_success(self) -> bool:
        return self._exception is None and self._event is not None




