# src/logic/coord/database/kernel/operation/crud/push/exception/duplicate.py

"""
Module: logic.coord.database.kernel.operation.crud.push.exception.duplicate
Author: Banji Lawal
Created: 2026-03-28
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# ADDING_DUPLICATE_COORD_EXCEPTION #======================#
    "AddingDuplicateCoordException",
]

from logic.system import DebugException

# ======================# ADDING_DUPLICATE_COORD_EXCEPTION #======================#
class AddingDuplicateCoordException(DebugException):
    """
    Role:
        - Error Variable Identifier
        - Exception Chain Layer 2
        - Exception Messaging

    Responsibilities:
        1.  Indicate an insertion failed because the coord was already in the stack.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        CoordDebugException
    """
    ERR_CODE = "ADDING_DUPLICATE_COORD_EXCEPTION"
    MSG = "Coord is already in the stack."
    
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