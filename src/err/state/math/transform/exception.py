# src/err/state/vector/transform/state.py

"""
Module: err.state.vector.transform.state
Author: Banji Lawal
Created: 2026-04-07
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# VECTOR_TRANSFORM_STATE_ERROR #======================#
    "VectorTransformException",
]

from err import VectorStateException


# ======================# VECTOR_TRANSFORM_STATE_ERROR #======================#
class VectorTransformException(VectorStateException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that an error occurred during VectorTransform state.

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
    MSG = "Error during VectorTransform."
    ERR_CODE = "VECTOR_TRANSFORM_STATE_ERROR"
    
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