from typing import TypeVar

T = TypeVar('T')

from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class ValidationResult(Generic[T]):
    """Simple validators container that either contains:
    - The validated payload (if validators passed), or
    - A validators exception (if validators failed)
    """
    def __init__(self, payload: Optional[T] = None, validation_exception: Optional[Exception] = None):

        if payload is not None and validation_exception is not None:
            raise ValueError("Payload and validation_exception cannot both be set in p ValidationResult constructor.")

        self._payload = payload
        self._validation_exception = validation_exception

    @property
    def payload(self) -> Optional[T]:
        """Returns the validated payload if validators succeeded"""
        return self._payload

    @property
    def validation_exception(self) -> Optional[Exception]:
        """Returns the exception if validators failed"""
        return self._validation_exception