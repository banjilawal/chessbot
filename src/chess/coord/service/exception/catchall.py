# src/chess/coord/service/exception/catchall.py

"""
Module: chess.coord.service.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# COORD_SERVICE EXCEPTION #======================#
    "CoordServiceException",
]

from typing import Optional

from chess.coord import CoordException
from chess.system import ServiceException


# ======================# COORD_SERVICE EXCEPTION #======================#
class CoordServiceException(ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an CoordService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a CoordService method.

    # PARENT:
        *   ServiceException
    
      # PROVIDES:
      None
    
      # ATTRIBUTES:
      None
      """
    ERR_CODE = "COORD_SERVICE_ERROR"
    MSG = "CoordService raised an exception."
    CLS_NAME = "CoordService"
    
    _cls_name: Optional[str]
    
    def __init__(
            self,
            cls_name: Optional[str] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        cls_name = cls_name or self.CLS_NAME
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        
        super().__init__(msg=msg, err_code=err_code, ex=ex)
        _cls_name = cls_name
    
    @property
    def cls_name(self) -> Optional[str]:
        return self._cls_name
    
    def __str__(self):
        return f"{super().__str__()}, cls_name:{self._cls_name}"