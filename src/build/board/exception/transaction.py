# src/build/board/exception/transaction.py

"""
Module: build.board.exception.transaction
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""
from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# BOARD_BUILD_FAILURE #======================#
    "BoardBuildException",
]

from system import BuildException


# ======================# BOARD_BUILD_FAILURE #======================#
class BoardBuildException(BuildException):
    """
    Role:
        - Worker Method Identification
        - Exception Chain Layer 1
        - Exception Messaging

    Responsibilities:
        1.  Indicate that, an error prevented a board from being built.
        2.  Trace the method calls.

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
    ERR_CODE = "BOARD_BUILD_FAILURE"
    MSG = "BoardBuilder method failed."
    
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