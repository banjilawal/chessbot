# src/command/system/service/operation/build/builder.py

"""
Module: command.system.service.operation.build.builder
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import Any, Dict

from command import Command, CommandBuildException, NullArgumentsException
from logic.system import BuildResult, Builder, IdFactory, IdentityService, LoggingLevelRouter, Service


class CommandBuilder(Builder[Command]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            name: str,
            server: Service,
            parameters: Dict[str, Any] = Dict[str, Any],
            id: int = IdFactory.next_id(class_name="Command"),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[Command]:
        method = "CommandBuilder.build"
        
        # Handle the case that, the request does not pass a validation check.
        identity_validation_result = identity_service.validate_identity(
            id_candidate=id,
            name_candidate=name,
        )
        if identity_validation_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                CommandBuildException(
                    err_code=CommandBuildException.ERR_CODE,
                    msg=CommandBuildException.MSG,
                    mthd=CommandBuildException.MTHD,
                    op=CommandBuildException.OP,
                    ex=identity_validation_result.exception
                )
            )
        
        # Handle the case that, the parameters is not a dictionary.
        if parameters is None:
            # Return the exception on failure.
            return BuildResult.failure(
                CommandBuildException(
                    err_code=CommandBuildException.ERR_CODE,
                    msg=CommandBuildException.MSG,
                    mthd=CommandBuildException.MTHD,
                    op=CommandBuildException.OP,
                    ex=NullArgumentsException(
                        err_code=NullArgumentsException.ERR_CODE,
                        msg=NullArgumentsException.MSG,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(parameters, Dict):
            # Return the exception on failure.
            return BuildResult.failure(
                CommandBuildException(
                    err_code=CommandBuildException.ERR_CODE,
                    msg=CommandBuildException.MSG,
                    mthd=CommandBuildException.MTHD,
                    op=CommandBuildException.OP,
                    ex=TypeError(
                        f"{method}: Expected Dict, got {type(parameters).__name__} instead."
                    )
                )
            )
        # --- The Build the Command then, send the success result. ---#
        return BuildResult.success(
            Command(
                id=id,
                name=name,
                server=server,
                parameters=parameters,
            )
        )
    
    