# src/logic/system/relation/exception/debug/debug.py

"""
Module: logic.system.relation.exception.debug.debug
Author: Banji Lawal
Created: 2025-12-28
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# RELATION_ANALYSIS_DEBUG_EXCEPTION #======================#
    "RelationDebugException",
]

from logic.system import DebugException

# ======================# RELATION_ANALYSIS_DEBUG_EXCEPTION #======================#
class RelationDebugException(DebugException):
    """
    # ROLE:  Exception Messaging, Exception Chain Layer 2
    # TASK: Capture Error Variable State
    
    # RESPONSIBILITIES:
    1.  Produce the:
            *   variable,
            *   it's Value,
            *   event which fired the variable into its error state.
        which occurred in the Anchor method identified in layer-0 of the exception chain.
    
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
        var: Optional[str]
        val: Optional[str]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
    
    # LOCAL METHODS:
    None
    
    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    VAR = Optional[str]
    VAL = Optional[Any]
    MSG = "RelationAnalysis debug error."
    ERR_CODE = "RELATION_ANALYSIS_DEBUG_EXCEPTION"
    
    def method(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        """
        Args:
            var: Optional[str]
            val: Optional[str]
            msg: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        var = var or self.VAR
        val = val or self.VAL
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)