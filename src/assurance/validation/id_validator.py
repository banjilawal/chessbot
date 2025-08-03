from assurance.validation.validation_result import ValidationResult
from assurance.validation.validation_exception import ValidationException
from chess.transaction.old_transaction_result import OldTransactionResult, Failure, StatusCode

class IdPositiveValidationFailed(ValidationException):
    default_message = "Failed id is positive validation test"

class IdNotNullValidationFailed(ValidationException):
    default_message = "Failed id exsts validation test"

class IdValidator:

    @staticmethod
    def test_id_positive(id: int) -> ValidationResult[int]:
        if id < 1:
            return ValidationResult.send_failed_valtidation_report(
                IdPositiveValidationFailed(IdPositiveValidationFailed.default_message)
            )
        return ValidationResult(payload=id)


    @staticmethod
    def id_exists(id: int) -> ValidationResult[int]:

        if id is None:
            return ValidationResult.send_failed_valtidation_report(
                IdNotNullValidationFailed("Failed id exists validation test")
            )
        return ValidationResult.send_passed_validation_report(payload=id)
