# src/logic/pair/build/exception/validator.py

"""
Module: logic.pair.build.exception.work
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""


from __future__ import annotations
from typing import Optional

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# NODE_TREE_BUILD_FAILURE #======================#
    "NodeTreeBuildException",
]

from system import BuildException


# ======================# NODE_TREE_BUILD_FAILURE #======================#
class NodeTreeBuildException(BuildException):
    """
    Role:Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Indicate the NodeTreeBuilder did not produce a valid work product.
    2.  Identify the NodeTreeBuilder method where the failure occurred.

    Super Class:
        *   BuildException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See BuildException class for inherited attributes.

    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See BuildException class for inherited methods.
    """
    OP = "Build"
    MTHD_RSLT = "BuildResult"
    ERR_CODE = "NODE_TREE_BUILD_FAILURE"
    MSG = "Failure in NodeTreeBuilder method."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_Ttype: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            mthd_rslt_type=mthd_rslt_type,
        )