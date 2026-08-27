# src/authorization/utility/crud/delete/stack/coord/utility.py

"""
Module: authorization.utility.crud.delete.stack.coord.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackDeleteContextValidator, CoordContextValidator
from authorization import StackDeletePermissionUtility
from domain import CoordDeleteContext


@dataclass
class CoordStackDeletePermissionUtility(StackDeletePermissionUtility[CoordDeleteContext]):
    """
    Role:
        - Utility

    Responsibilities:
        1.  Bundles resources the CoordDeleteAuthorizer needs to evaluate a CoordDeleteRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        coord_context_validator: CoordContextValidator
        
    Provides:

    Super Class:
        StackDeletePermissionUtility
    """
    validator: Dict[str, StackDeleteContextValidator] = field(
        default_factory=lambda: {
            "coord_context_validator": CoordContextValidator(),
        }
    )
    
    @property
    def coord_context_validator(self) -> CoordContextValidator:
        return self.resources["coord_context_validator"]

    