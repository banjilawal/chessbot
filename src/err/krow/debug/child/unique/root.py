# src/logic/system/err/debug/child/unique.py

"""
Module: logic.system.err.debug.child.unique
Author: Banji Lawal
Created: 2026-02-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# COLLISION EXCEPTION #======================#
    "UniqueAttributeException",
]

from system import DebugException

# ======================# COLLISION EXCEPTION #======================#
class UniqueAttributeException(DebugException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a set of bag of the same class, has two bag share a value for their unique property

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
    ERR_CODE = "UNIQUE_ATTRIBUTE_COLLISION_EXCEPTION"
    MSG = "Two objects have the same value for an attribute that should be unique."
    
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

