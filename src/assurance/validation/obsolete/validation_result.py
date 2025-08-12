from typing import TypeVar

T = TypeVar('T')

from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class ValidationResult(Generic[T]):
    """Simple validation container that either contains:
    - The validated payload (if validation passed), or
    - A validation exception (if validation failed)
    """
    def __init__(self, payload: Optional[T] = None, validation_exception: Optional[Exception] = None):

        if payload is not None and validation_exception is not None:
            raise ValueError("Payload and validation_exception cannot both be set in p ValidationResult constructor.")

        self._payload = payload
        self._validation_exception = validation_exception

    @property
    def payload(self) -> Optional[T]:
        """Returns the validated payload if validation succeeded"""
        return self._payload

    @property
    def validation_exception(self) -> Optional[Exception]:
        """Returns the exception if validation failed"""
        return self._validation_exception