# src/err/builder/vector/register/mismatch/py

"""
Module: err.builder.vector.register.mismatch.operation
Author: Banji Lawal
Created: 2026-04-07
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# VECTOR_REGISTER_MISMATCH_ERROR #======================#
    "VectorRegisterMismatchException",
]

from err import VectorOperationException


# ======================# VECTOR_REGISTER_MISMATCH_ERROR #======================#
class VectorRegisterMismatchException(VectorOperationException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that an binary operation failed because the operands do
            not have the same context.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        Mthd_Rslt_Type: Optional[MethodResultType]
        
    Provides:

    Super Class:
        VectorOperationException
    """
    MSG = "The registers do not have the same context."
    ERR_CODE = "VECTOR_REGISTER_MISMATCH_ERROR"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_mthd: Optional[str] | None = None,
            cls_name: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
        args:
            Msg: Optional[str]
            Var: Optional[str]
            val: Optional[any]
            ex: Optional[Exception]
            cls_name: Optional[Str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
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