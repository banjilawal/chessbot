# src/chess/square/service/command/build/validator/validator.py

"""
Module: chess.square.service.command.build.validator.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import Any, cast

from chess.square import SquareBuildCommand, SquareBuildCommandNullException, SquareBuildCommandValidationException
from chess.system import (
    ArgumentNameException, CommandNameException, LoggingLevelRouter, ArgumentCountException,
    ServiceRequestValidator, ValidationResult, Validator, ServiceRequest
)


class SquareBuildCommandValidator(Validator[SquareBuildCommand]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            key: SquareBuildCommand = SquareBuildCommand.cipher(),
            command_validator: CommandValidator = CommandValidator(),
            request_validator: ServiceRequestValidator =ServiceRequestValidator()
    ) -> ValidationResult[SquareBuildCommand]:
        method = "SquareBuildCommandValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            return ValidationResult.failure(
                SquareBuildCommandValidationException(
                    msg=f"{method}: {SquareBuildCommandValidationException.MSG}",
                    ex=SquareBuildCommandNullException(
                        err_code=SquareBuildCommandValidationException.ERR_CODE,
                        msg=SquareBuildCommandValidationException.MSG,
                    )
                )
            )
        
        
        if request_validation_result.is_failure:
            # Return the exception on failure.
            return ValidationResult.failure(
                SquareBuildCommandValidationException(
                    msg=f"{method}: {SquareBuildCommandValidationException.MSG}",
                    ex=request_validation_result.exception
                )
            )
        # --- Cast candidate to a ServiceRequest for additional tests. ---#
        request = cast(ServiceRequest, candidate)
        
        # Handle the case that, request.command != command.name
        if request.command.upper() != command.name.upper():
            # Return the exception on failure.
            return ValidationResult.failure(
                SquareBuildCommandValidationException(
                    
                    msg=f"{method}: {SquareBuildCommandValidationException.MSG}",
                    ex=
                    # ex=CommandNameException(
                    #     var="request.command_name",
                    #     val=request.command_name,
                    #     msg=(
                    #         f"{method}: Expected command: {command.name} received: {request.command} instead."
                    #     )
                    # )
                )
            )
        # Handle the case that, request has the wrong number of arguments.
        if len(request.arguments) != len(command.parameters):
            # Return the exception on failure.
            return ValidationResult.failure(
                SquareBuildCommandValidationException(
                    msg=f"{method}: {SquareBuildCommandValidationException.MSG}",
                    ex=ArgumentCountException(
                        f"{method}: Expected command: {ArgumentCountException.MSG}."
                    )
                )
            )
        # Handle the case that, the request has an identifier wrong
        for identifier in request.arguments.keys():
            if identifier not in command.parameters.keys():
                return ValidationResult.failure(
                    SquareBuildCommandValidationException(
                        msg=f"{method}: {SquareBuildCommandValidationException.MSG}",
                        ex=ArgumentNameException(
                            f"{method}: Expected command: {identifier} not found."
                        )
                    )
                )
        # Handle the case that, the request has an incorrect type.
        for identifier in request.arguments.keys():
            if not isinstance(request.arguments[identifier, command.cipher()[identifier]]):
                return ValidationResult.failure(
                    SquareBuildCommandValidationException(
                        msg=f"{method}: {SquareBuildCommandValidationException.MSG}",
                        ex=ArgumentNameException(
                            f"{identifier: Expected command: {identifier} not found."
                        )
                    )
                )
        # --- On certification successes send the square in the ValidationResult. ---#
        return ValidationResult.success(request)
    
    