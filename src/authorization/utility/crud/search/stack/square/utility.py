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

from assurance import ContextValidator, SquareContextValidator
from authorization import SearchPermissionUtility
from domain import SquareSearchContext


@dataclass
class SquareSearchPermissionUtility(SearchPermissionUtility[SquareSearchContext]):
    """
    Role:
        -   Toolkit

    Responsibilities:
        1.  Bundles resources the SquareSearchAuthorizer needs to evaluate a SquareSearchRequest..

    Attributes:
        validator: Dict[str, ContextValidator]
        square_context_validator: SquareContextValidator
        
    Provides:

    Super Class:
        SearchPermissionUtility
    """
    validator: Dict[str, ContextValidator] = field(
        default_factory=lambda: {
            "square_context_validator": SquareContextValidator(),
        }
    )
    
    @property
    def square_context_validator(self) -> SquareContextValidator:
        return self.resources["square_context_validator"]

    