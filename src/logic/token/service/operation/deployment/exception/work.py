# src/logic/token/service/operation/tokenDeployment/exception/validator.py

"""
Module: logic.token.service.operation.tokenDeployment.exception.work
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TOKEN_DEPLOYMENT_FAILURE #======================#
    "TokenDeploymentException",
]

from logic.system import UpdateException

# ======================# TOKEN_DEPLOYMENT_FAILURE #======================#
class TokenDeploymentException(UpdateException):
    """
    Role:Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Indicate that deploying a token failed.
    2.  Identify the TokenDeploymentProcess method where the failure occurred.

    Super Class:
        *   UpdateException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See UpdateException class for inherited attributes.

    Attributes:
        op: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See UpdateException class for inherited methods.
    """
    OP = "TokenDeploymentProcess"
    RSLT_TYPE = "UpdateResult"
    ERR_CODE = "TOKEN_DEPLOYMENT_FAILURE"
    MSG = "TokenDeploymentProcess method failed."
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            rslt_type: Optional[str]
        """
        op = op or self.OP
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        rslt_type = rslt_type or self.RSLT_TYPE
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            rslt_type=rslt_type,
        )