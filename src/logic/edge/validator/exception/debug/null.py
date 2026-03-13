# src/logic/edge/validator/exception/debug/null.py

"""
Module: logic.edge.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
#======================# NULL_EDGE_EXCEPTION #======================#
    "NullEdgeException",
]

from logic.system import NullException

#======================# NULL_EDGE_EXCEPTION #======================#
class NullEdgeException(NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a edge is null where it should not be.
    
    # PARENT:
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See NUllException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
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
    VAR = Optional[str]
    VAL = Optional[Any]
    MSG = "Edge cannot be null."
    ERR_CODE = "NULL_EDGE_EXCEPTION"
    
    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            msg: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
  
    ):
        """
        Args:
        
        """
        msg = msg or self.MSG
        var = var or self.VAR
        val = val or self.VAL
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)


    





