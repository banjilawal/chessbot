# src/err/state/registration/register/exception.py

"""
Module: err.state.registration.register.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import RegistrationException

__all__ = [
    # ======================# WORKER_REGISTRATION_FAILURE #======================#
    "WorkerRegistrationException",
]

from result import MethodResultType


# ======================# WORKER_REGISTRATION_FAILURE #======================#
class WorkerRegistrationException(RegistrationException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that registering a worker failed.

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
        RegistrationException
    """
    MSG = "Worker registration failed."
    ERR_CODE = "WORKER_REGISTRATION_FAILURE"
    MTHD_RSLT_TYPE = MethodResultType.INSERTION_RESULT
    
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
        Args:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
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