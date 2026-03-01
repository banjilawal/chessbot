# template.service/exception.anchor.py

"""
Module: template.service.exception.anchor
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TEMPLATE_SERVICE_EXCEPTION #======================#
    "TemplateServiceException",
]

from chess.system import IntegrityServiceException

# ======================# TEMPLATE_SERVICE_EXCEPTION #======================#
class TemplateServiceException(IntegrityServiceException):
    """
    # ROLE: Debug Coverage Target, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Indicate that an error occurred in TemplateService instance.

    # PARENT:
    *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See TemplateServiceException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
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
    ERR_CODE = "INTEGRITY_TEMPLATE_SERVICE_EXCEPTION"
    MSG = "TemplateService raised an exception."
    CLS_NAME = "TemplateService"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
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