# src/logic/hostage/route/exception/validator.py

"""
Module: logic.hostage.route.exception.work
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# HOSTAGE_SEARCH_FAILURE #======================#
    "HostageSearchException",
]

from system import SearchException


# ======================# HOSTAGE_SEARCH_FAILURE #======================#
class HostageSearchException(SearchException):
    """
    Role:Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Indicate that a hostage search was not completed, it returned an error instead of a
        work product. 
    2.  Trace the method calls.

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
    ERR_CODE = "HOSTAGE_SEARCH_FAILURE"
    MSG = "Hostage search method failed."
 
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
    # ======================# HOSTAGE_SEARCH_FAILURE #======================#
    "HostageSearchException",
]

from system import SearchException
from model.hostage import HostageException


# ======================# HOSTAGE_SEARCH_FAILURE #======================#
class HostageSearchException(HostageException, SearchException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why a hostage search operation failed. The exception chain
        traces the ultimate source of failure.

    Super Class:
        *   FinderException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
