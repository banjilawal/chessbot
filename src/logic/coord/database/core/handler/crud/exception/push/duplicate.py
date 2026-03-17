# src/logic/coord/database/core/handler/crud/exception/push/duplicate.py

"""
Module: logic.coord.database.core.handler.crud.exception.push.duplicate
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# PUSHING_DUPLICATE_COORD_ONTO_STACK_EXCEPTION #======================#
    "DuplicateCoordPushException",
]

from logic.system import DebugException

# ======================# PUSHING_DUPLICATE_COORD_ONTO_STACK_EXCEPTION #======================#
class DuplicateCoordPushException(DebugException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate pushing a Coord failed because it was already on the top coord on the stack.

    # PARENT:
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DebugException class for inherited attributes.

    # CONSTRUCTOR:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val Optional[Any])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    MSG = "Coord is already the top coord on the stack."
    ERR_CODE = "PUSHING_DUPLICATE_COORD_ONTO_STACK_EXCEPTION"
    
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