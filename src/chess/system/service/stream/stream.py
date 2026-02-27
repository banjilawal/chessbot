# src/chess/system/service/stream/stream.py

"""
Module: chess.system.service.stream.stream
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, List, TypeVar

from chess.system import  CommandRouter
from chess.system.service.pipeline import CommandPipeline

S = TypeVar("S")


class ServiceStream(ABC, Generic[S]):
    """
    # ROLE: Stream

    # RESPONSIBILITIES:
    1.  Collection of pipelines for the different operations the service supports.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   router (CommandRouter[S])
        *   pipelines (List[CommandPipeline])

    # INHERITED ATTRIBUTES:
    None.

    # CONSTRUCTOR PARAMETERS:)
        *   router (CommandRouter[S])
        *   pipelines (List[CommandPipeline])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _router: CommandRouter[S]
    _pipelines: List[CommandPipeline[S]]

    def __init__(
            self,
            router: CommandRouter[S],
            pipelines: List[CommandPipeline[S]],
    ):
        self._router = router
        self._pipelines = pipelines

    @property
    def router(self) -> CommandRouter[S]:
        return self._router
    
    @property
    def pipelines(self) -> List[CommandPipeline]:
        return self._pipelines