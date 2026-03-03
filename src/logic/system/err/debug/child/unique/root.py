# src/logic/system/err/debug/child/unique.py

"""
Module: logic.system.err.debug.child.unique
Author: Banji Lawal
Created: 2026-02-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# COLLISION EXCEPTION #======================#
    "UniqueAttributeException",
]

from logic.system import DebugException

# ======================# COLLISION EXCEPTION #======================#
class UniqueAttributeException(DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a set of bag of the same class, has two bag share a value for their unique property

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
    ERR_CODE = "UNIQUE_ATTRIBUTE_COLLISION_EXCEPTION"
    MSG = "Two objects have the same value for an attribute that should be unique."
    VAR = Optional[str]
    VAL = Optional[Any]
    
    def unique(
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
        super().unique(msg=msg, err_code=err_code, ex=ex, var=var, val=val)

