# src/authorization/utility/crud/delete/stack/token/utility.py

"""
Module: authorization.utility.crud.delete.stack.token.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackDeleteContextValidator, TokenContextValidator
from authorization import StackDeletePermissionUtility
from domain import TokenDeleteContext


@dataclass
class TokenStackDeletePermissionUtility(
    StackDeletePermissionUtility[TokenDeleteContext]
):
    """
    Role:
        - Utility

    Responsibilities:
        1.  Bundles resources the TokenDeleteAuthorizer needs to evaluate a TokenDeleteRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        token_context_validator: TokenContextValidator
        
    Provides:

    Super Class:
        StackDeletePermissionUtility
    """
    validator: Dict[str, StackDeleteContextValidator] = field(
        default_factory=lambda: {
            "token_context_validator": TokenContextValidator(),
        }
    )
    
    @property
    def token_context_validator(self) -> TokenContextValidator:
        return self.resources["token_context_validator"]

    