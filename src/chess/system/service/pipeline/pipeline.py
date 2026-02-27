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
    # ROLE: Pipeline

    # RESPONSIBILITIES:
    1.  Pipeline commands a command to the service's appropriate method.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   router: (CommandRouter[S])
        *   builder: (Builder[Command])
        *   request_validator: (TypeRequestValidator)

    # INHERITED ATTRIBUTES:
    None.

    # CONSTRUCTOR PARAMETERS:)
        *   router: (CommandRouter[S])
        *   builder: (Builder[Command])
        *   request_validator: (TypeRequestValidator)

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _router: CommandRouter[S]
    _builder: Builder[Command]
    _request_validator: TypeRequestValidator
    
    def __init__(
            self,
            router: CommandRouter[S],
            builder: Builder[Command],
            request_validator: TypeRequestValidator = TypeRequestValidator(),
    ):
        self._router = router
        self._builder = builder
        self._request_validator = request_validator

    @property
    def router(self) -> CommandRouter[S]:
        return self._router
    
    @property
    def builder(self) -> Builder[Command]:
        return self._builder
    
    @property
    def request_validator(self) -> TypeRequestValidator:
        return self._request_validator