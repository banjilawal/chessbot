from chess.common.result import ResultPayloadConflictException, EmptyResultConstructorException
from typing import Optional, TypeVar, Generic


T = TypeVar('T')

class BuildResult(Generic[T]):
    """
    BuildResult is a generic class that encapsulates the outcome of Builder operation. BuildResult has the
    same structure as Result but is used specifically in the context of building entities. It can hold either.
    a payload of type T or an Exception, but not both. If the build operation is successful, the payload will
    contain the built object. If the build operation fails, the exception will contain the error that
    occurred during the build process.

    BuildResult is helpful for debugging and showing Builders have different outcomes than operations which generate a result.

    Attributes:
        _payload (Optional[T]): The payload of the result, if successful.
        _exception (Optional[Exception]): The exception of the result, if failed.

    Methods:
        is_success() -> bool: Returns True if the result is successful (i.e., has a payload only).
    """


    def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
        """
        Initializes a BuildResult object.
        Args:
            payload (Optional[T]): The payload of the result, if successful.
            exception (Optional[Exception]): The exception of the result, if failed.
        Raises:
            EmptyResultConstructorException: If neither payload nor exception is provided.
            ResultPayloadConflictException: If both payload and exception are provided.
        """
        method = "Result.__init_"

        if payload is None and exception is None:
            raise EmptyResultConstructorException(f"{method}: {EmptyResultConstructorException.DEFAULT_MESSAGE}")

        if  not (payload is None or exception is None):
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
        return self._exception is None and self._payload is not None




