# src/logic/zone/service/operation/build/exception/validator.py

"""
Module: logic.zone.service.operation.build.exception.work
Author: Banji Lawal
Created: 2026-03-29
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# ZONE_BUILD_FAILURE #======================#
    "ZoneBuildException",
]

from logic.system import BuildException

# ======================# ZONE_BUILD_FAILURE #======================#
class ZoneBuildException(BuildException):
    """
    Role:
        -   Worker Method Identifier
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate the ZoneBuildProcess was not completed.
        2.  Identify the ZoneBuildProcess method where the failure occurred.

    Attributes:
        op: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        rslt_type: Optional[str]

    Provides

    Super Class:
        BuildException
    """
    OP = "Build"
    RSLT_TYPE = "BuildResult"
    ERR_CODE = "ZONE_BUILD_FAILURE"
    MSG = "Failure in ZoneBuildProcess method."
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
            ex: Optional[Exception]
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