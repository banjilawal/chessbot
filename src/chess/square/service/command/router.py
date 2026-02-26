# src/chess/square/service/route/route.py

"""
Module: chess.square.service.route.route
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import Any, List

from chess.square import SquareBuildCommand, SquareCommand, SquareService
from chess.system import CommandRouter


class SquareServiceRouter(CommandRouter[SquareService]):
    
    COMMANDS: List[SquareCommand] = [
        SquareBuildCommand, 
    ]
    
    _service: SquareService
    _commands: List[SquareCommand]
    
    def __init__(self,
            service: SquareService = SquareService(),
            commands: List[SquareCommand] = None,
    ):
        
        self._service = service
        self._commands = commands
        
    @property
    def commands(self) -> List[SquareCommand]:
        return self._commands
    
    