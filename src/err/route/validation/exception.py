# MISSING_src/err/route/validation/__init__.py

"""
Module: err.route.validation.__init__
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""
from __future__ import annotations
from typing import Any, Optional

from err import ExecutionRouteException

__all__ = [
    # ======================# MISSING_VALIDATION_ROUTE #======================#
    "ValidationRouteException",
]

# ======================# MISSING_VALIDATION_ROUTE #======================#
class ValidationRouteException(ExecutionRouteException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that one of  validation routes is missing.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]
            
    Provides:

    Super Class:
        ExecutionRouteException
    """
    MSG = "One of  validation routes is missing."
    ERR_CODE = "VALIDATION_ROUTE"
    MTHD_RSLT = "ValidationResult"
    _mthd_rslt_type = Optional[str]
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_mthd: Optional[str] | None = None,
            cls_name: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
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
        return f"{super().__str__()},  mthd_rslt_type:{self._mthd_rslt}"