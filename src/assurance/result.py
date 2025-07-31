from enum import auto, Enum
from typing import Optional

T = TypeVar('T')

class ResultStatus(Enum):
    SUCCESS = auto()
    FAILURE = auto()
    FAILURE_REQUIRES_ROLLBACK = auto()

class Result:
    _status: ResultStatus
    _payload: Optional[T] = None
    _message: Optional[str] = None
    _exception: Optional[Exception] = None

    def __init__(self, staus: ResultStatus, payload: T=None, message: str=None, exception: Exception=None):
        self._status = staus
        self._payload = payload
        self._message = message
        self._exception = exception

    @property
    def status(self) -> ResultStatus:
        return self._status

    @property
    def payload(self) -> T:
        return self._payload

    @property
    def message(self) -> str:
        return self._message

    @property
    def exception(self) -> Exception:
        return self._exception


