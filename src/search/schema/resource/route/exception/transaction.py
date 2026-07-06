# src/logic/system/searcher/exception/validator.py

"""
Module: logic.system.searcher.exception.work
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SCHEMA_SEARCH_FAILURE #======================#
    "SchemaSearchException",
]

from system import SearchException


# ======================# SCHEMA_SEARCH_FAILURE #======================#
class SchemaSearchException(SearchException):
    """
     Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate a Schema search was not completed because an error occurred.
        2.  Identify the SchemaSearchRouter method where the failure occurred.

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
    ERR_CODE = "SCHEMA_SEARCH_FAILURE"
    MSG = "Search method failed."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_Ttype: Optional[MethodResultType] | None = None,
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