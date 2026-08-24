# src/authorization/utility/crud/insert/stack/token/utility.py

"""
Module: authorization.utility.crud.insert.stack.token.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackInsertContextValidator, TokenContextValidator
from authorization import StackInsertPermissionUtility
from domain import TokenInsertContext


@dataclass
class TokenStackInsertPermissionUtility(
    StackInsertPermissionUtility[TokenInsertContext]
):
    """
    Role:
        -   Utility

    Responsibilities:
        1.  Bundles resources the TokenInsertAuthorizer needs to evaluate a TokenInsertRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        token_context_validator: TokenContextValidator
        
    Provides:

    Super Class:
        StackInsertPermissionUtility
    """
    validator: Dict[str, StackInsertContextValidator] = field(
        default_factory=lambda: {
            "token_context_validator": TokenContextValidator(),
        }
    )
    
    @property
    def token_context_validator(self) -> TokenContextValidator:
        return self.resources["token_context_validator"]

    