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
#======================# NULL_NODE_EXCEPTION #======================#
    "NullNodeException",
]

from logic.system import NullException

#======================# NULL_NODE_EXCEPTION #======================#
class NullNodeException(NullException):
    """
    # ROLE: Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a node is null where it should not be.
    
    # PARENT:
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See NUllException class for inherited attributes.

    # CONSTRUCTOR:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val Optional[Any])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See NullException class for inherited methods.
    """
    MSG = "Node cannot be null."
    ERR_CODE = "NULL_NODE_EXCEPTION"
    
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
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)


    





