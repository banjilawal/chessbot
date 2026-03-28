# src/logic/snapshotContext/query/build/exception/work.py

"""
Module: logic.snapshotContext.query.build.exception.work
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SNAPSHOT_CONTEXT_BUILD_FAILURE #======================#
    "SnapshotContextBuildException",
]

from logic.system import BuildException

# ======================# SNAPSHOT_CONTEXT_BUILD_FAILURE #======================#
class SnapshotContextBuildException(BuildException):
    """
    Role:Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Identify the SnapshotContextBuildTransaction method where the exception failed.

    Super Class:
        *   BuildException

    Provides:

    # LOCAL ATTRIBUTES:
        *   op (Optional[str])
        *   rslt_type (Optional[str])

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
        *   See BuildException class for inherited methods.
    """
    ERR_CODE = "SNAPSHOT_CONTEXT_BUILD_FAILURE"
    MSG = "Failure in SnapshotContextBuildTransaction method."
    OP = "Build"
    RSLT_TYPE = "BuildResult"
    
    _op = Optional[str]
    _rslt_type = Optional[str]
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None,
            op: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
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