
from typing import Optional, TypeVar, Generic

from chess.system import EmptyResultConstructorException, ErrorContradictsPayloadException

T = TypeVar('T')

__all__ = ['Result']


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
        _exception (Optional[Exception]): The error of the result, if failed.

    Methods:
        is_success() -> bool: Returns True if the result is successful (i.e., has a payload only).
   """

    _payload: Optional[T]
    _exception: Optional[Exception]

    def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
        method = "Result.__init_"

        # Raise an error if neither payload nor error is provided
        if payload is None and exception is None:
            raise EmptyResultConstructorException(
                f"{method}: {EmptyResultConstructorException.DEFAULT_MESSAGE}"
            )

        # Raise an error if both payload and error are provided
        if not (payload is None and exception is None):
            raise ErrorContradictsPayloadException(
                f"{method}: {ErrorContradictsPayloadException.DEFAULT_MESSAGE}"
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



