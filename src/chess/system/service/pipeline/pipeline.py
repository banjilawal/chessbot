# src/chess/system/service/pipeline/pipeline.py

"""
Module: chess.system.service.pipeline.pipeline
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations

from abc import ABC
from distutils.command.build import build
from typing import Generic, TypeVar
from xml.etree.ElementPath import prepare_parent

from chess.system import (
    BuildResult, Builder, Command, LoggingLevelRouter, PipelineException, ServiceRequestValidator, ValidationResult,
    ServiceRequest
)
from chess.system.service.command.builder import CommandBuilder

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
        *   builder: (Builder[Command])
        *   request_validator: (ServiceRequestValidator)

    # INHERITED ATTRIBUTES:
    None.

    # CONSTRUCTOR PARAMETERS:)
        *   builder: (Builder[Command])
        *   request_validator: (ServiceRequestValidator)

    # LOCAL METHODS:
    None

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
