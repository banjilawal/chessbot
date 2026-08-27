# src/authorization/utility/crud/search/stack/board/utility.py

"""
Module: authorization.utility.crud.search.stack.board.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackSearchContextValidator, BoardContextValidator
from authorization import StackSearchPermissionUtility
from domain import BoardSearchSearchContext


@dataclass
class BoardStackSearchPermissionUtility(StackSearchPermissionUtility[BoardSearchSearchContext]):
    """
    Role:
        - Utility

    Responsibilities:
        1.  Bundles resources the BoardSearchAuthorizer needs to evaluate a BoardSearchRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        board_context_validator: BoardContextValidator
        
    Provides:

    Super Class:
        StackSearchPermissionUtility
    """
    validator: Dict[str, StackSearchContextValidator] = field(
        default_factory=lambda: {
            "board_context_validator": BoardContextValidator(),
        }
    )
    
    @property
    def board_context_validator(self) -> BoardContextValidator:
        return self.resources["board_context_validator"]

    