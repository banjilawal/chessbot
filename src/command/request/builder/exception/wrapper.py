# src/command/command/request/builder/wrapper.py

"""
Module: command.command.request.builder.wrapper
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SERVICE_REQUEST_BUILD_FAILURE #======================#
    "RequestBuildException",
]

from chess.system import BuildException


# ======================# SERVICE_REQUEST_BUILD_FAILURE #======================#
class RequestBuildException(BuildException):
    """
    # ROLE: Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate that an error prevented RequestBuilder from returning a product.

        # PARENT:
            *   BuildException

        # PROVIDES:
        None

        # LOCAL ATTRIBUTES:
        None

        # INHERITED ATTRIBUTES:
            *   See BuildException class for inherited attributes.

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
            *   See WorkerException class for inherited methods.
        """
    ERR_CODE = "SERVICE_REQUEST_BUILD_FAILURE"
    MSG = "RequestBuilder returned an error."
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
