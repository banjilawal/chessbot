# src/err/model/context/zero/vector/__init__.py

"""
Module: err.model.zero.vector.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import ZeroContextFlagsException

_all_ = [
    # ======================# ZERO_VECTOR_CONTEXT_FLAGS_EXCEPTION #======================#
    "ZeroVectorContextFlagsException",
]

# ======================# ZERO_VECTOR_CONTEXT_FLAGS_EXCEPTION #======================#
class ZeroVectorContextFlagsException(ZeroContextFlagsException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicates that no VectorContext attribute enabled.

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
        ZeroContextFlagsException
    """
    MSG = "No VectorCcontext attribute enabled."
    ERR_CODE = "ZERO_VECTOR_CONTEXT_FLAGS_EXCEPTION"
    
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