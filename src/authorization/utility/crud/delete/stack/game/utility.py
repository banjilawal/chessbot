# src/authorization/utility/crud/delete/stack/game/utility.py

"""
Module: authorization.utility.crud.delete.stack.game.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackDeleteContextValidator, GameContextValidator
from authorization import StackDeletePermissionUtility
from domain import GameDeleteContext


@dataclass
class GameStackDeletePermissionUtility(StackDeletePermissionUtility[GameDeleteContext]):
    """
    Role:
        - Utility

    Responsibilities:
        1.  Bundles resources the GameDeleteAuthorizer needs to evaluate a GameDeleteRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        game_context_validator: GameContextValidator
        
    Provides:

    Super Class:
        StackDeletePermissionUtility
    """
    validator: Dict[str, StackDeleteContextValidator] = field(
        default_factory=lambda: {
            "game_context_validator": GameContextValidator(),
        }
    )
    
    @property
    def game_context_validator(self) -> GameContextValidator:
        return self.resources["game_context_validator"]

    