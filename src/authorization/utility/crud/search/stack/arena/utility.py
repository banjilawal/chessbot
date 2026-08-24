# src/authorization/utility/crud/search/stack/arena/utility.py

"""
Module: authorization.utility.crud.search.stack.arena.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import ContextValidator, ArenaContextValidator
from authorization import SearchPermissionUtility
from domain import ArenaSearchContext


@dataclass
class ArenaSearchPermissionUtility(SearchPermissionUtility[ArenaSearchContext]):
    """
    Role:
        -   Toolkit

    Responsibilities:
        1.  Bundles resources the ArenaSearchAuthorizer needs to evaluate a ArenaSearchRequest..

    Attributes:
        validator: Dict[str, ContextValidator]
        arena_context_validator: ArenaContextValidator
        
    Provides:

    Super Class:
        SearchPermissionUtility
    """
    validator: Dict[str, ContextValidator] = field(
        default_factory=lambda: {
            "arena_context_validator": ArenaContextValidator(),
        }
    )
    
    @property
    def arena_context_validator(self) -> ArenaContextValidator:
        return self.resources["arena_context_validator"]

    