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
    # ======================# PAIR_LIST_BUILD_FAILURE #======================#
    "PairListBuildException",
]

from system import BuildException


# ======================# PAIR_LIST_BUILD_FAILURE #======================#
class PairListBuildException(BuildException):
    """
    Role:Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Indicate the PairListBuilder did not produce a valid work product.
    2.  Identify the PairListBuilder method where the failure occurred.

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
        mthd_rslt: Optional[ResultCategory]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See BuildException class for inherited methods.
    """
    OP = "Build"
    MTHD_RSLT = "BuildResult"
    ERR_CODE = "PAIR_LIST_BUILD_FAILURE"
    MSG = "Failure in PairListBuilder method."
    
    def __init__(
            self,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            mthd_rslt: Optional[ResultCategory] = None,
    ):
        """
        Args:
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt: Optional[ResultCategory]
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
            mthd_rslt=mthd_rslt,
        )