from enum import Enum, auto
from typing import Optional, T, Generic


class ValidationStatus(Enum):
    IS_VALID = auto()
    INVALID = auto()


class ValidationResult(Generic[T]):
    def __init__(
        self,
        payload: Optional[T],
        status: ValidationStatus,
        error_message: Optional[str] = None
    ):
        self._payload = payload
        self._status = status
        self._error_message = error_message

    @property
    def payload(self) -> Optional[T]:
        return self._payload

    @property
    def status(self) -> ValidationStatus:
        return self._status

    @property
    def error_message(self) -> Optional[str]:
        return self._error_message

    @property
    def is_valid(self) -> bool:
        return self._status == ValidationStatus.IS_VALID

    @staticmethod
    def valid(payload: T) -> 'ValidationResult[T]':
        return ValidationResult(payload=payload, status=ValidationStatus.IS_VALID)

    @staticmethod
    def invalid(message: str) -> 'ValidationResult[T]':
        return ValidationResult(payload=None, status=ValidationStatus.INVALID, error_message=message)