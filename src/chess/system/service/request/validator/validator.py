# src/chess/system/service/request/validator/validator.py

"""
Module: chess.system.service.request.validator.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Any, cast

from chess.system import (
    IdentityService, LoggingLevelRouter, ServiceRequestNullException, ServiceRequestValidationException,
    ValidationResult, Validator, ServiceRequest
)


class ServiceRequestValidator(Validator[ServiceRequest]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a ServiceRequest has.
            *   str
            *   Dict[str, Any]
            *   nd consistent before use.
        Before the OperationValidator checks that the fields match ServiceOperation.key

    # PARENT:
        *   Validator

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
    None

    # LOCAL METHODS:
        *   validate(
                candidate: Any,
                identity_service: IdentityService = IdentityService()
            ) -> ValidationResult[ServiceRequest]

    # INHERITED METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[ServiceRequest]:
        method = "ServiceRequestValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ServiceRequestValidationException(
                    message=f"{method}: {ServiceRequestValidationException.ERROR_CODE}",
                    ex=ServiceRequestNullException(
                        f"{method}: {ServiceRequestNullException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, ServiceRequest):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ServiceRequestValidationException(
                    message=f"{method}: {ServiceRequestValidationException.ERROR_CODE}",
                    ex=TypeError(
                        f"{method}: Expected ServiceRequest, but, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast candidate to a ServiceRequest for additional tests. ---#
        request = cast(ServiceRequest, candidate)
        
        # Handle the case that, the request.operation is not a string.
        identity_validation = identity_service.validate_name(request.operation)
        # Return the exception chain on failure.
        if identity_validation.is_failure:
            return ValidationResult.failure(
                ServiceRequestValidationException(
                    message=f"{method}: {ServiceRequestValidationException.ERROR_CODE}",
                    ex=identity_validation.exception
                )
            )
        # Handle the case that, request.arguments is not a Dict.
        if not isinstance(candidate, ServiceRequest):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ServiceRequestValidationException(
                    message=f"{method}: {ServiceRequestValidationException.ERROR_CODE}",
                    ex=TypeError(
                        f"{method}: ServiceRequest.params is type: "
                        f"{type(candidate).__name__}, instead of Dict[str, Any]."
                    )
                )
            )
        # Handle the case that, a key is not a string.
        for key in request.arguments.keys():
            if not isinstance(key, str):
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    ServiceRequestValidationException(
                        message=f"{method}: {ServiceRequestValidationException.ERROR_CODE}",
                        ex=TypeError(
                            f"{method}: A ServiceRequest.key is : {type(candidate).__name__} instead of str."
                        )
                    )
                )

        # --- On certification successes send the request in the ValidationResult. ---#
        return ValidationResult.success(payload=request)