# src/logic/square/validation/exception/validator.py

"""
Module: logic.square.validation.exception.work
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# OPENING_SQUARE_DISCOVERY_EXCEPTION #======================#
    "SearchException",
]

from system import SearchException


# ======================# OPENING_SQUARE_DISCOVERY_EXCEPTION #======================#
class OpeningSquareDiscoveryException(SearchException):
    """
     Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that, the opening square discovery exception was aborted by an error.
        2.  Trace the method calls.

    Attributes:
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    Provides:

    Super Class:
        SearchException
    """
    OP = "Search"
    MTHD_RSLT = "SearchResult"
    ERR_CODE = "OPENING_SQUARE_DISCOVERY_EXCEPTION"
    MSG = "OpeningSquareSearch failure"
    
    def __init__(
            self,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            mthd_rslt_type: Optional[MethodResultType] = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
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
            title=title,
            err_code=err_code,
            mthd_rslt_type=mthd_rslt_type,
        )