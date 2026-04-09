# MISSING_src/err/route/search/node/exception.py

"""
Module: err.route.search.node.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional
from err import SearchRouteException


__all__ = [
    # ======================# MISSING_NODE_SEARCH_ROUTE #======================#
    "NodeSearchRouteException",
]

# ======================# MISSING_NODE_SEARCH_ROUTE #======================#
class NodeSearchRouteException(SearchRouteException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that one of Node search routes is missing.

    Attributes:
        op: Optional[str]
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]
            
    Provides:

    Super Class:
        SearchRouteException
    """
    MSG = "One of Node search paths is missing."
    ERR_CODE = "NODE_SEARCH_ROUTE"
    
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
