# src/logic/token/route/exception/work.py

"""
Module: logic.token.route.exception.work
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TOKEN_SEARCH_FAILURE #======================#
    "TokenSearchException",
]

from logic.system import SearchException


# ======================# TOKEN_SEARCH_FAILURE #======================#
class TokenSearchException(SearchException):
    """
    Role:Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Indicate that a token search was not completed, it returned an error instead of a
        work product. 
    2.  Identify the method where the failure occurred.

    Super Class:
        *   SearchException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See SearchException class for inherited attributes.

    Attributes:
        op: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See SearchException class for inherited methods.
    """
    OP = "Search"
    RSLT_TYPE = "SearchResult"
    ERR_CODE = "TOKEN_SEARCH_FAILURE"
    MSG = " Token search method failed."
 
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
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

__all__ = [
    # ======================# TOKEN_SEARCH_FAILURE #======================#
    "TokenSearchException",
]

from logic.system import SearchException
from logic.token import TokenException


# ======================# TOKEN_SEARCH_FAILURE #======================#
class TokenSearchException(TokenException, SearchException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why a token search operation failed. The exception chain
        traces the ultimate source of failure.

    Super Class:
        *   FinderException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
