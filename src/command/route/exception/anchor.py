# src/command/route/exception/anchor.py

"""
Module: command.route.exception.anchor
Author: Banji Lawal
Created: 2026-02-25
"""

from __future__ import annotations
from typing import Optional


__all__ = [
    # ======================# COMMAND_ROUTER_EXCEPTION #======================#
    "CommandRouterException",
]

from logic.system import AnchorException


# ======================# COMMAND_ROUTER_EXCEPTION #======================#
class CommandRouterException(AnchorException):
    """
    # ROLE: Information, Reporting, Debug

    # RESPONSIBILITIES:
    1.  Locus of attention for CommandRouterDebugExceptions.

    # PARENT:
        *   AnchorException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See AnchorException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])
        *   cls_mthd (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See AnchorException class for inherited methods.
    """
    ERR_CODE = "COMMAND_ROUTER_EXCEPTION"
    MSG = "CommandRouter raised an exception."
    CLS_NAME = "CommandRouter"

        
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
    ):
        msg = msg or self.MSG
        cls_name = cls_name or self.CLS_NAME
        cls_mthd = cls_mthd or self.CLS_MTHD
        err_code = err_code or self.ERR_CODE
        super().__init__(
            ex=ex,
            msg=msg,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd
        )
