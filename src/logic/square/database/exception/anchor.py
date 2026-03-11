# src/logic/square/database/exception/super.py

"""
Module: logic.square.database.exception.super
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

___all__ = [
    # ======================# SQUARE_DATABASE_EXCEPTION #======================#
    "SquareDatabaseException",
]

from logic.system import DatabaseException

# ======================# SQUARE_DATABASE_EXCEPTION #======================#
class SquareDatabaseException(DatabaseException):
    """
    # ROLE: Debug Coverage Target, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Indicate that an error occurred in a SquareDatabase.

    # PARENT:
    *   DatabaseException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DatabaseException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See DatabaseException class for inherited methods.
    """
    CLS_MTHD = None
    CLS_NAME = "SquareDatabase"
    ERR_CODE = "SQUARE_SERVICE_EXCEPTION"
    MSG = " SquareDatabase raised an exception."
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
    ):
        """
        Args:
            msg: Optional[str]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        cls_name = cls_name or self.CLS_NAME
        cls_mthd = cls_mthd or self.CLS_MTHD
        super().__init__(msg=msg, err_code=err_code, ex=ex, cls_name=cls_name, cls_mthd=cls_mthd)