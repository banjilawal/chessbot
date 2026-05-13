# src/logic/system/err/debug/child/invariant.py

"""
Module: logic.system.err.debug.child.invariant
Author: Banji Lawal
Created: 2026-02-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# INVARIANT_BREACH EXCEPTION #======================#
    "InvariantBreachException",
]

from system import DebugException

# ======================# INVARIANT_BREACH EXCEPTION #======================#
class InvariantBreachException(DebugException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  Indicate that a fundamental invariant of the system or environment is violated. The system’s
        assumptions about its internal state are no longer valid.

    Super Class:
        *   DebugException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See DebugException class for inherited attributes.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    ERR_CODE = "INVARIANT_BREACH_EXCEPTION"
    MSG = "System invariant violated. Indicates critical data loss."
    
    def __init__(
            self,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            msg: Optional[str] | None = None,
            err_code: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
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
