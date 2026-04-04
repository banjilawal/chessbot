# MISSING_src/err/route/validation/token/exception.py

"""
Module: err.route.validation.token.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import ValidationRouteException


__all__ = [
    # ======================# MISSING_TOKEN_VALIDATION_ROUTE #======================#
    "TokenValidationRouteException",
]

# ======================# MISSING_TOKEN_VALIDATION_ROUTE #======================#
class TokenValidationRouteException(ValidationRouteException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate a Token validation routes is missing.

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
        ValidationRouteException
    """
    MSG = "One of Token validation routes is missing."
    ERR_CODE = "TOKEN_VALIDATION_ROUTE"
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
            err_code: Optional[str] = None,
            rslt_type: Optional[str] = None,
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
        op = op or self.OP
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        rslt_type = rslt_type or self.RSLT_TYPE
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
        )
