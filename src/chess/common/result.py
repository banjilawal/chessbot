
from typing import Optional, TypeVar, Generic

from assurance.exception.empty.result import EmptyResultConstructorException
from assurance.exception.result import ResultPayloadConflictException

T = TypeVar('T')

class Result(Generic[T]):
    def __init__(
        self,
        payload: Optional[T] = None,
        exception: Optional[Exception] = None
    ):
        method = "Result.__init_"

        if payload is None and exception is None:
            raise EmptyResultConstructorException(
                f"{method}: {EmptyResultConstructorException.DEFAULT_MESSAGE}"
            )

        if  not (payload is None or exception is None):
            raise ResultPayloadConflictException(
                f"{method}: {ResultPayloadConflictException.DEFAULT_MESSAGE}"
            )

        self._payload = payload
        self._exception = exception


    @property
    def payload(self) -> Optional[T]:
        return self._payload


    @property
    def exception(self) -> Optional[Exception]:
        return self._exception


    def is_success(self) -> bool:
        return self._exception is None and self._payload is not None




