# src/logic/persona/key/builder/exception/wrapper.py

"""
Module: logic.persona.key.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# PERSONA_KEY_BUILD_FAILURE #======================#
    "PersonaKeyBuildException",
]

from logic.system import BuildException

#======================# PERSONA_KEY_BUILD_FAILURE #======================#
class PersonaKeyBuildException(BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the PersonaKey build creates an exception. Failed check exceptions are encapsulated
        in a PersonaKeyBuildException which is sent to the caller in a BuildResult.
    2.  The PersonaKeyBuildException provides a trace for debugging and application recovery.
        # RESPONSIBILITIES:

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
        *   See WrapperException class for inherited methods.
    """
    ERR_CODE = "PERSONA_KEY_BUILD_FAILED"
    MSG = "PersonaKey build failed:"
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
