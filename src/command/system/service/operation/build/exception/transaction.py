# src/command/system/service/operation/build/exception/validator.py

"""
Module: command.system.service.operation.build.exception.work
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# COMMAND_BUILD_FAILURE #======================#
    "CommandBuildException",
]

from system import BuildException


# ======================# COMMAND_BUILD_FAILURE #======================#
class CommandBuildException(BuildException):
    """
    Role:Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Indicate that an error prevented CommandBuilder from returning a product.

        Super Class:
            *   BuildException

        # PROVIDES:
        None

        # LOCAL ATTRIBUTES:
        None

        # INHERITED ATTRIBUTES:
            *   See BuildException class for inherited attributes.

        Attributes:
            *   err_code (str)
            *   msg (str)
            *   ex (Optional[Exception])
            *   mthd (Optional[str])
            *   op (Optional[str])
            *   rslt_type (Optional[str])

        # LOCAL METHODS:
       None

        # INHERITED METHODS:
            *   See WorkException class for inherited methods.
        """
    ERR_CODE = "COMMAND_BUILD_FAILURE"
    MSG = "CommandBuilder returned an error."
    MTHD = "build"
    OP = "Build"
    RSLT_TYPE = "BuildResult"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None, = None,
            rslt_type: Optional[str] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        op = op or self.OP
        rslt_type = rslt_type or self.RSLT_TYPE
        super().__init__(err_code=err_code, msg=msg, ex=ex, mthd=mthd, op=op, rslt_type=rslt_type)
