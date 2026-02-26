# src/chess/ vector/exception.py

"""
Module: chess. vector.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# VECTOR_EXCEPTION #======================#
    "VectorException",
]

from chess.system import SuperClassException


# ======================# VECTOR_EXCEPTION #======================#
class  VectorException(SuperClassException):
    """
    # ROLE: DebugException Parent, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Indicate that an error occurred in a vector.

    # PARENT:
    *   SuperClassException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
        
    # INHERITED ATTRIBUTES:
        *   See SuperClassException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See SuperClassException class for inherited methods.
    """
    ERR_CODE = " VECTOR_EXCEPTION"
    MSG = " Vector raised an exception."
    CLS_NAME = " Vector"
    
    _cls_name: Optional[str]
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        cls_name = cls_name or self.CLS_NAME
        super().__init__(msg=msg, err_code=err_code, ex=ex, cls_name=cls_name)

 