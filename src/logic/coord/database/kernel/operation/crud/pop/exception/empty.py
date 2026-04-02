# src/logic/coord/database/kernel/operation/crud/pop/exception/empty.py

"""
Module: logic.coord.database.kernel.operation.crud.pop.exception.empty
Author: Banji Lawal
Created: 2026-03-28
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# POPPING_EMPTY_COORD_STACK_EXCEPTION #======================#
    "PoppingEmptyCoordStackException",
]

from logic.system import DebugException


# ======================# POPPING_EMPTY_COORD_STACK_EXCEPTION #======================#
class PoppingEmptyCoordStackException(DebugException):
    """
    Role:
        -    Error Variable Identifier
        -   Exception Chain Layer 2,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that a pop failed because the schema was empty.
        
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
    ERR_CODE = "POPPING_EMPTY_COORD_STACK_EXCEPTION"
    MSG = "CoordStackService pop failed: Cannot pop from an empty schema."
    
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

