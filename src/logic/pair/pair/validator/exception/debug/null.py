# src/logic/pair/pair/validator/exception/debug/null.py

"""
Module: logic.pair.pair.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
#======================# NODE_PAIR_NULL_EXCEPTION #======================#
    "NodePairNullException",
]

from logic.system import NullException

#======================# NODE_PAIR_NULL_EXCEPTION #======================#
class NodePairNullException(NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a node_pair is null where it should not be.
    
    # PARENT:
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See NUllException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        err_code: Optional[str]
        ex: Optional[Exception]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See NullException class for inherited methods.
    """
    VAR = Optional[str]
    VAL = Optional[Any]
    MSG = "NodePair cannot be null."
    ERR_CODE = "NODE_PAIR_NULL_EXCEPTION"
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        """
        Args:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            err_code: Optional[str]
            ex: Optional[Exception]
        """
        msg = msg or self.MSG
        var = var or self.VAR
        val = val or self.VAL
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)


    





