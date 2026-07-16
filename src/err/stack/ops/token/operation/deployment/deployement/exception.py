# src/logic/token/database/kernel/operation/deployment/exception/validator.py

"""
Module: logic.token.database.kernel.operation.deployment.exception.work
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TOKEN_STACK_DEPLOYMENT_FAILURE #======================#
    "TokenStackDeploymentException",
]

from system import UpdateException


# ======================# TOKEN_STACK_DEPLOYMENT_FAILURE #======================#
class TokenStackDeploymentException(UpdateException):
    """
    Role:
        - Worker Method Identification
        - Exception Chain Layer 1
        - Exception Messaging

    Responsibilities:
        1.  Indicate that a token schema from deploying.
        2.  Trace the method calls.
        
    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    Provides:

    Super:
        DeletionException
    """
    OP = "Delete"
    MTHD_RSLT_TYPE = "UpdateException"
    ERR_CODE = "TOKEN_STACK_DEPLOYMENT_FAILURE"
    MSG = "TokenStack deployment onto board failed."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt_type = mthd_rslt or self.MTHD_RSLT_TYPE
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            title=title,
            err_code=err_code,
            mthd_rslt_type=mthd_rslt_type,
        )
