# src/command/command/pipeline/pipeline.py

"""
Module: command.command.pipeline.pipeline
Author: Banji Lawal
Created: 2026-02-25
"""

from __future__ import annotations

from abc import ABC
from time import process_time
from typing import Any, Dict, Generic, TypeVar


from logic.system import (
    BuildResult, Command, CommandService, IdentityService, LoggingLevelRouter, PipelineException,
    RequestService,
    Request, ValidationResult
)

C = TypeVar("C", bound=Command)

class CommandPipeline(ABC, Generic[C]):
    """
    # ROLE: Pipeline, Integrity Lifecycle Manager. Worker

    # RESPONSIBILITIES:
    1.  Integrity Lifecycle of a Command.
            *   Validating a Request object.
            *   Building a Command instance from the Request.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   cipher: (C)
        *   builder: (Builder[Command])
        *   request_validator: (ServiceRequestValidator)

    # INHERITED ATTRIBUTES:
    None.

    # CONSTRUCTOR PARAMETERS:)
        *   cipher: (C)
        *   builder: (Builder[Command])
        *   request_validator: (ServiceRequestValidator)

    # LOCAL METHODS:
        *   process_service_request(request: Request) -> BuildResult[C]

    # INHERITED METHODS:
    None
    """
    PIPELINE_NAME = "CommandPipeline"
    _id: int
    _name: str
    _cipher: C
    _command_service: CommandService
    _request_service: RequestService
    
    def __init__(
            self,
            id: int,
            cipher: C,
            name: str,
            command_service: CommandService = CommandService(),
            request_service: RequestService = RequestService(),
    ):
        self._id = id
        self._name = name
        self._cipher = cipher
        self._command_service= command_service
        self._request_validator = request_service
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
        
    @property
    def cipher(self) -> C:
        return self._cipher
    
    @property
    def command_service(self) -> CommandService:
        return self._command_service
    
    @property
    def request_service(self) -> RequestService:
        return self._request_service
    
    def build_request(self, command_name: str, arguments: Dict[str, Any]) -> BuildResult[Request]:
        method = "CommandPipeline.build_request"
        
        # Handle the case that the
        build_result = self._request_service.builder.build(
            command_name=command_name,
            arguments=arguments
        )
        if build_result.is_failure:
            # Return the exception chain on failure
            return BuildResult.failure(
                PipelineException(
                    err_code=PipelineException.ERR_CODE,
                    msg=PipelineException.MSG,
                    cls_name=type(self).__name__,
                    cls_mthd=method,
                    ex=build_result.exception,
                )
            )
        # --- Send the success result to command_service ---#
        return BuildResult.success(build_result.payload)
    
    def _build_command(self, request: Request) -> BuildResult[C]:
        method = "CommandPipeline._build_command"
        
        build_result = self._command_service.builder.build(request=request)
        
        # Handle the case that, the command is not created.
        command_build_result = self._command_service.builder.build(
            request=request,
            cipher=self._cipher,
            request_validator=self._request_service.validator,
        )
    
        if build_result.is_failure:
            # Return the exception chain on failure
            return BuildResult.failure(
                PipelineException(
                    err_code=PipelineException.ERR_CODE,
                    msg=PipelineException.MSG,
                    cls_name=type(self).__name__,
                    cls_mthd=method,
                    ex=build_result.exception,
                )
            )
        # --- Send the success result to command_service ---#
        return BuildResult.success(build_result.payload)
