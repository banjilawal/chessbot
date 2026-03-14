# src/logic/system/relation/exception/debug/null.py

"""
Module: logic.system.relation.exception.debug.null
Author: Banji Lawal
Created: 2025-11-26
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional


___all__ = [
    # ======================# NO_RELATION_EXCEPTION #======================#
    "NoRelationException",
]

from logic.system import RelationDebugException

# ======================# NO_RELATION_EXCEPTION #======================#
class NoRelationException(RelationDebugException):
    """
    # ROLE:  Exception Messaging, Exception Chain Layer 2
    # TASK: Capture Error Variable State

    # RESPONSIBILITIES:
    1.  Produce the:
            *   variable,
            *   it's Value,
            *   event which fired the variable into its error state.
        which occurred in the Anchor method identified in layer-0 of the exception chain.
    2.  Indicate that, a failing result was returned because the candidates did not
        have any relationship.

    # PARENT:
        *   RelationDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See RelationDebugException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        var: Optional[str]
        val: Optional[str]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See RelationDebugException class for inherited methods.
    """
    VAR = Optional[str]
    VAL = Optional[Any]
    ERR_CODE = "NO_RELATION_EXCEPTION"
    MSG = "There is no relationship between entities"
    
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