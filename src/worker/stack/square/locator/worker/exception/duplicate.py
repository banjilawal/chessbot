# src/logic/square/database/kernel/operation/crud/deployment/exception/duplicate.py

"""
Module: logic.square.database.kernel.operation.crud.deployment.exception.duplicate
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# ADDING_DUPLICATE_SQUARE_EXCEPTION #======================#
    "AddingDuplicateSquareException",
]

from system import DebugException

# ======================# ADDING_DUPLICATE_SQUARE_EXCEPTION #======================#
class AddingDuplicateSquareException(DebugException):
    """
    Role:
        - Error Variable Identifier
        - Exception Chain Layer 2
        - Exception Messaging

    Responsibilities:
        1.  Indicate an insertion failed because the square was already in the schema.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        SquareDebugException
    """
    ERR_CODE = "ADDING_DUPLICATE_SQUARE_EXCEPTION"
    MSG = "Square is already in the schema."
    
    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            msg: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        """
        Args:
            var: Optional[str]
            val: Optional[Any]
            msg: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)