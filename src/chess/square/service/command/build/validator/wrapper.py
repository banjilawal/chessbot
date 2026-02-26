# src/chess/square/service/build/request/validator/wrapper.py

"""
Module: chess.square.service.build.request.validator.wrapper
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

__all__ = [
    # ======================# SQUARE_BUILD_REQUEST_FAILURE #======================#
    "SquareBuildRequestException",
]

from chess.system import SuperClassException


# ======================# SQUARE_BUILD_REQUEST_FAILURE #======================#
class SquareBuildRequestException(SuperClassException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in SquareBuildRequestValidator.validate that, prevented a success
        result from being returned.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_BUILD_REQUEST_FAILED"
    MSG = "SquareBuildRequest validation failed."
    CLS_NAME = "ServiceRequestException"
    
    def __new__(cls, msg: str = MSG, ex: Exception | None = None) -> SquareBuildRequestException:
        super().__init__()
    
    def __init__(self, msg: str = MSG, ex: Exception | None = None) -> None:
        # src/chess/square/exception.py
        
        """
        Module: chess.square.exception
        Author: Banji Lawal
        Created: 2025-09-08
        version: 1.0.0
        """
        
        from __future__ import annotations
        
        from typing import Optional
        
        __all__ = [
            # ======================# SQUARE EXCEPTION #======================#
            "SquareException",
        ]
        
        from chess.system import SuperClassException
        
        # ======================# SQUARE EXCEPTION #======================#
        class SquareException(SuperClassException):
            """
            # ROLE: DebugException Parent, Exception Chain Layer 0

            # RESPONSIBILITIES:
            1.  Layer-0 of Exception chain which is the Parent of SquareDebugException

            # PARENT:
            *   SuperClassException

            # PROVIDES:
            None

            # ATTRIBUTES:
            None
            """
            ERR_CODE = "SQUARE_ERROR"
            MSG = "Square raised an exception."
            CLS_NAME = "Square"
            
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