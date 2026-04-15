# MISSING_src/err/route/search/rank/exception.py

"""
Module: err.route.search.rank.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import SearchRouteException


__all__ = [
    # ======================# MISSING_RANK_SEARCH_ROUTE #======================#
    "RankSearchRouteException",
]

# ======================# MISSING_RANK_SEARCH_ROUTE #======================#
class RankSearchRouteException(SearchRouteException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that one of Rank search routes is missing.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[ResultCategory]
            
    Provides:

    Super Class:
        SearchRouteException
    """
    MSG = "One of Rank search paths is missing."
    ERR_CODE = "RANK_SEARCH_ROUTE"
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
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
