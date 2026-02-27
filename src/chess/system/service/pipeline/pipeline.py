# src/chess/system/service/pipeline/pipeline.py

"""
Module: chess.system.service.pipeline.pipeline
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from chess.system import Builder, Command, CommandRouter

S = TypeVar("S")


class CommandPipeline(ABC, Generic[S]):
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
        *   request_validator: (TypeRequestValidator)

    # INHERITED ATTRIBUTES:
    None.

    # CONSTRUCTOR PARAMETERS:)
        *   builder: (Builder[Command])
        *   request_validator: (TypeRequestValidator)

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _builder: Builder[Command]
    _request_validator: TypeRequestValidator
    
    def __init__(
            self,
            builder: Builder[Command],
            request_validator: TypeRequestValidator = TypeRequestValidator(),
    ):
        self._builder = builder
        self._request_validator = request_validator

    @property
    def builder(self) -> Builder[Command]:
        return self._builder
    
    @property
    def request_validator(self) -> TypeRequestValidator:
        return self._request_validator