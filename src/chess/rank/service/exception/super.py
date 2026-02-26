# src/chess/rank/service/exception.super.py

"""
Module: chess.rank.service.exception.super
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# RANK_SERVICE EXCEPTION #======================#
    "RankServiceException",
]

from chess.system import ServiceException


# ======================# RANK_SERVICE EXCEPTION #======================#
class RankServiceException(ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by RankService methods that return Result objects.

    # PARENT:
        *   RankException
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "RANK_SERVICE_ERROR"
    MSG = "RankService raised an exception."
    CLS_NAME = "RankService"
    
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