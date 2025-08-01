from assurance.validation.validatin_report import ValidationReport
from assurance.validation.validation_exception import ValidationException
from chess.transaction.transaction_result import TransactionResult, Failure, StatusCode

class IdPositiveValidationFailed(ValidationException):
    default_message = "Failed id is positive validation test"

class IdNotNullValidationFailed(ValidationException):
    default_message = "Failed id exsts validation test"

class IdValidator:

    @staticmethod
    def test_id_positive(id: int) -> ValidationReport[int]:
        if id < 1:
            return ValidationReport.send_failed_valtidation_report(
                IdPositiveValidationFailed(IdPositiveValidationFailed.default_message)
            )
        return ValidationReport(payload=id)


    @staticmethod
    def id_exists(id: int) -> ValidationReport[int]:

        if id is None:
            return ValidationReport.send_failed_valtidation_report(
                IdNotNullValidationFailed("Failed id exists validation test")
            )
        return ValidationReport.send_passed_validation_report(payload=id)
