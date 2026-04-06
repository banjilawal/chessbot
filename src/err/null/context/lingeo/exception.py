# src/err/null/context/lingeo/exception.py

"""
Module: err.null.lingeo.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional



__all__ = [
    # ======================# LIN_GEO_CONTEXT_NULL_EXCEPTION #======================#
    "LinGeoContextNullException",
]



# ======================# LINGEO_CONTEXT_NULL_EXCEPTION #======================#
class LinGeoContextNullException(ContextNullException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Indicate that null was received instead od a LinGeoContext.

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
        ContextNullException
    """
    MSG = str = "LinGeoContext cannot be null."
    ERR_CODE = "LINGEO_CONTEXT_NULL_EXCEPTION"
    
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
