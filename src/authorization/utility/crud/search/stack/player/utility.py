# src/authorization/utility/crud/search/stack/square/utility.py

"""
Module: authorization.utility.crud.search.stack.square.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackSearchContextValidator, SquareContextValidator
from authorization import StackSearchPermissionUtility
from domain import SquareSearchSearchContext


@dataclass
class SquareStackSearchPermissionUtility(StackSearchPermissionUtility[SquareSearchSearchContext]):
    """
    Role:
        - Utility

    Responsibilities:
        1.  Bundles resources the SquareSearchAuthorizer needs to evaluate a SquareSearchRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        square_context_validator: SquareContextValidator
        
    Provides:

    Super Class:
        StackSearchPermissionUtility
    """
    validator: Dict[str, StackSearchContextValidator] = field(
        default_factory=lambda: {
            "square_context_validator": SquareContextValidator(),
        }
    )
    
    @property
    def square_context_validator(self) -> SquareContextValidator:
        return self.resources["square_context_validator"]

    