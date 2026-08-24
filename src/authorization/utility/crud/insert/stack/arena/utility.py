# src/authorization/utility/crud/insert/stack/arena/utility.py

"""
Module: authorization.utility.crud.insert.stack.arena.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackInsertContextValidator, ArenaContextValidator
from authorization import StackInsertPermissionUtility
from domain import ArenaInsertContext


@dataclass
class ArenaStackInsertPermissionUtility(StackInsertPermissionUtility[ArenaInsertContext]):
    """
    Role:
        -   Utility

    Responsibilities:
        1.  Bundles resources the ArenaInsertAuthorizer needs to evaluate a ArenaInsertRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        arena_context_validator: ArenaContextValidator
        
    Provides:

    Super Class:
        StackInsertPermissionUtility
    """
    validator: Dict[str, StackInsertContextValidator] = field(
        default_factory=lambda: {
            "arena_context_validator": ArenaContextValidator(),
        }
    )
    
    @property
    def arena_context_validator(self) -> ArenaContextValidator:
        return self.resources["arena_context_validator"]

    