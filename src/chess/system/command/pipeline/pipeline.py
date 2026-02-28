# src/chess/system/service/pipeline/pipeline.py

"""
Module: chess.system.service.pipeline.pipeline
Author: Banji Lawal
Created: 2026-02-25
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar


from chess.system import (
    BuildResult, Command, CommandBuilder, LoggingLevelRouter, PipelineException, ServiceRequestValidator,
    ServiceRequest
)

C = TypeVar("C", bound=Command)

class CommandPipeline(ABC, Generic[C]):
    """
    # ROLE: Pipeline, Integrity Lifecycle Manager. Worker

    # RESPONSIBILITIES:
    1.  Integrity Lifecycle of a Command.
            *   Validating a ServiceRequest object.
            *   Building a Command instance from the ServiceRequest.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   key: (C)
        *   builder: (Builder[Command])
        *   request_validator: (ServiceRequestValidator)

    # INHERITED ATTRIBUTES:
    None.

    # CONSTRUCTOR PARAMETERS:)
        *   key: (C)
        *   builder: (Builder[Command])
        *   request_validator: (ServiceRequestValidator)

    # LOCAL METHODS:
        *   process_service_request(request: ServiceRequest) -> BuildResult[C]

    # INHERITED METHODS:
    None
    """
    _key: C
    _builder: CommandBuilder
    _request_validator: ServiceRequestValidator
    
    def __init__(
            self,
            key: C,
            builder: CommandBuilder = CommandBuilder(),
            request_validator: ServiceRequestValidator = ServiceRequestValidator(),
    ):
        self._key = key
        self._builder = builder
        self._request_validator = request_validator
        
    @property
    def key(self) -> C:
        return self._key
        
    @LoggingLevelRouter.monitor
    def process_service_request(self, request: ServiceRequest) -> BuildResult[C]:
        method_name = "CommandPipeline.process_service_request"
        
        # Handle the case that, the request is not certified as safe.
        validation_result = self._request_validator.validate(candidate=request)
        # Return the exception chain on failure.
        if validation_result.is_failure:
            return BuildResult.failure(
                PipelineException(
                    err_code=PipelineException.ERR_CODE,
                    msg=PipelineException.MSG,
                    cls_name=type(self).__name__,
                    cls_mthd=method_name,
                    ex=validation_result.exception,
                )
            )
        # Handle the case that, the command was not built.
        build_result = self._builder.build(key=self._key, request=request)
        # Return the exception chain on failure.
        if validation_result.is_failure:
            return BuildResult.failure(
                PipelineException(
                    err_code=PipelineException.ERR_CODE,
                    msg=PipelineException.MSG,
                    cls_name=type(self).__name__,
                    cls_mthd=method_name,
                    ex=build_result.exception,
                )
            )
        # --- Forward the success result. ---#
        return build_result
