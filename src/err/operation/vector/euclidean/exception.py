# src/err/operation/vector/euclidean/operation.py

"""
Module: err.operation.vector.euclidean.operation
Author: Banji Lawal
Created: 2026-04-07
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# EUCLIDEAN_DISTANCE_CALCULATION_ERROR #======================#
    "VectorEuclideanException",
]

from err import VectorOperationException


# ======================# EUCLIDEAN_DISTANCE_CALCULATION_ERROR #======================#
class VectorEuclideanException(VectorOperationException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that an error aborted the Euclidean distance calculation.

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
        VectorOperationException
    """
    MSG = str = "Error during Euclidean distance calculation."
    ERR_CODE = "EUCLIDEAN_DISTANCE_CALCULATION_ERROR"
    
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