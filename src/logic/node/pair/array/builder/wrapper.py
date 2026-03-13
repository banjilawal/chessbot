# src/logic/node/pair/array/builder/wrapper.py

"""
Module: logic.node.pair.array.builder.wrapper
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# NODE_PAIR_LIST_BUILD_FAILURE #======================#
    "NodePairListBuildException",
]

from logic.system import BuildException

# ======================# NODE_PAIR_LIST_BUILD_FAILURE #======================#
class NodePairListBuildException(BuildException):
    """
    # ROLE: Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    # RESPONSIBILITIES:
    1.  Identify the NodePairListBuilder method where the process failed.

    # PARENT:
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See BuildException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:)
        op: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        ex: Optional[Exception]
        rslt_type: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See BuildException class for inherited methods.
    """
    MTHD = None
    OP = "Build"
    RSLT_TYPE = "BuildResult"
    ERR_CODE = "NODE_PAIR_LIST_BUILD_FAILURE"
    MSG = "Failure in NodePairListBuilder method."
    
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
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            rslt_type=rslt_type,
        )