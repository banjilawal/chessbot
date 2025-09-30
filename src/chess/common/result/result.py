
from typing import Optional, TypeVar, Generic


T = TypeVar('T')

__all__ = [
    'Result',
    'SearchResult'
]

class Result(Generic[T]):
    """
    A Result object encapsulates the outcome of methods and operations that return an object. Different from
    TransactionResult which assures an existing object's state changed correctly without causing inconsistencies.

    USAGE:
        Result is used with
        - Validation of existing objects.
        - Objects returned by accessors and query methods.
        - Operations that return an object, but may fail due to business logic or other reasons.
        - Methods that may fail due to external factors (e.g., network issues, file I

    Attributes:
        _payload (Optional[T]): The payload of the result, if successful.
        _exception (Optional[Exception]): The exception of the result, if failed.

    Methods:
        is_success() -> bool: Returns True if the result is successful (i.e., has a payload only).
   """

    def __init__(
        self,
        payload: Optional[T] = None,
        exception: Optional[Exception] = None
    ):
        method = "Result.__init_"

        # Raise an exception if neither payload nor exception is provided
        if payload is None and exception is None:
            raise EmptyResultConstructorException(
                f"{method}: {EmptyResultConstructorException.DEFAULT_MESSAGE}"
            )

        # Raise an exception if both payload and exception are provided
        if not (payload is None and exception is None):
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


class SearchResult(Result):

    def is_not_found(self) -> bool:
        """"""
        return not (self._exception is None and self._payload is None)

    def __str__(self):
        if self.is_success():
            return f"Result(SUCCESS: {self._payload})"
        elif self.is_not_found():
            return "Result(NOT_FOUND)"
        else:
            return f"Result(FAILURE: {self._exception}"



