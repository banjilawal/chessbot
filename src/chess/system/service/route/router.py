# src/chess/system/service/menu/route/route.py

"""
Module: chess.system.service.menu.route.route
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from chess.system import LoggingLevelRouter
from chess.system.service.pipeline import CommandPipeline

S = TypeVar("S")

class CommandRouter(ABC, Generic[S]):
    """
    # ROLE: Interface, Routing, Worker

    # RESPONSIBILITIES:
    1.  Route commands a command to the service's appropriate method.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None.

    # CONSTRUCTOR PARAMETERS:)
    None

    # LOCAL METHODS:
        *   route(command: Command) -> Any:

    # INHERITED METHODS:
    None
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def route(self, pipeline: CommandPipeline) -> Any:
        pass
        
    
    