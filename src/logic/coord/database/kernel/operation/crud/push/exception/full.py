# src/logic/coord/database/kernel/operation/crud/push/exception/full.py

"""
Module: logic.coord.database.kernel.operation.crud.push.exception.full
Author: Banji Lawal
Created: 2026-03-28
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# COORD_STACK_FULL_EXCEPTION #======================#
    "CoordStackFullException",
]

from logic.system import DebugException

# ======================# COORD_STACK_FULL_EXCEPTION #======================#
class CoordStackFullException(DebugException):
    """
    Role:
        - Error Variable Identifier
        - Exception Chain Layer 2
        - Exception Messaging

    Responsibilities:
        1.  Indicate that pushing a coord to the stack failed because the stack was full.
        
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
    ERR_CODE = "COORD_STACK_FULL_EXCEPTION"
    MSG = "Cannot push a coord onto a full stack."
    
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