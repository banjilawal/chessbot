# src/err/carrier_validator/builder/dto/exception.py

"""
Module: err.carrier_validator.builder.dto.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import BuilderBootstrapperException
from result import MethodResultType


__all__ = [
    # ======================# DTO_BUILDER_BOOTSTRAPPER_FAILURE #======================#
    "DtoBuilderBootstrapperException",
]

# ======================# DTO_BUILDER_BOOTSTRAPPER_FAILURE #======================#
class DtoBuilderBootstrapperException(BuilderBootstrapperException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that a DtoBuilderBootstrapper was aborted by an exception.

   BuilderBootstrapper was aborted by an exception.s:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
            
    Provides:

    Super Class:
        BuilderBootstrapperException
    """
    MSG = "DtoBuilderBootstrapper failure."
    ERR_CODE = "DTO_BUILDER_BOOTSTRAPPER_FAILURE"
    
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
        mthd_rslt_type = mthd_rslt_type or self.mthd_rslt_type
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
