# src/chess/system/command/request/validator/validator.py

"""
Module: chess.system.command.request.validator.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Any, cast

from chess.system import (
    IdentityService, LoggingLevelRouter, NullArgumentsException, ServiceRequestNullException,
    ServiceRequestValidationException, ValidationResult, Validator, ServiceRequest
)

class ServiceRequestValidator(Validator[ServiceRequest]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a ServiceRequest has.
            *   The correct number of arguments.
            *   The arguments have the correct names.
            *   The correct types.

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
                candidate: ServiceRequest,
                key: Command,
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
        """
        # ACTION:
            1.  If the candidate fails either:
                    *   existence
                    *   type
                tests send an exception chain in the ValidationResult. Else, cast to ServiceRequest
                instance, request.
            2.  Use identity_service does not verify request.command_name is a valid str. Send an
                exception chain in th ValidationResult.
            3.  If the request.arguments is either
                    *   Null
                    *   Not a Dict[str, Any]
                Send an exception chain in the ValidationResult.
            4.  All the tests for ServiceRequestType are passed, return the success result.
        # PARAMETERS:
            *   candidate (Any)
            *   identity_service (IdentityService)
        # RETURNS:
            *   ValidationResult[ServiceRequest] containing either:
                    - On failure: Exception.
                    - On success: ServiceRequest in the payload.
        # RAISES:
            *   TypeError
            *   NullArgumentsException
            *   NullServiceRequestException
            *   ServiceRequestValidationException
        """
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
                        f"{method}: Expected ServiceRequest, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast candidate to a ServiceRequest for additional tests. ---#
        request = cast(ServiceRequest, candidate)
        
        # Handle the case that, the request.command_name is not a string.
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
        # Handle the case that, request.arguments is null.
        if request.arguments is not None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ServiceRequestValidationException(
                    err_code=ServiceRequestValidationException.ERR_CODE,
                    msg=ServiceRequestValidationException.MSG,
                    mthd=ServiceRequestValidationException.MTHD,
                    ex=NullArgumentsException(
                        err_code=NullArgumentsException.ERR_CODE,
                        msg=NullArgumentsException.MSG
                    )
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