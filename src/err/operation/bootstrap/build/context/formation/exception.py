# src/err/operation/bootstrap/build/context/formation/exception.py

"""
Module: err.operation.bootstrap.build.context.formation.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""
from __future__ import annotations
from typing import Any, Optional

from err import BootstrapContextBuildException


__all__ = [
    # ======================# BOOTSTRAPPING_FORMATION_CONTEXT_BUILD_AILURE #======================#
    "BootstrapFormationContextBuildException",
]
# ======================# BOOTSTRAPPING_FORMATION_CONTEXT_BUILD_AILURE #======================#
class BootstrapFormationContextBuildException(BootstrapContextBuildException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that a FormationContextBuild bootstrap step failed.

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
        ContextBootstrapBuildException
    """
    MSG = "FormationContextBuild bootstrap step failed."
    ERR_CODE = "BOOTSTRAPPING_FORMATION_CONTEXT_BUILD_AILURE"
    
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
