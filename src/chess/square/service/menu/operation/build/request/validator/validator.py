# src/chess/square/service/menu/build/request/validator/validator.py

"""
Module: chess.square.service.menu.build.request.validator.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import Any, cast

from chess.square import SquareBuildOperation, SquareBuildRequestException
from chess.system import (
    IdentifierException, LoggingLevelRouter, NumberOfArgumentsException, ServiceRequest, ServiceRequestValidator,
    ValidationResult,
    Validator,
    WrongOperationException
)


class SquareBuildRequestValidator(Validator[SquareBuildOperation]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            operation: SquareBuildOperation,
            service_request_validator: ServiceRequestValidator = ServiceRequestValidator(),
    ) -> ValidationResult[SquareBuildOperation]:
        method = "SquareBuildRequestValidator.validate"
        
        # Handle the case that, the candidate is not certified as a safe ServiceRequest.
        request_validation_result = service_request_validator.validate(candidate=candidate)
        if request_validation_result.is_failure:
            # Return the exception on failure.
            return ValidationResult.failure(
                SquareBuildRequestException(
                    message=f"{method}: {SquareBuildRequestException.DEFAULT_MESSAGE}",
                    ex=request_validation_result.exception
                )
            )
        # --- Cast candidate to a ServiceRequest for additional tests. ---#
        request = cast(ServiceRequest, candidate)
        
        # Handle the case that, request.command != operation.name
        if request.command.upper() != operation.name.upper():
            # Return the exception on failure.
            return ValidationResult.failure(
                SquareBuildRequestException(
                    message=f"{method}: {SquareBuildRequestException.DEFAULT_MESSAGE}",
                    ex=WrongOperationException(
                        f"{method}: Expected command: {operation.name} received: {request.command} instead."
                    )
                )
            )
        # Handle the case that, request has the wrong number of arguments.
        if len(request.arguments) != len(operation.parameters):
            # Return the exception on failure.
            return ValidationResult.failure(
                SquareBuildRequestException(
                    message=f"{method}: {SquareBuildRequestException.DEFAULT_MESSAGE}",
                    ex=NumberOfArgumentsException(
                        f"{method}: Expected command: {NumberOfArgumentsException.DEFAULT_MESSAGE}."
                    )
                )
            )
        # Handle the case that, the request has an identifier wrong
        for identifier in request.arguments.keys():
            if identifier not in operation.parameters.keys():
                return ValidationResult.failure(
                    SquareBuildRequestException(
                        message=f"{method}: {SquareBuildRequestException.DEFAULT_MESSAGE}",
                        ex=IdentifierException(
                            f"{method}: Expected command: {identifier} not found."
                        )
                    )
                )
    