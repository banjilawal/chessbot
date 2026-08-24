# src/authorization/utility/crud/insert/stack/game/utility.py

"""
Module: authorization.utility.crud.insert.stack.game.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackInsertContextValidator, GameContextValidator
from authorization import StackInsertPermissionUtility
from domain import GameInsertContext


@dataclass
class GameStackInsertPermissionUtility(StackInsertPermissionUtility[GameInsertContext]):
    """
    Role:
        -   Utility

    Responsibilities:
        1.  Bundles resources the GameInsertAuthorizer needs to evaluate a GameInsertRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        game_context_validator: GameContextValidator
        
    Provides:

    Super Class:
        StackInsertPermissionUtility
    """
    validator: Dict[str, StackInsertContextValidator] = field(
        default_factory=lambda: {
            "game_context_validator": GameContextValidator(),
        }
    )
    
    @property
    def game_context_validator(self) -> GameContextValidator:
        return self.resources["game_context_validator"]

    