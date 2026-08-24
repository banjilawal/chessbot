# src/authorization/utility/crud/delete/stack/square/utility.py

"""
Module: authorization.utility.crud.delete.stack.square.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackDeleteContextValidator, SquareContextValidator
from authorization import StackDeletePermissionUtility
from domain import SquareDeleteContext


@dataclass
class SquareStackDeletePermissionUtility(StackDeletePermissionUtility[SquareDeleteContext]):
    """
    Role:
        -   Utility

    Responsibilities:
        1.  Bundles resources the SquareDeleteAuthorizer needs to evaluate a SquareDeleteRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        square_context_validator: SquareContextValidator
        
    Provides:

    Super Class:
        StackDeletePermissionUtility
    """
    validator: Dict[str, StackDeleteContextValidator] = field(
        default_factory=lambda: {
            "square_context_validator": SquareContextValidator(),
        }
    )
    
    @property
    def square_context_validator(self) -> SquareContextValidator:
        return self.resources["square_context_validator"]

    