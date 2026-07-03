# src/logic/pair/listing/build/validator.py

"""
Module: logic.pair.listing.build.work
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# PAIR_LIST_BUILDER_FAILURE #======================#
    "PairListBuilderException",
]

from system import BuilderException


# ======================# PAIR_LIST_BUILDER_FAILURE #======================#
class PairListBuilderException(BuilderException):
    """
    Role:Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Indicate the PairListBuilder did not produce a valid work product.
    2.  Identify the PairListBuilder method where the failure occurred.

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
    ERR_CODE = "PAIR_LIST_BUILDER_FAILURE"
    MSG = "Failure in PairListBuilder method."
    
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