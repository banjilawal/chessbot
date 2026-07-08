# src/logic/arena/context/build/exception/validator.py

"""
Module: logic.arena.context.build.exception.work
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# ARENA_CONTEXT_BUILDER_FAILURE #======================#
    "ArenaContextBuilderException",
]

from system import BuilderException

# ======================# ARENA_CONTEXT_BUILDER_FAILURE #======================#
class ArenaContextBuilderException(BuilderException):
    """
    Role:Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Indicate the ArenaContextBuilder did not produce a valid work product.
    2.  Identify the ArenaContextBuilder method where the failure occurred.

    Super Class:
        *   BuilderException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See BuilderException class for inherited attributes.

    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See BuilderException class for inherited methods.
    """
    OP = "Build"
    MTHD_RSLT = "BuildResult"
    ERR_CODE = "ARENA_CONTEXT_BUILDER_FAILURE"
    MSG = "Failure in ArenaContextBuilder method."

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