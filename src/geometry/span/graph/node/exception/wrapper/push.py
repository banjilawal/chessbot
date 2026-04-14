# src/geometry/span/service/operation/node/exception/work/push.py

"""
Module: geometry.span.service.operation.node.exception.work.push
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# PAIR_INSERTION_FAILURE #======================#
    "PairInsertionException",
]

from system import InsertionException

# ======================# PAIR_INSERTION_FAILURE #======================#
class PairInsertionException(InsertionException):
    """
    Role:Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    Responsibilities:
    1.  Identify the Pair method where the push failed.
        
    Super Class:
        *   InsertionException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See InsertionException class for inherited attributes.

    Attributes:
        *   err_code (str)
        *   msg (str)
        *   ex (Optional[Exception])
        *   mthd (Optional[str])
        *   op (Optional[str])
        *   rslt_type (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See InsertionException class for inherited methods.
    """
    OP = "Insert"
    RSLT_TYPE = "InsertionResult"
    MSG = "Pair push failed."
    ERR_CODE = "PAIR_INSERTION_FAILURE"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None, = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            rslt_type: Optional[str]
        """
        op = op or self.OP
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        rslt_type = rslt_type or self.RSLT_TYPE
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            rslt_type=rslt_type,
        )