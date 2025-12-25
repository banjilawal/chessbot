from typing import Any, cast

from chess.system import LoggingLevelRouter, Service, ValidationResult, Validator


class ServiceValidator(Validator[Service]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a candidate is not null and the correct type before its used as a Service.
    2.  If verification fails indicate the reason in an exception returned to the caller.

    # PARENT:
        *   Validator

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any, expected_service: Service = Service) -> ValidationResult[Service]:
        """
        # ACTION:.
            1.  If the candidate passes existence and type checks cast into a Service instance and return
                in the ValidationResult. Else return an exception in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
        # RETURNS:
            *   ValidationResult[Service] containing either:
                    - On failure: Exception.
                    - On success: Service in the payload.
        # RAISES:
            *   TypeError
            *   NullServiceException
            *   ServiceValidationFailedException
        """
        method = "ServiceValidator.validate"
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ServiceValidationFailedException(
                    message=f"{method}: {ServiceValidationFailedException.ERROR_CODE}",
                    ex=NullServiceException(f"{method} {NullServiceException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, expected_class):
            # Return the exception chain on failure
            return ValidationResult.failure(
                ServiceValidationFailedException(
                    message=f"{method}: {ServiceValidationFailedException.ERROR_CODE}",
                    ex=TypeError(f"{method} Expected a {type(expected_service).__name__}, got {type(candidate).__name__} instead.")
                )
            )
        # On certification success return the service instance in a ValidationResult.
        return ValidationResult.success(payload=cast(expected_service, candidate))
    
    @classmethod
    def _validate_builder(cls, candidate: Any):
        pass
    
    @classmethod
    def _validate_validator(cls, candidate: Any):
        pass