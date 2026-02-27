# src/chess/square/service/build/request/builder/builder.py

"""
Module: chess.square.service.build.request.builder.builder
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import Any, cast

from chess.square import SquareBuildCommand, SquareBuildCommandFabException
from chess.system import (
    ArgumentCountException, ArgumentNameException, Builder, ServiceRequestValidator,
    ValidationResult
)


class SquareBuildCommandFab(Builder[SquareBuildCommand]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            request: ServiceRequest,
            key: SquareBuildCommand = SquareBuildCommand().key(),
            service_request_validator: ServiceRequestValidator = ServiceRequestValidator(),
    ) -> ValidationResult[SquareBuildCommand]:
        method = "SquareBuildFab.validate"
        
        # Handle the case that, the candidate is not certified as a safe ServiceRequest.
        validation_result = service_request_validator.validate(candidate=request)
        if validation_result.is_failure:
            # Return the exception on failure.
            return ValidationResult.failure(
                SquareBuildCommandFabException(
                    err_code=SquareBuildCommandFabException.ERR_CODE,
                    msg=SquareBuildCommandFabException.MSG,
                    mthd=SquareBuildCommandFabException.MTHD,
                    op=SquareBuildCommandFabException.OP,
                    ex=validation_result.exception
                )
            )
        
        # Handle the case that, request.command != command.name
        if request.command_name.upper() != key.name:
            # Return the exception on failure.
            return ValidationResult.failure(
                SquareBuildCommandFabException(
                    err_code=SquareBuildCommandFabException.ERR_CODE,
                    msg=SquareBuildCommandFabException.MSG,
                    mthd=SquareBuildCommandFabException.MTHD,
                    op=SquareBuildCommandFabException.OP,
                    ex=ArgumentNameException(
                        var=""
                    )
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
                SquareBuildCommandFabException(
                    msg=f"{method}: {SquareBuildCommandFabException.MSG}",
                    ex=ArgumentCountException(
                        f"{method}: Expected command: {ArgumentCountException.MSG}."
                    )
                )
            )
        # Handle the case that, the request has an identifier wrong
        for identifier in request.arguments.keys():
            if identifier not in command.parameters.keys():
                return ValidationResult.failure(
                    SquareBuildCommandFabException(
                        msg=f"{method}: {SquareBuildCommandFabException.MSG}",
                        ex=ArgumentNameException(
                            f"{method}: Expected command: {identifier} not found."
                        )
                    )
                )
        # Handle the case that, the request has an incorrect type.
        for identifier in request.arguments.keys():
            if not isinstance(request.arguments[identifier, command.key()[identifier]]):
                return ValidationResult.failure(
                    SquareBuildCommandFabException(
                        cls_name="",
                        msg=f"{method}: {SquareBuildCommandFabException.MSG}",
                        ex=ArgumentNameException(
                            var="identifier",
                            val=type(identifier).__name__,
                            msg=(
                                f"{key.name} expected {key.parameters[identifier].type.__name__} but "
                                f"received {type(identifier).__name__} instead."
                            )
                        )
                    )
                )
        # --- On certification successes send the square in the ValidationResult. ---#
        return ValidationResult.success(request)
    
    