# src/err/consistency/register/identity/exception.py

"""
Module: err.consistency.register.identity.exception
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import RegisterException
from result import MethodResultType

__all__ = [
    # ======================# VECTOR_IDENTITY_REGISTER_CONSISTENCY_CHECKER_FAILURE #======================#
    "VectorIdentityRegisterConsistencyCheckerException",
]

# ======================# VECTOR_IDENTITY_REGISTER_CONSISTENCY_CHECKER_FAILURE #======================#
class VectorIdentityRegisterConsistencyCheckerException(RegisterException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that a VectorIdentityRegisterConsistencyChecker raised an error.

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
        RegisterException
    """
    MSG = "VectorIdentityRegister consistency error."
    ERR_CODE = "VECTOR_IDENTITY_REGISTER_CONSISTENCY_CHECKER_FAILURE"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            ex: Optional[Exception] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
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

    
    
