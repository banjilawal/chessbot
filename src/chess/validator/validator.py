from abc import ABC

from chess.validator.validation_result import ValidationResult


class Validator(ABC):

    @staticmethod
    def error(error_message: str, exception: Exception) -> ValidationResult:
        return ValidationResult.failure(error_message)

    @staticmethod
    def success():
        return ValidationResult.success()
    protected
    abstract
    Class <? > getLoggerSource();

    protected
    ValidationResult < T > error(
        String
    logMessage,
    String
    exceptionMessage,
    RuntimeException
    exception
    ) {
        AppLogger.error(getLoggerSource(), logMessage, exception);
    return ValidationResult.failure(exceptionMessage);
    }

    protected
    ValidationResult < T > success(T
    value) {
    return ValidationResult.success(value);

}
}