# src/chess/system/service/menu/route/route.py

"""
Module: chess.system.service.menu.route.route
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from chess.system import Command, LoggingLevelRouter, AbstractService

S = TypeVar("S", bound="AbstractService")

class CommandRouter(ABC, Generic[S]):
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def route(self, command: Command) -> Any:
        pass
        
    
    