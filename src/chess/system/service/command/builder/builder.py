# src/chess/square/service/build/request/builder/builder.py

"""
Module: chess.square.service.build.request.builder.builder
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from chess.system import (
    ArgumentCountException, ArgumentNameException, ArgumentTypeException, Builder, Command, CommandNameException,
    LoggingLevelRouter, ServiceRequestValidator, BuildResult, ServiceRequest
)
from chess.system.service.command.builder import CommandBuilderException


class CommandBuilder(Builder[Command]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            key: Command,
            request: ServiceRequest,
            service_request_validator: ServiceRequestValidator = ServiceRequestValidator(),
    ) -> BuildResult[Command]:
        method = "CommandBuilder.build"
        
        # Handle the case that, the request is not certified as safe.
        validation_result = service_request_validator.validate(candidate=request)
        if validation_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                CommandBuilderException(
                    err_code=CommandBuilderException.ERR_CODE,
                    msg=CommandBuilderException.MSG,
                    mthd=CommandBuilderException.MTHD,
                    op=CommandBuilderException.OP,
                    ex=validation_result.exception
                )
            )
        # Handle the case that, request.command_name does not match key.name
        if request.command_name.upper() != key.name.upper():
            # Return the exception on failure.
            return BuildResult.failure(
                CommandBuilderException(
                    err_code=CommandBuilderException.ERR_CODE,
                    msg=CommandBuilderException.MSG,
                    mthd=CommandBuilderException.MTHD,
                    op=CommandBuilderException.OP,
                    ex=CommandNameException(
                        err_code=CommandNameException.ERR_CODE,
                        msg=CommandNameException.MSG,
                        var=f"{request.command_name}",
                        val=request.command_name,
                    )
                )
            )
        # Handle the case that, request has the wrong number of arguments.
        if len(request.arguments) != len(key.parameters):
            # Return the exception on failure.
            return BuildResult.failure(
                CommandBuilderException(
                    err_code=CommandBuilderException.ERR_CODE,
                    msg=CommandBuilderException.MSG,
                    mthd=CommandBuilderException.MTHD,
                    op=CommandBuilderException.OP,
                    ex=ArgumentCountException(
                        err_code=ArgumentCountException.ERR_CODE,
                        msg=ArgumentCountException.MSG,
                    )
                )
            )
        # Handle the case that, the request has an identifier wrong
        for identifier in request.arguments.keys():
            if identifier not in key.parameters.keys():
                # Return the exception on failure.
                return BuildResult.failure(
                    CommandBuilderException(
                        err_code=CommandBuilderException.ERR_CODE,
                        msg=CommandBuilderException.MSG,
                        mthd=CommandBuilderException.MTHD,
                        op=CommandBuilderException.OP,
                        ex=ArgumentNameException(
                            err_code=ArgumentNameException.ERR_CODE,
                            msg=ArgumentNameException.MSG,
                            var=f"{identifier}",
                        )
                    )
                )
        # Handle the case that, a request argument' type is wrong.
        for identifier in request.arguments.keys():
            if not isinstance(request.arguments[identifier, key.parameters[identifier]]):
                # Return the exception on failure.
                return BuildResult.failure(
                    CommandBuilderException(
                        err_code=CommandBuilderException.ERR_CODE,
                        msg=CommandBuilderException.MSG,
                        mthd=CommandBuilderException.MTHD,
                        op=CommandBuilderException.OP,
                        ex=ArgumentTypeException(
                            err_code=ArgumentTypeException.ERR_CODE,
                            msg=ArgumentTypeException.MSG,
                            var=f"{identifier}",
                            val=type(request.arguments[identifier]).__name__,
                        )
                    )
                )
        # --- The Build the Command then, send the success result. ---#
        return BuildResult.success(
            payload=Command(
                name=request.command_name,
                parameters=request.arguments
            )
        )
    
    