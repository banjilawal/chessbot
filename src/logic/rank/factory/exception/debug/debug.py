# src/logic/rank/factory/exception/debug/debug.py

"""
Module: logic.rank.factory.exception.debug.debug
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# RANK_FACTORY_DEBUG_EXCEPTION #======================#
    "RankFactoryDebugException",
]

from logic.system import DebugException

# ======================# RANK_FACTORY_DEBUG_EXCEPTION #======================#
class RankFactoryDebugException(DebugException):
    """
    # ROLE: Error Tracing, Debugging, Super Exception

    # RESPONSIBILITIES:
    1.  Indicate that there is no build route for a concrete Rank.

    # PARENT:
        *   ExecutionRoute

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ExecutionRoute class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        msg: Optional[str]
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        err_code: Optional[str]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See ExecutionRoute class for inherited methods.
    """
    VAR = Optional[str]
    VAL = Optional[Any]
    MSG = "RankFactory experienced a debug exception."
    ERR_CODE = "RANK_FACTORY_DEBUG_EXCEPTION"
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
    ):
        """
        Args:
            msg: Optional[str]
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        var = var or self.VAR
        val = val or self.VAL
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)