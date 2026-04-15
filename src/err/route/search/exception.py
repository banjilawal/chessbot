# MISSING_src/err/route/search/__init__.py

"""
Module: err.route.search.__init__
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""
from __future__ import annotations
from typing import Any, Optional

from err import ExecutionRouteException

__all__ = [
    # ======================# MISSING_SEARCH_ROUTE #======================#
    "SearchRouteException",
]

# ======================# MISSING_SEARCH_ROUTE #======================#
class SearchRouteException(ExecutionRouteException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that one of  search routes is missing.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt: Optional[ResultCategory]
            
    Provides:

    Super Class:
        ExecutionRouteException
    """
    OP = "Search"
    MSG = "One of  search routes is missing."
    ERR_CODE = "SEARCH_ROUTE"
    MTHD_RSLT = "SearchResult"
    _mthd_rslt = Optional[str]
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            cls_mthd: Optional[str] = None,
            cls_name: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
    ):
        """
        Args:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        mthd_rslt = self.MTHD_RSLT
        err_code = err_code or self.ERR_CODE
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
        )
        self._mthd_rslt = mthd_rslt
    
    @property
    def mthd_rslt(self) -> Optional[str]:
        return self._mthd_rslt
    
    def __str__(self):
        return f"{super().__str__()},  mthd_rslt:{self._mthd_rslt}"