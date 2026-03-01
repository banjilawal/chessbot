# src/command/request/builder/builder.py

"""
Module: command.request.builder.builder
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import Any, Dict

from chess.system import (
    BuildResult, Builder, IdentityService, LoggingLevelRouter, NullArgumentsException, Request, RequestBuildException
)


class RequestBuilder(Builder[Request]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            name: str,
            arguments: Dict[str: Any],
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[Request]:
        method = "RequestBuild.build"
        
        # Handle the case that, the name is not certified as safe.
        name_validation_result = identity_service.validate_name(candidate=name)
        # Return the exception chain on failure.
        if name_validation_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                RequestBuildException(
                    mthd=method,
                    op=RequestBuildException.OP,
                    msg=RequestBuildException.MSG,
                    err_code=RequestBuildException.ERR_CODE,
                    rslt_type=RequestBuildException.RSLT_TYPE,
                    ex=name_validation_result.exception
                )
            )
        # Handle the case that, arguments is null.
        if arguments is None:
            # Return the exception chain on failure.
            return BuildResult.failure(
                RequestBuildException(
                    mthd=method,
                    op=RequestBuildException.OP,
                    msg=RequestBuildException.MSG,
                    err_code=RequestBuildException.ERR_CODE,
                    rslt_type=RequestBuildException.RSLT_TYPE,
                    ex=NullArgumentsException(
                        err_code=NullArgumentsException.ERR_CODE,
                        msg=NullArgumentsException.MSG
                    )
                )
            )
        # Handle the case that, arguments is not a Dict.
        if not isinstance(arguments, Dict):
            # Return the exception chain on failure.
            return BuildResult.failure(
                RequestBuildException(
                    mthd=method,
                    op=RequestBuildException.OP,
                    msg=RequestBuildException.MSG,
                    err_code=RequestBuildException.ERR_CODE,
                    rslt_type=RequestBuildException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected Dict[str, Any], got {type(arguments).__name__}. instead."
                    )
                )
            )
        # --- On certification successes send the request in the ValidationResult. ---#
        return BuildResult.success(Request(command_name=name, arguments=arguments))
    
    