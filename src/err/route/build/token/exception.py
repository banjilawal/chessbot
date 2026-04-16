# MISSING_src/err/route/build/token/exception.py

"""
Module: err.route.build.token.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import BuildRouteException


__all__ = [
    # ======================# MISSING_TOKEN_BUILD_ROUTE #======================#
    "TokenBuildRouteException",
]

# ======================# MISSING_TOKEN_BUILD_ROUTE #======================#
class TokenBuildRouteException(BuildRouteException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate a Token build routes is missing.

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
        BuildRouteException
    """
    MSG = "One of Token build routes is missing."
    ERR_CODE = "TOKEN_BUILD_ROUTE"
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
            err_code: Optional[str] = None,
            mthd_rslt: Optional[ResultCategory] = None,
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
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
        )
