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
        Before the OperationValidator checks that the fields match Command.key

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
                    err_code=ServiceRequestValidationException.ERR_CODE,
                    msg=ServiceRequestValidationException.MSG,
                    mthd=ServiceRequestValidationException.MTHD,
                   ex=ServiceRequestNullException(
                        var="candidate",
                        val=None,
                        err_code=ServiceRequestNullException.ERR_CODE,
                        msg=ServiceRequestNullException.MSG
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, ServiceRequest):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ServiceRequestValidationException(
                    err_code=ServiceRequestValidationException.ERR_CODE,
                    msg=ServiceRequestValidationException.MSG,
                    mthd=ServiceRequestValidationException.MTHD,
                    ex=TypeError(
                        f"{method}: Expected ServiceRequest, but, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast candidate to a ServiceRequest for additional tests. ---#
        request = cast(ServiceRequest, candidate)
        
        # Handle the case that, the request.operation is not a string.
        identity_validation = identity_service.validate_name(request.command_name)
        # Return the exception chain on failure.
        if identity_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ServiceRequestValidationException(
                    err_code=ServiceRequestValidationException.ERR_CODE,
                    msg=ServiceRequestValidationException.MSG,
                    mthd=ServiceRequestValidationException.MTHD,
                    ex=identity_validation.exception
                )
            )
        # Handle the case that, request.arguments is not a Dict.
        if not isinstance(candidate, ServiceRequest):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ServiceRequestValidationException(
                    err_code=ServiceRequestValidationException.ERR_CODE,
                    msg=ServiceRequestValidationException.MSG,
                    mthd=ServiceRequestValidationException.MTHD,
                    ex=TypeError(
                        f"ServiceRequest.arguments type is not Dict[str, Any]. "
                    )
                )
            )
        # --- On certification successes send the request in the ValidationResult. ---#
        return ValidationResult.success(payload=request)