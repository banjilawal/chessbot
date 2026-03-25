# src/logic/formation/key/build/exception/work.py

"""
Module: logic.formation.key.build.exception.work
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# FORMATION_KEY_BUILD_FAILURE #======================#
    "FormationKeyBuildException",
]

from logic.system import BuildException


# ======================# FORMATION_KEY_BUILD_FAILURE #======================#
class FormationKeyBuildException(BuildException):
    """
    Role:Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Indicate the FormationKeyBuildProcess did not produce a valid work product.
    2.  Identify the FormationKeyBuildProcess method where the failure occurred.

    Super Class:
        *   BuildException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See BuildException class for inherited attributes.

    Attributes:
        op: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See BuildException class for inherited methods.
    """
    OP = "Build"
    RSLT_TYPE = "BuildResult"
    ERR_CODE = "FORMATION_KEY_BUILD_FAILURE"
    MSG = "Failure in FormationKeyBuildProcess method."
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
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
            err_code=err_code,
            rslt_type=rslt_type,
        )
