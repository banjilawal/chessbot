# src/err/state/vector/product/state.py

"""
Module: err.state.vector.product.state
Author: Banji Lawal
Created: 2026-04-07
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# SCALAR_PRODUCT_ERROR #======================#
    "ScalarProductException",
]

from err import VectorStateException


# ======================# SCALAR_PRODUCT_ERROR #======================#
class ScalarProductException(VectorStateException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that an error occurred during scalar multiplication.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
            
    Provides:

    Super Class:
        VectorStateException
    """
    MSG = "Error during scalar multiplication."
    ERR_CODE = "SCALAR_PRODUCT_ERROR"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_mthd: Optional[str] | None = None,
            cls_name: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            Mthd_rslt_Type: optional[methodResultType] | None = none,
    ):
        """
        args:
            Msg: Optional[str]
            Var: Optional[str]
            val: Optional[any]
            ex: optional[Exception]
            cls_name: optional[Str]
            cls_mthd: optional[str]
            err_code: optional[str]
            mthd_rslt_type: optional[methodResultType]
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
            mthd_rslt_type=mthd_rslt_type,
        )