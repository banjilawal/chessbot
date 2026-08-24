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

from assurance import ContextValidator, BoardContextValidator
from authorization import SearchPermissionUtility
from domain import BoardSearchContext


@dataclass
class BoardSearchPermissionUtility(SearchPermissionUtility[BoardSearchContext]):
    """
    Role:
        -   Toolkit

    Responsibilities:
        1.  Bundles resources the BoardSearchAuthorizer needs to evaluate a BoardSearchRequest..

    Attributes:
        validator: Dict[str, ContextValidator]
        board_context_validator: BoardContextValidator
        
    Provides:

    Super Class:
        SearchPermissionUtility
    """
    validator: Dict[str, ContextValidator] = field(
        default_factory=lambda: {
            "board_context_validator": BoardContextValidator(),
        }
    )
    
    @property
    def board_context_validator(self) -> BoardContextValidator:
        return self.resources["board_context_validator"]

    