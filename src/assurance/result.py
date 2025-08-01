from enum import Enum, auto
from typing import Optional, TypeVar, Generic

from assurance.validation.validation_result import ValidationResult

T = TypeVar('T')


class ResultStatus(Enum):
    SUCCESS = auto()
    FAILURE = auto()
    EMPTY_SEARCH_RESULT = auto()
    FAILURE_REQUIRES_ROLLBACK = auto()


class Result(Generic[T]):
    def __init__(
        self,
        status: ResultStatus,
        payload: Optional[T] = None,
        message: Optional[str] = None,
        exception: Optional[Exception] = None,
        validation_result: Optional['ValidationResult'] = None
    ):
        self._status = status
        self._payload = payload
        self._message = message
        self._exception = exception
        self._validation_result = validation_result


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
    def validation_result(self) -> Optional['ValidationResult']:
        return self._validation_result

    @staticmethod
    def ok(payload: Optional[T], message: Optional[str]) -> 'Result[T]':
        return Result(status=ResultStatus.SUCCESS, payload=payload, message=message)

    @staticmethod
    def fail(
        message: str,
        exception: Optional[Exception] = None,
        validation_result: Optional['ValidationResult'] = None,
        status: ResultStatus = ResultStatus.FAILURE | ResultStatus.FAILURE_REQUIRES_ROLLBACK
     ) -> 'Result[T]':
        return Result(status=status, message=message, exception=exception, validation_result=validation_result)





