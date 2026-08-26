# src/authorization/utility/crud/delete/stack/arena/utility.py

"""
Module: authorization.utility.crud.delete.stack.arena.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackDeleteContextValidator, ArenaContextValidator
from authorization import StackDeletePermissionUtility
from domain import ArenaDeleteContext


@dataclass
class ArenaStackDeletePermissionUtility(StackDeletePermissionUtility[ArenaDeleteContext]):
    """
    Role:
        -  Utility

    Responsibilities:
        1.  Bundles resources the ArenaDeleteAuthorizer needs to evaluate a ArenaDeleteRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        arena_context_validator: ArenaContextValidator
        
    Provides:

    Super Class:
        StackDeletePermissionUtility
    """
    validator: Dict[str, StackDeleteContextValidator] = field(
        default_factory=lambda: {
            "arena_context_validator": ArenaContextValidator(),
        }
    )
    
    @property
    def arena_context_validator(self) -> ArenaContextValidator:
        return self.resources["arena_context_validator"]

    