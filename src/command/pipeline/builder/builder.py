# src/command/command/build/request/builder/builder.py

"""
Module: command.command.build.request.builder.builder
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from chess.system import (
    ArgumentCountException, ArgumentNameException, ArgumentTypeException, Builder, Command, CommandBuilderException,
    CommandNameException, LoggingLevelRouter, RequestValidator, BuildResult, Request
)


class CommandBuilder(Builder[Command]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            cipher: Command,
            request: Request,
            request_validator: RequestValidator = RequestValidator(),
    ) -> BuildResult[Command]:
        method = "CommandBuilder.build"
        
        # Handle the case that, the request is not certified as safe.
        validation_result = request_validator.validate(candidate=request)
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
        if request.command_name.upper() != cipher.name.upper():
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
        if len(request.arguments) != len(cipher.parameters):
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
            if identifier not in cipher.parameters.keys():
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
            if not isinstance(
                    type(request.arguments[identifier]),
                    type(cipher.parameters[identifier])
            ):
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
        return BuildResult.success(Command(name=request.command_name, parameters=request.arguments))
    
    