from typing import Optional


class ValidationResult:
    _payload: object
    _is_valid: bool
    _errorMessage: str

    def __init__(self, payload: Optional[object], is_valid: Optional[bool], error_message: Optional[str]) -> None:
        self._payload = payload
        self._isValid = is_valid
        self._error_message = error_message

    @property
    def payload(self) -> Optional[object]:
        return self._payload

    @property
    def is_valid(self) -> Optional[bool]:
        return self._isValid

    @staticmethod
    def success(payload: object) -> 'ValidationResult':
        return ValidationResult(payload, True, None)

    @staticmethod
    def failure(self, error_message: str) -> 'ValidationResult':
        return ValidationResult(None, False, error_message)