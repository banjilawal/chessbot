# src/authorization/utility/crud/insert/stack/square/utility.py

"""
Module: authorization.utility.crud.insert.stack.square.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackInsertContextValidator, SquareContextValidator
from authorization import StackInsertPermissionUtility
from domain import SquareInsertContext


@dataclass
class SquareStackInsertPermissionUtility(StackInsertPermissionUtility[SquareInsertContext]):
    """
    Role:
        -  Utility

    Responsibilities:
        1.  Bundles resources the SquareInsertAuthorizer needs to evaluate a SquareInsertRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        square_context_validator: SquareContextValidator
        
    Provides:

    Super Class:
        StackInsertPermissionUtility
    """
    validator: Dict[str, StackInsertContextValidator] = field(
        default_factory=lambda: {
            "square_context_validator": SquareContextValidator(),
        }
    )
    
    @property
    def square_context_validator(self) -> SquareContextValidator:
        return self.resources["square_context_validator"]

    