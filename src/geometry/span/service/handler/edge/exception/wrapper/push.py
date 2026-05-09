# src/geometry/span/service/operation/edge/exception/work/push.py

"""
Module: geometry.span.service.operation.edge.exception.work.push
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# EDGE_PAIR_INSERTION_FAILURE #======================#
    "EdgePairInsertionException",
]

from system import InsertionException

# ======================# EDGE_PAIR_INSERTION_FAILURE #======================#
class EdgePairInsertionException(InsertionException):
    """
    Role:Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    Responsibilities:
    1.  Identify the EdgePair method where the push failed.
        
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
        *   mthd_rslt (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See InsertionException class for inherited methods.
    """
    OP = "Insert"
    MTHD_RSLT = "InsertionResult"
    MSG = "EdgePair push failed."
    ERR_CODE = "EDGE_PAIR_INSERTION_FAILURE"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None, = None,
            mthd_rslt_type: Optional[MethodResultType] = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            mthd_rslt_type=mthd_rslt_type,
        )