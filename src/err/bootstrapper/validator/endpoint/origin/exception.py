# src/err/bootstrap/validator/endpoint/origin/exception.py

"""
Module: err.bootstrapper.validator.endpoint.origin.exception
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import ValidatorBootstrapperException
from result import MethodResultType

__all__ = [
    # ======================# ORIGIN_CERTIFIER_BOOTSTRAPPER_FAILURE #======================#
    "OriginCertifierBootstrapperException",
]

# ======================# ORIGIN_CERTIFIER_BOOTSTRAPPER_FAILURE #======================#
class OriginCertifierBootstrapperException(ValidatorBootstrapperException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that an OriginCertifierBootstrapper
            was aborted by an exception.
        
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
        ValidatorBootstrapperException
    """
    MSG = "OriginCertifierBootstrapper encountered an error."
    ERR_CODE = "ORIGIN_CERTIFIER_BOOTSTRAPPER_FAILURE"
    MTHD_RSLT_TYPE = MethodResultType.ANALYSIS_RESULT
    
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
        mthd_rslt_type = mthd_rslt_type or self.MTHD_RSLT_TYPE
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