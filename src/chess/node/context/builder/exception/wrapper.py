# src/chess/node/context/builder/exception/wrapper.py

"""
Module: chess.node.context.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional


__all__ = [
    # ======================# NODE_CONTEXT_BUILD_FAILURE #======================#
    "NodeContextBuildException",
]

from chess.system import BuildException

# ======================# NODE_CONTEXT_BUILD_FAILURE #======================#
class NodeContextBuildException(BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a node_context build operation failed. The exception chain
        traces the ultimate source of failure.

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
    ERR_CODE = "NODE_CONTEXT_BUILD_FAILED"
    MSG = "NodeContext build failed."
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

