# src/authorization/utility/crud/search/stack/game/utility.py

"""
Module: authorization.utility.crud.search.stack.game.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import ContextValidator, GameContextValidator
from authorization import SearchPermissionUtility
from domain import GameSearchContext


@dataclass
class GameSearchPermissionUtility(SearchPermissionUtility[GameSearchContext]):
    """
    Role:
        -   Toolkit

    Responsibilities:
        1.  Bundles resources the GameSearchAuthorizer needs to evaluate a GameSearchRequest..

    Attributes:
        validator: Dict[str, ContextValidator]
        game_context_validator: GameContextValidator
        
    Provides:

    Super Class:
        SearchPermissionUtility
    """
    validator: Dict[str, ContextValidator] = field(
        default_factory=lambda: {
            "game_context_validator": GameContextValidator(),
        }
    )
    
    @property
    def game_context_validator(self) -> GameContextValidator:
        return self.resources["game_context_validator"]

    