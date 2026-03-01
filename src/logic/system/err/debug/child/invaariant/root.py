# src/logic/system/err/debug/child/invariant.py

"""
Module: logic.system.err.debug.child.invariant
Author: Banji Lawal
Created: 2026-02-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# INVARIANT_BREACH EXCEPTION #======================#
    "InvariantBreachException",
]

from logic.system import DebugException

# ======================# INVARIANT_BREACH EXCEPTION #======================#
class InvariantBreachException(DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a fundamental invariant of the system or environment is violated. The system’s
        assumptions about its internal state are no longer valid.

    # PARENT:
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DebugException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
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
    DEFAULT_CODE = "INVARIANT_BREACH_EXCEPTION"
    MSG = (
        "A system invariant was violated, indicating a critical state inconsistency. Or entity_service loss."
    )
    VAR = Optional[Any]
    VAL = Optional[Any]
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        var = var or self.VAR
        val = val or self.VAL
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)
