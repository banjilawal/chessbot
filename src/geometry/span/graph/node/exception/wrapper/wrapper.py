# src/geometry/span/square/build/validator.py

"""
Module: geometry.span.square.build.work
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# NODE_STACK_SERVICE_PRODUCTION_FAILURE #======================#
    "NodeStackServiceProductionException",
]

from system import BuildException


# ======================# NODE_STACK_SERVICE_PRODUCTION_FAILURE #======================#
class NodeStackServiceProductionException(BuildException):
    """
    Role:Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    Responsibilities:
    1.  Identify the NodeStackServiceProducer method where the exception failed.

    Super Class:
        *   BuildException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See BuildException class for inherited attributes.

    Attributes:
        *   op: Optional[str]
        *   msg: Optional[str]
        *   mthd: Optional[str]
        *   err_code: Optional[str]
        *   ex: Optional[Exception]
        *   mthd_rslt_type: Optional[MethodResultType]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See BuildException class for inherited methods.
    """
    OP = "Build"
    MTHD_RSLT = "BuildResult"
    ERR_CODE = "NODE_STACK_SERVICE_PRODUCTION_FAILURE"
    MSG = "Failure in NodeStackServiceProduce rmethod."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            ex: Optional[Exception]
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            mthd_rslt_type=mthd_rslt_type,
        )