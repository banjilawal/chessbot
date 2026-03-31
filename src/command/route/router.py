# src/command/route/route.py

"""
Module: command.route.route
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, TypeVar

from command import Command
from logic.system import LoggingLevelRouter, Router

S = TypeVar("S")

class CommandRouter(Router[Command]):
    """
    Role:Interface, Routing, Worker

    Responsibilities:
    1.  Route commands a command to the service's appropriate method.

    Super Class:
    None

    Provides:


    # INHERITED ATTRIBUTES:
    None.

    Attributes:
    None

    # LOCAL METHODS:
        *   route(command: Command) -> Any:

    # INHERITED METHODS:
    None
    """
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def route(self, command: Command) -> Any:
        pass
        
    
    