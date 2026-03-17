# src/logic/pair/listing/validator/exception/debug/null.py

"""
Module: logic.pair.listing.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
#======================# PAIR_LIST_NULL_EXCEPTION #======================#
    "PairListNullException",
]

from logic.system import NullException

#======================# PAIR_LIST_NULL_EXCEPTION #======================#
class PairListNullException(NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a pairList is null where it should not be.
    
    Super Class:
        *   NullException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See NUllException class for inherited attributes.

    Attributes:
        val: Optional[Any]
        var: Optional[str]
        msg: Optional[str]
        err_code: Optional[str]
        ex: Optional[Exception

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See NullException class for inherited methods.
    """
    MSG = "PairList cannot be null."
    ERR_CODE = "PAIR_LIST_NULL_EXCEPTION"
    
    def __init__(
            self,
            val: Optional[Any] = None,
            var: Optional[str] = None,
            msg: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,

    ):
        """
        Args:
            val: Optional[Any]
            var: Optional[str]
            msg: Optional[str]
            err_code: Optional[str]
            ex: Optional[Exception]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)


    





