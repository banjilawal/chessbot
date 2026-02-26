# src/chess/square/service/route/route.py

"""
Module: chess.square.service.route.route
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import Any, List

from chess.square import SquareBuildCommand, SquareServiceCommand, SquareService
from chess.system import CommandRouter


class SquareServiceRouter(CommandRouter[SquareService]):
    
    COMMANDS: List[SquareServiceCommand] = [
        SquareBuildCommand, 
    ]
    
    _service: SquareService
    _commands: List[SquareServiceCommand]
    
    def __init__(self,
            service: SquareService = SquareService(),
            commands: List[SquareServiceCommand] = None,
    ):
        _commands = commands or self.COMMANDS
        self._service = service
        self._commands = commands
        
    @property
    def commands(self) -> List[SquareServiceCommand]:
        return self._commands
    
    def route(self, command: SquareServiceCommand) -> Any:
        pass
    