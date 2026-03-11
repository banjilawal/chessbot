# src/logic/rank/factory/exception/wrapper.py

"""
Module: logic.rank.factory.exception.wrapper
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# RANK_BUILD_FAILURE #======================#
    "RankBuildException",
]

from logic.system import BuildException


# ======================# RANK_BUILD_FAILURE #======================#
class RankBuildException(BuildException):
    """
    # ROLE: Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in RankBuilder.build that, prevented BuildResult.success() from 
        being returned.

    # PARENT:
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See OperationException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:)
        *   err_code (str)
        *   msg (str)
        *   ex (Optional[Exception])
        *   mthd (Optional[str])
        *   op (Optional[str])
        *   rslt_type (Optional[str])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See WrapperException class for inherited methods.
    """
    OP = "Build"
    MTHD = "build"
    MSG = "Rank build failed."
    RSLT_TYPE = "BuildResult"
    ERR_CODE = "RANK_BUILD_FAILED"
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            ex: Optional[Exception]
            rslt_type: Optional[str]
        """
        op = op or self.OP
        msg = msg or self.MSG
        mthd = mthd or self.MTHD
        err_code = err_code or self.ERR_CODE
        rslt_type = rslt_type or self.RSLT_TYPE
        
        super().__init__(err_code=err_code, msg=msg, ex=ex, mthd=mthd, op=op, rslt_type=rslt_type)