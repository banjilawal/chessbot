# src/chess/system/service/validator/validator.py

"""
Module: chess.system.service.validator.validator
Author: Banji Lawal
Created: 2025-11-18
"""

from typing import Any, cast

from chess.system import (
    Builder, EntityService, LoggingLevelRouter, NullServiceException, Service, ServiceValidationException,
    ValidationResult, Validator
)
from chess.system.service.validator.exception.null.builder import ServiceNullBuilderException
from chess.system.service.validator.exception.null.validator import ServiceNullValidatorException


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
    def validate(cls, candidate: Any, expected_service: EntityService = type[EntityService]) -> ValidationResult[Service]:
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
            *   ServiceValidationException
        """
        method = "ServiceValidator.validate"
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ServiceValidationException(
                    message=f"{method}: {ServiceValidationException.ERROR_CODE}",
                    ex=NullServiceException(f"{method} {NullServiceException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, expected_service):
            # Return the exception chain on failure
            return ValidationResult.failure(
                ServiceValidationException(
                    message=f"{method}: {ServiceValidationException.ERROR_CODE}",
                    ex=TypeError(f"{method} Expected a {type(expected_service).__name__}, got {type(candidate).__name__} instead.")
                )
            )
        
        service = cast(EntityService, candidate)
        builder_validation = cls._validate_builder(service.entity_builder)
        # On certification success return the service instance in a ValidationResult.
        return ValidationResult.success(payload=cast(expected_service, candidate))
    
    @classmethod
    def _validate_builder(cls, candidate: Any):
        method = "ServiceValidator._validate_builder"
        if candidate is None:
            return ValidationResult(
                ServiceValidationException(
                    message=f"{method}: {ServiceValidationException.ERROR_CODE}",
                    ex=ServiceNullBuilderException(f"{method}: {ServiceNullBuilderException.DEFAULT_MESSAGE}")
                )
            )
        if not isinstance(candidate, Builder):
            return ValidationResult(
                ServiceValidationException(
                    message=f"{method}: {ServiceValidationException.ERROR_CODE}",
                    ex=TypeError(f"{method}: Expected Builder, got {type(candidate).__name__} instead.")
                )
            )
        return ValidationResult.success(payload=(cast(Builder, candidate)))
    
    @classmethod
    def _validate_validator(cls, candidate: Any):
        method = "ServiceValidator._validate_validator"
        if candidate is None:
            return ValidationResult(
                ServiceValidationException(
                    message=f"{method}: {ServiceValidationException.ERROR_CODE}",
                    ex=ServiceNullValidatorException(f"{method}: {ServiceNullValidatorException.DEFAULT_MESSAGE}")
                )
            )
        if not isinstance(candidate, Validator):
            return ValidationResult(
                ServiceValidationException(
                    message=f"{method}: {ServiceValidationException.ERROR_CODE}",
                    ex=TypeError(f"{method}: Expected Builder, got {type(candidate).__name__} instead.")
                )
            )
        return ValidationResult.success(payload=(cast(Validator, candidate)))