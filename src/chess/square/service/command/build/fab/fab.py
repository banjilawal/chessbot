# src/chess/square/service/command/build/fab/fab.py

"""
Module: chess.square.service.command.build.fab.fab
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from chess.square import SquareBuildCommand, SquareBuildCommandFabException
from chess.system import (
    BuildResult, Builder, Command, CommandNameException, LoggingLevelRouter,
    ServiceRequestArgumentsValidator
)


class SquareBuildCommandFab(Builder[Command]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            request: ServiceRequest,
            key: SquareBuildCommand = SquareBuildCommand,
            service_request_validator: ServiceRequestValidator = ServiceRequestValidator(),
            arguments_validator: ServiceRequestArgumentsValidator = ServiceRequestArgumentsValidator(),
    ) -> BuildResult[Command]:
        method = "SquareBuildCommandFab.build"
        
        # Handle the case that, the request is not certified as safe.
        validation_result = service_request_validator.validate(candidate=request)
        if validation_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                SquareBuildCommandFabException(
                    mthd=method,
                    op=SquareBuildCommandFabException.OP,
                    msg=SquareBuildCommandFabException.MSG,
                    err_code=SquareBuildCommandFabException.ERR_CODE,
                    rslt_type=SquareBuildCommandFabException.RSLT_TYPE,
                    ex=validation_result.exception,
                )
            )
        # Handle the case that, the command is incorrect.
        if request.command_name.upper() != key.name.upper():
            # Return the exception chain on failure.
            return BuildResult.failure(
                SquareBuildCommandFabException(
                    mthd=method,
                    op=SquareBuildCommandFabException.OP,
                    msg=SquareBuildCommandFabException.MSG,
                    err_code=SquareBuildCommandFabException.ERR_CODE,
                    rslt_type=SquareBuildCommandFabException.RSLT_TYPE,
                    ex=CommandNameException(
                        err_code=CommandNameException.ERR_CODE,
                        msg=f"{request.command_name}: Unknown command",
                        var=f"{request.command_name}",
                        val=request.command_name,
                    )
                )
            )
        # Handle the case that the arguments are incorrect.
        args_validation_result = arguments_validator.validate(
            key=key,
            candidate=request.arguments,
        )
        if args_validation_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                SquareBuildCommandFabException(
                    mthd=method,
                    op=SquareBuildCommandFabException.OP,
                    msg=SquareBuildCommandFabException.MSG,
                    err_code=SquareBuildCommandFabException.ERR_CODE,
                    rslt_type=SquareBuildCommandFabException.RSLT_TYPE,
                    ex=args_validation_result.exception
                )
            )
        # --- The Build the Command then, send the success result. ---#
        return BuildResult.success(
            Command(name=request.command_name, parameters=request.arguments)
        )

    
