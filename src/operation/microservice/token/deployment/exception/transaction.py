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

from system import UpdateException

# ======================# TOKEN_DEPLOYMENT_FAILURE #======================#
class TokenDeploymentException(UpdateException):
    """
    Role:Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Indicate that deploying a token failed.
    2.  Identify the TokenDeployer method where the failure occurred.

    Super Class:
        *   UpdateException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See UpdateException class for inherited attributes.

    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt: Optional[ResultCategory]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See UpdateException class for inherited methods.
    """
    OP = "TokenDeployer"
    MTHD_RSLT = "UpdateResult"
    ERR_CODE = "TOKEN_DEPLOYMENT_FAILURE"
    MSG = "TokenDeployer method failed."
    
    def __init__(
            self,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            mthd_rslt: Optional[ResultCategory] = None,
    ):
        """
        Args:
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt: Optional[ResultCategory]
        """
        op = op or self.OP
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            mthd_rslt=mthd_rslt,
        )