# src/chess/square/service/build/request/validator/wrapper.py

"""
Module: chess.square.service.build.request.validator.wrapper
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_BUILD_REQUEST_FAILURE #======================#
    "SquareBuildCommandFabException",
]

from chess.system import BuildException


# ======================# SQUARE_BUILD_REQUEST_FAILURE #======================#
class SquareBuildCommandFabException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in SquareBuildCommandValidator.validate that, prevented a success
        result from being returned.

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
    ERR_CODE = "SQUARE_BUILD_REQUEST_FAILED"
    MSG = "SquareBuildRequest validation failed."
    MTHD = "build"
    OP = "Build"
    RSLT_TYPE = "BuildResult"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None,
            op: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        mthd = mthd or self.MTHD
        op = op or self.OP
        rslt_type = rslt_type or self.RSLT_TYPE
        
        super().__init__(err_code=err_code, msg=msg, ex=ex, mthd=mthd, op=op, rslt_type=rslt_type)
