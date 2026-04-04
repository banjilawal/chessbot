# src/logic/coord/database/exception/null.py

"""
Module: logic.coord.database.exception.null
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
#======================# COORD_DATABASE_NULL_EXCEPTION #======================#
    "CoordDatabaseNullException",
]

from system import NullException

#======================# COORD_DATABASE_NULL_EXCEPTION #======================#
class CoordDatabaseNullException(NullException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging
    
    Responsibilities:
    1.  Indicate that a coordDatabase is null where it should not be.
    
    Super Class:
        *   NullException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See NUllException class for inherited attributes.

    Attributes:
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
    MSG = "CoordDatabase cannot be null."
    ERR_CODE = "COORD_DATABASE_NULL_EXCEPTION"
    
    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            msg: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        """
        Args:
            var: Optional[str]
            val: Optional[Any]
            msg: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)
    



    





