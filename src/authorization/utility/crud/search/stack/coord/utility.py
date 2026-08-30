# src/authorization/utility/crud/search/stack/coord/utility.py

"""
Module: authorization.utility.crud.search.stack.coord.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackContextValidator, CoordContextValidator
from authorization import StackSearchPermissionUtility
from domain import CoordSearchContext


@dataclass
class CoordStackSearchPermissionUtility(StackSearchPermissionUtility[CoordSearchContext]):
    """
    Role:
        - Utility

    Responsibilities:
        1.  Bundles resources the CoordSearchAuthorizer needs to evaluate a CoordSearchRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        coord_context_validator: CoordContextValidator
        
    Provides:

    Super Class:
        StackSearchPermissionUtility
    """
    validator: Dict[str, StackContextValidator] = field(
        default_factory=lambda: {
            "coord_context_validator": CoordContextValidator(),
        }
    )
    
    @property
    def coord_context_validator(self) -> CoordContextValidator:
        return self.resources["coord_context_validator"]

    