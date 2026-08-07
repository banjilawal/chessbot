# src/report/approval/token/report.py

"""
Module: report.approval.token.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar, cast

from report import RequestDecision, Permission

T = TypeVar("T", bound="TokenRequest")


class TokenRequestDecision(RequestDecision, ABC, Generic[T]):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Give details about an operationOperation approval.
        
    Attributes:
        exception: Optional[Exception]
        permission: Permission
        is_denied: bool
        is_granted: bool
        
    Provides:
        -   def approve(*args, **kwargs) -> OperationApprovalReport
        -   def deny(exception: Exception) -> OperationApprovalReport:

    Super Class:
        OperationApprovalReport
    """
   
    def __init__(
            self,
            permission: Permission,
            request: Optional[T],
            exception: Optional[Exception] | None = None,
    ):
        super().__init__(request=request, permission=permission, exception=exception)

    @property
    def request(self) -> Optional[T]:
        return cast(T, super().request)
    
    @property
    def request_is_denied(self) -> bool:
        return (
                self.request is None and
                self.exception is not None and
                self.permission == Permission.DENIED
        )
    
    @property
    def request_is_granted(self) -> bool:
        return (
            self.request is not None and
            self.exception is None and
            self.permission == Permission.GRANTED
        )
    
    @classmethod
    def approve(cls, request: T) -> RequestDecision:
        return cls(request=request, permission=Permission.GRANTED)
    
    @classmethod
    def deny(cls, exception: Exception) -> RequestDecision:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )
    
    
