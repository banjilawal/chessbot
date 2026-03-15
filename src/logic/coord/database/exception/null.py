# src/logic/coord/database/exception/null.py

"""
Module: logic.coord.database.exception.null
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
#======================# COORD_DATABASE_NULL_EXCEPTION #======================#
    "CoordDatabaseNullException",
]

from logic.system import NullException

#======================# COORD_DATABASE_NULL_EXCEPTION #======================#
class CoordDatabaseNullException(NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a coordDatabase is null where it should not be.
    
    # PARENT:
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See NUllException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val Optional[Any])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See NullException class for inherited methods.
    """
    ERR_CODE = "COORD_DATABASE_NULL_EXCEPTION"
    MSG = "CoordDatabase cannot be null."
    VAR = Optional[str]
    VAL = Optional[Any]
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        var = var or self.VAR
        val = val or self.VAL
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)


    





