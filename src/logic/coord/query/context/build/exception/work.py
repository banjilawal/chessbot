# src/logic/coord/query/query/build/exception/work.py

"""
Module: logic.coord.query.build.exception.work
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# COORD_CONTEXT_BUILD_FAILURE #======================#
    "CoordContextBuildException",
]

from logic.system import BuildException


# ======================# COORD_CONTEXT_BUILD_FAILURE #======================#
class CoordContextBuildException(BuildException):
    """
    Role:
        - Worker Method Identification
        - Exception Chain Layer 1
        - Exception Messaging

    Responsibilities:
        1.  Indicate that  an error prevented a coordContext from being built.
        2.  Identify the method where the failure occurred.

    Attributes:
        op: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]

    Provides:

    Super:
        BuildException
    """
    OP = "Build"
    RSLT_TYPE = "BuildResult"
    ERR_CODE = "COORD_CONTEXT_BUILD_FAILURE"
    MSG = "Failure in CoordContextBuilder method."
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
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
            title: Optional[str]
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
            title=title,
            err_code=err_code,
            rslt_type=rslt_type,
        )