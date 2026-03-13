# src/logic/system/relation/exception/debug/debug.py

"""
Module: logic.system.relation.exception.debug.debug
Author: Banji Lawal
Created: 2025-12-28
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# RELATION_ANALYSIS_DEBUG_EXCEPTION #======================#
    "RelationDebugException",
]

from logic.system import DebugException

# ======================# RELATION_ANALYSIS_DEBUG_EXCEPTION #======================#
class RelationDebugException(DebugException):
    """
    # ROLE: Error Tracing, Debugging
    
    # RESPONSIBILITIES:
    1.  Indicate that an error condition prevented the RelationAnalysis from completing.
    
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
    ERR_CODE = "RELATION_ANALYSIS_DEBUG_EXCEPTION"
    MSG = "RelationAnalysis debug error."
    VAR = Optional[str]
    VAL = Optional[Any]
    
    def method(
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
        super().method(msg=msg, err_code=err_code, ex=ex, var=var, val=val)