# src/authorization/utility/crud/delete/stack/board/utility.py

"""
Module: authorization.utility.crud.delete.stack.board.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackDeleteContextValidator, BoardContextValidator
from authorization import StackDeletePermissionUtility
from domain import BoardDeleteContext


@dataclass
class BoardStackDeletePermissionUtility(StackDeletePermissionUtility[BoardDeleteContext]):
    """
    Role:
        -  Utility

    Responsibilities:
        1.  Bundles resources the BoardDeleteAuthorizer needs to evaluate a BoardDeleteRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        board_context_validator: BoardContextValidator
        
    Provides:

    Super Class:
        StackDeletePermissionUtility
    """
    validator: Dict[str, StackDeleteContextValidator] = field(
        default_factory=lambda: {
            "board_context_validator": BoardContextValidator(),
        }
    )
    
    @property
    def board_context_validator(self) -> BoardContextValidator:
        return self.resources["board_context_validator"]

    