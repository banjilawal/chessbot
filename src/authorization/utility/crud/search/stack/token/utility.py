# src/authorization/utility/crud/search/stack/token/utility.py

"""
Module: authorization.utility.crud.search.stack.token.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackSearchContextValidator, TokenContextValidator
from authorization import StackSearchPermissionUtility
from domain import TokenSearchContext


@dataclass
class TokenStackSearchPermissionUtility(
    StackSearchPermissionUtility[TokenSearchContext]
):
    """
    Role:
        -   Toolkit

    Responsibilities:
        1.  Bundles resources the TokenSearchAuthorizer needs to evaluate a TokenSearchRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        token_context_validator: TokenContextValidator
        
    Provides:

    Super Class:
        StackSearchPermissionUtility
    """
    validator: Dict[str, StackSearchContextValidator] = field(
        default_factory=lambda: {
            "token_context_validator": TokenContextValidator(),
        }
    )
    
    @property
    def token_context_validator(self) -> TokenContextValidator:
        return self.resources["token_context_validator"]

    