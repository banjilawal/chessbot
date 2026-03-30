# src/logic/system/collection/hash/lookup/exception/validator.py

"""
Module: logic.system.collection.hash.lookup.exception.work
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# LOOKUP_FAILURE #======================#
    "LookupException",
]

from logic.system import CollectionOperationException


# ======================# LOOKUP_FAILURE #======================#
class LookupException(CollectionOperationException):
    """
    Role:Exception Work
  
    Responsibilities:
    1.  Parent of exceptions raised by Lookup operations.
    3.  Super for Metadata errors not covered by lower level LookupFailedExceptions.

    Provides:


    # INHERITED ATTRIBUTES:
        *   See CollectionException class for inherited attributes.

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
        *   See WorkException class for inherited methods.
    """
    DEFAULT_CODE = "LOOKUP_FAILED_EXCEPTION"
    MSG = "Lookup failed."
    MTHD = "lookup"
    OP_NAME = "lookup"
    RSLT = "SearchResult"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None,
            op: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        op = op or self.OP
        rslt_type = rslt_type or self.RSLT_TYPE
        super().__init__(err_code=err_code, msg=msg, ex=ex, mthd=mthd, op=op, rslt_type=rslt_type)