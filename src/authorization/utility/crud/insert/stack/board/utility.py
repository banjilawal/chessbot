# src/authorization/utility/crud/insert/stack/board/utility.py

"""
Module: authorization.utility.crud.insert.stack.board.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackInsertContextValidator, BoardContextValidator
from authorization import StackInsertPermissionUtility
from domain import BoardInsertContext


@dataclass
class BoardStackInsertPermissionUtility(StackInsertPermissionUtility[BoardInsertContext]):
    """
    Role:
        - Utility

    Responsibilities:
        1.  Bundles resources the BoardInsertAuthorizer needs to evaluate a BoardInsertRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        board_context_validator: BoardContextValidator
        
    Provides:

    Super Class:
        StackInsertPermissionUtility
    """
    validator: Dict[str, StackInsertContextValidator] = field(
        default_factory=lambda: {
            "board_context_validator": BoardContextValidator(),
        }
    )
    
    @property
    def board_context_validator(self) -> BoardContextValidator:
        return self.resources["board_context_validator"]

    