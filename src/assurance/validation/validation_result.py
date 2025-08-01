from enum import Enum, auto
from typing import Optional, T, Generic, TypeVar

T = TypeVar('T')

class TestOutcome(Enum):
    IS_VALID = auto()
    INVALID = auto()


class ValidationReport(Generic[T]):
    _payload: T
    _test_outcome: TestOutcome
    _validation_failure_message: Optional[str]

    def __init__(self, payload: Optional[T], test_outcome: TestOutcome, validation_failure_message: Optional[str] = None):
        self._payload = payload
        self._test_outcome = test_outcome
        self._validation_failure_message = validation_failure_message

    @property
    def payload(self) -> Optional[T]:
        return self._payload

    @property
    def test_outcome(self) -> TestOutcome:
        return self._test_outcome

    @property
    def validation_failure_message(self) -> Optional[str]:
        return self._validation_failure_message


    @staticmethod
    def valid_outcome_report(payload: T) -> 'ValidationReport[T]':
        return ValidationReport(payload=payload, test_outcome=TestOutcome.IS_VALID)


    @staticmethod
    def invalid_outcome_report(message: str) -> 'ValidationReport[T]':
        return ValidationReport(payload=None, test_outcome=TestOutcome.INVALID, validation_failure_message=message)