# src/logic/system/collection/operation/update/exception/wrapper.py

"""
Module: logic.system.collection.operation.update.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# UPDATE_FAILURE #======================#
    "UpdateException",
]

from logic.system import CollectionOperationException


# ======================# UPDATE_FAILURE #======================#
class UpdateException(CollectionOperationException):
    """
    Role:Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Indicate an updated was unsuccessful at producing a  valid work product.
    2.  Identify the method where the failure occurred.

    Super Class:
        *   CollectionOperationException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See CollectionException class for inherited attributes.

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
        *   See CollectionOperationException class for inherited methods.
    """
    OP = "Update"
    RSLT_TYPE = "UpdateResult"
    ERR_CODE = "UPDATE_FAILURE"
    MSG = "Update method failed."
    
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
        mthd = mthd or self.MTHD
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