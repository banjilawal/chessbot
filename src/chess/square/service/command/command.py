# src/chess/square/service/command/command.py

"""
Module: chess.square.service.command.command
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Dict

from chess.system import Command


class SquareServiceCommand(Command):
    """
    A class representing a service command.
    """
    
    def __init__(self, name: str , parameters: Dict[str, Any]):
        super().__init__(name, parameters)

    @classmethod
    @abstractmethod
    def cipher(cls) -> SquareServiceCommand:
        pass