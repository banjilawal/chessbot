
from typing import Optional, TypeVar, Generic


T = TypeVar('T')

class SearchResult:
    _payload: Optional[T]
    _exception: Optional[Exception]

    def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
        method = "SearchResult.__init_"

        self._payload = payload
        self._exception = exception


    def is_success(self) -> bool:
        return self._exception is None and self._payload is not None


    def is_empty(self) -> bool:
        return not (self._exception is None and self._payload is None)


    def __str__(self):
        if self.is_success():
            return f"Result(SUCCESS: {self._payload})"
        elif self.is_empty():
            return "Result(NOT_FOUND)"
        else:
            return f"Result(FAILURE: {self._exception}"