# src/logic/arena/route/exception/validator.py

"""
Module: logic.arena.route.exception.work
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# ARENA_SEARCH_FAILURE #======================#
    "ArenaSearchException",
]

from system import SearchException


# ======================# ARENA_SEARCH_FAILURE #======================#
class ArenaSearchException(SearchException):
    """
    Role:Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Indicate that a arena search was not completed, it returned an error instead of a
        work product. 
    2.  Trace the method calls.

    Super Class:
        *   SearchException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See SearchException class for inherited attributes.

    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See SearchException class for inherited methods.
    """
    OP = "Search"
    MTHD_RSLT = "SearchResult"
    ERR_CODE = "ARENA_SEARCH_FAILURE"
    MSG = "Arena search method failed."
 
    def __init__(
            self,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            mthd_rslt_type: Optional[MethodResultType] = None,
    ):
        """
        Args:
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
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

__all__ = [
    # ======================# ARENA_SEARCH_FAILURE #======================#
    "ArenaSearchException",
]

from system import SearchException
from logic.arena import ArenaException


# ======================# ARENA_SEARCH_FAILURE #======================#
class ArenaSearchException(ArenaException, SearchException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why a arena search operation failed. The exception chain
        traces the ultimate source of failure.

    Super Class:
        *   FinderException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
