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
#======================# NULL_PAIR_EXCEPTION #======================#
    "NullPairException",
]

from logic.system import NullException

#======================# NULL_PAIR_EXCEPTION #======================#
class NullPairException(NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a pair is null where it should not be.
    
    Super Class:
        *   NullException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See NUllException class for inherited attributes.

    Attributes:
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
    MSG = "Pair cannot be null."
    ERR_CODE = "NULL_PAIR_EXCEPTION"
    
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


    





