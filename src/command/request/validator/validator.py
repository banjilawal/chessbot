# src/command/request/validation/validation.py

"""
Module: command.request.validation.validation
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Any, cast

from logic.system import (
    IdentityService, LoggingLevelRouter, NullArgumentsException, NullRequestException, Validator, Request,
    RequestValidationException, ValidationResult,
)

class RequestValidator(Validator[Request]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a ServiceRequest has.
            *   The correct number of arguments.
            *   The arguments have the correct names.
            *   The correct types.

    Super Class:
        *   Validator

    Provides:


    # INHERITED ATTRIBUTES:
    None

    Attributes:
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
    ) -> ValidationResult[Request]:
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
            4.  All the tests for RequestType are passed, return the success result.
        # PARAMETERS:
            *   candidate (Any)
            *   identity_service (IdentityService)
        # RETURNS:
            *   ValidationResult[ServiceRequest] containing either:
                    - On failure: Exception.
                    - On success: ServiceRequest in the payload.
        Raises:
            *   TypeError
            *   NullArgumentsException
            *   NullRequestException
            *   RequestValidationException
        """
        method = "RequestValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RequestValidationException(
                    err_code=RequestValidationException.ERR_CODE,
                    msg=RequestValidationException.MSG,
                    mthd=RequestValidationException.MTHD,
                   ex=NullRequestException(
                        err_code=NullRequestException.ERR_CODE,
                        msg=NullRequestException.MSG
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Request):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RequestValidationException(
                    err_code=RequestValidationException.ERR_CODE,
                    msg=RequestValidationException.MSG,
                    mthd=RequestValidationException.MTHD,
                    ex=TypeError(
                        f"{method}: Expected ServiceRequest, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast candidate to a ServiceRequest for additional tests. ---#
        request = cast(Request, candidate)
        
        # Handle the case that, the request.command_name is not a string.
        identity_validation = identity_service.validate_name(request.command_name)
        # Return the exception chain on failure.
        if identity_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RequestValidationException(
                    err_code=RequestValidationException.ERR_CODE,
                    msg=RequestValidationException.MSG,
                    mthd=RequestValidationException.MTHD,
                    ex=identity_validation.exception
                )
            )
        # Handle the case that, request.arguments is null.
        if request.arguments is not None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RequestValidationException(
                    err_code=RequestValidationException.ERR_CODE,
                    msg=RequestValidationException.MSG,
                    mthd=RequestValidationException.MTHD,
                    ex=NullArgumentsException(
                        err_code=NullArgumentsException.ERR_CODE,
                        msg=NullArgumentsException.MSG
                    )
                )
            )
        # Handle the case that, request.arguments is not a Dict.
        if not isinstance(candidate, Request):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                RequestValidationException(
                    err_code=RequestValidationException.ERR_CODE,
                    msg=RequestValidationException.MSG,
                    mthd=RequestValidationException.MTHD,
                    ex=TypeError(
                        f"ServiceRequest.arguments type is not Dict[str, Any]. "
                    )
                )
            )
        # --- On certification successes send the request in the ValidationResult. ---#
        return ValidationResult.success(payload=request)