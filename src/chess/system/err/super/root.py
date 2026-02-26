# src/chess/system/err/super.py

"""
Module: chess.system.err.super
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SUPER_CLASS EXCEPTION #======================#
    "SuperClassException",
]

from chess.system import ChessException


# ======================# SUPER_CLASS EXCEPTION #======================#
class SuperClassException(ChessException):
    """
    # ROLE: DebugException Parent, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Exception for an Entity or Class.
    2.  Parent of Debug exceptions that are raised by an object being manipulated.

    # NAMING CONVENTION:
    1.  Class name followed by the Exception suffix
    2.  The Syntax is: [Class]Exception

    # ERROR CODE CONVENTION:
    1.  Class name followed by the ERROR suffix.
    2.  The Syntax is: [Class]_ERROR

    # DEFAULT MSG CONVENTION:
    1.  Class name followed by "raised an exception."
    2.  The Syntax is: [Class] raised an exception

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   cls_name (Optional[str])
        
    # INHERITED ATTRIBUTES:
        *   See ChessException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See Exception class for inherited methods.
    """
    ERR_CODE = "CLASS_ERROR"
    MSG = "An exception occurred in the class."
    CLS_NAME: None

    _cls_name: Optional[str]
 
    def __init__(
            self,
            cls_name: Optional[str] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        cls_name = cls_name or self.__class__.__name__
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE

        super().__init__(msg=msg, err_code=err_code, ex=ex)
        _cls_name = cls_name

    @property
    def cls_name(self) -> Optional[str]:
        return self._cls_name
    
    def __str__(self):
        return f"{super().__str__()}, cls_name:{self._cls_name}"