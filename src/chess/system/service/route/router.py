# src/chess/system/service/menu/route/route.py

"""
Module: chess.system.service.menu.route.route
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List

from chess.system import Command, LoggingLevelRouter, Service


class CommandRouter(ABC, Service):
    _service: Service
    _commands: List[Command]
    
    def __init__(self, service: Service, commands: List[Command]):
        self._service = service
        self._commands = commands
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def route(self, service_request: ServiceRequest) -> Any:
        pass
        
    
    