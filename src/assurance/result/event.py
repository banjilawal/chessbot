from abc import ABC
from typing import Optional

from chess.common.permit import Event
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




