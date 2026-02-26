# src/chess/system/service/menu/route/route.py

"""
Module: chess.system.service.menu.route.route
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, List, TypeVar

from chess.system import Command, LoggingLevelRouter, Service

S = TypeVar("S", bound="Service")

class CommandRouter(ABC, Generic[S]):
    _service: S
    _commands: List[Command]
    
    def __init__(self, service: Service, commands: List[Command]):
        self._service = service
        self._commands = commands
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def route(self, command: Command) -> Any:
        pass
        
    
    