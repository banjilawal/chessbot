# src/logic/system/search/exception/validator.py

"""
Module: logic.system.search.exception.work
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
        rslt_type: Optional[resultCategory]

    Provides:

    Super Class:
        SearchException
    """
    OP = "Search"
    RSLT_TYPE = "SearchResult"
    ERR_CODE = "SCHEMA_SEARCH_FAILURE"
    MSG = "Search method failed."
    
    def __init__(
            self, = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            rslt_type: Optional[resultCategory] = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            rslt_type: Optional[resultCategory]
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
            title=title,
            err_code=err_code,
            rslt_type=rslt_type,
        )