# src/authorization/utility/crud/insert/stack/coord/utility.py

"""
Module: authorization.utility.crud.insert.stack.coord.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackInsertContextValidator, CoordContextValidator
from authorization import StackInsertPermissionUtility
from domain import CoordInsertContext


@dataclass
class CoordStackInsertPermissionUtility(StackInsertPermissionUtility[CoordInsertContext]):
    """
    Role:
        -   Utility

    Responsibilities:
        1.  Bundles resources the CoordInsertAuthorizer needs to evaluate a CoordInsertRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        coord_context_validator: CoordContextValidator
        
    Provides:

    Super Class:
        StackInsertPermissionUtility
    """
    validator: Dict[str, StackInsertContextValidator] = field(
        default_factory=lambda: {
            "coord_context_validator": CoordContextValidator(),
        }
    )
    
    @property
    def coord_context_validator(self) -> CoordContextValidator:
        return self.resources["coord_context_validator"]

    