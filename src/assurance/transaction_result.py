from typing import Optional, Generic

from assurance.result import Result, ResultStatus, T


class TransactionResult(Result, Generic[T]):
    def __init__(
            self,
            method_name: str,
            status: ResultStatus,
            payload: Optional[T] = None,
            message: Optional[str] = None,
            exception: Optional[Exception] = None,
            validation_result: Optional['ValidationResult'] = None
    ):
        super().__init__(
            status = status,
            payload = payload,
            message = message,
            exception =exception,
            validation_result = validation_result
        )
        self._method_name = method_name

    @property
    def method_name(self) -> str:
        return self._method_name