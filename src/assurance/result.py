from abc import ABC
from enum import Enum, auto
from typing import Optional, TypeVar, Generic

T = TypeVar('T')


class ResultStatus(Enum):
    SUCCESS = auto()
    FAILURE = auto()
    FAILURE_REQUIRES_ROLLBACK = auto()


class Result(Generic[T]):
    def __init__(
        self,
        status: ResultStatus,
        payload: Optional[T] = None,
        message: Optional[str] = None,
        exception: Optional[Exception] = None
    ):
        self._status = status
        self._payload = payload
        self._message = message
        self._exception = exception

    @property
    def status(self) -> ResultStatus:
        return self._status

    @property
    def payload(self) -> Optional[T]:
        return self._payload

    @property
    def message(self) -> Optional[str]:
        return self._message

    @property
    def exception(self) -> Optional[Exception]:
        return self._exception

    @property
    def status(self) -> ResultStatus:
        return self._status


    @staticmethod
    def ok(data: Optional[T] = None) -> 'Result[T]':
        return Result(status=ResultStatus.SUCCESS, payload=data, message=None)

    @staticmethod
    def fail(message: str, exception: Optional[Exception] = None) -> 'Result[T]':
        return Result(status=ResultStatus.FAILURE, message=message, exception=exception)

    @staticmethod
    def fail_with_rollback(message: str, exception: Optional[Exception] = None) -> 'Result[T]':
        return Result(status=ResultStatus.FAILURE_REQUIRES_ROLLBACK, message=message, exception=exception)



