from enum import Enum, auto
from typing import Optional, T, Generic, TypeVar

from assurance.validation.validation_exception import ValidationException

T = TypeVar('T')

class TestOutcome(Enum):
    PASSED_VALIDATION_TEST = auto()
    FAILED_VALIDATION_TEST = auto()


class ValidationReport(Generic[T]):
    _payload: T
    _test_outcome: TestOutcome
    _validation_exception: Optional[ValidationException]


    def __init__(self, payload: Optional[T], test_outcome: TestOutcome, validation_exception: ValidationException):
        self._payload = payload
        self._test_outcome = test_outcome
        self._validation_exception = validation_exception

    @property
    def payload(self) -> Optional[T]:
        return self._payload


    @property
    def test_outcome(self) -> TestOutcome:
        return self._test_outcome


    @property
    def validation_exception(self) -> Optional[ValidationException]:
        return self._validation_exception


    @staticmethod
    def send_passed_validation_report(payload: T) -> 'ValidationReport[T]':
        return ValidationReport(payload=payload, test_outcome=TestOutcome.PASSED_VALIDATION_TEST)


    @staticmethod
    def send_failed_valtidation_report(validation_exception: ValidationException) -> 'ValidationReport[T]':
        return ValidationReport(payload=None, test_outcome=TestOutcome.FAILED_VALIDATION_TEST, validation_exception=validation_exception)