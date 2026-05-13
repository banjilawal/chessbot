# system.service/exception.anchor.py

"""
Module: src.command.root.system.service.exception.anchor
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# COMMAND_SERVICE_EXCEPTION #======================#
    "CommandServiceException",
]

from system import IntegrityServiceException

# ======================# COMMAND_SERVICE_EXCEPTION #======================#
class CommandServiceException(IntegrityServiceException):
    """
    Role:Debug Coverage Target, Exception Chain Layer 0

    Responsibilities:
    1.  Indicate that an error occurred in CommandService instance.

    Super Class:
    *   ServiceException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See TokenCommandServiceException class for inherited attributes.

    Attributes:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])
        *   id (Optional[int])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See ServiceException class for inherited methods.
    """
    ERR_CODE = "INTEGRITY_COMMAND_SERVICE_EXCEPTION"
    MSG = "CommandService raised an exception."
    CLS_NAME = "CommandService"
    
    def __init__(
            self,
            err_code: Optional[str] | None = None,
            msg: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            id: Optional[int] = None,
    ):
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        cls_name = cls_name or self.CLS_NAME
        anchor().__init__(
            id=id,
            ex=ex,
            msg=msg,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
        )