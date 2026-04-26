# src/err/operation/assembly/binder/Vector/exception.py

"""
Module: err.operation.assembly.binder.Vector.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""
from __future__ import annotations
from typing import Any, Optional

from err import BinderAssemblyException

__all__ = [
    # ======================# VECTOR_BINDER_ASSEMBLY_FAILURE #======================#
    "VectorBinderAssemblyException",
]

# ======================# VECTOR_BINDER_ASSEMBLY_FAILURE #======================#
class VectorBinderAssemblyException(BinderAssemblyException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that a VectorBinder assembly failed.

    Assembly Failed.s:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
            
    Provides:

    Super Class:
        BinderAssemblyException
    """
    MSG = "VectorBinder assembly failed."
    ERR_CODE = "VECTOR_BINDER_ASSEMBLY_FAILURE"
    
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
