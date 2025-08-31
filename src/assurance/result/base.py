
from typing import Optional, TypeVar, Generic


T = TypeVar('T')

class Result(Generic[T]):
    def __init__(
        self,
        payload: Optional[T] = None,
        exception: Optional[Exception] = None,
    ):
        method = "Result.__init_"
        if payload is not None and exception is not None:
            raise ResultPayloadConflictException(f"{method}: {ResultPayloadConflictException.DEFAULT_MESSAGE}")
        self._payload = payload
        self._exception = exception


    @property
    def payload(self) -> Optional[T]:
        return self._payload


    @property
    def exception(self) -> Optional[Exception]:
        return self._exception


    def is_success(self) -> bool:
        return self._exception is None
