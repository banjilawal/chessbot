from assurance.validators.obsolete.validation_result import ValidationResult
from assurance.exception.validation.base_validationpy import ValidationException


class IdPositiveValidationFailed(ValidationException):
    DEFAULT_MESSAGE = "Failed id is positive validators test"

class IdNotNullValidationFailed(ValidationException):
    DEFAULT_MESSAGE = "Failed id exsts validators test"

class ObsoleteIdValidator:

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
                IdNotNullValidationFailed("Failed id exists validators test")
            )
        return ValidationResult.send_passed_validation_report(payload=id)

    @classmethod
    def is_valid(cls, id):
        pass
