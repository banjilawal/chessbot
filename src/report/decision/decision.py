# src/report/approval/report.py

"""
Module: report.approval.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar

from report import Permission, Report

T = TypeVar("T", bound="Request")


class RequestDecision(Report, Generic[T]):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Give details about an operationOperation approval.
        
    Attributes:
        permission: Permission
        request: Optional[T]
        exception: Optional[Exception]
        
    Provides:
        -   def approve(request: T) -> OperationApprovalReport
        -   def deny(exception: Exception) -> OperationApprovalReport:

    Super Class:
        Report
    """
    _permission: Permission
    _request: Optional[T]
    _exception: Optional[Exception]

    
    def __init__(
            self,
            permission: Permission,
            request: Optional[T] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            request: Optional[T]
            exception: Optional[Exception]
        """
        self._request = request
        self._exception = exception
        self._permission = permission
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def request(self) -> Optional[T]:
        return self._request
    
    @property
    def permission(self) -> Permission:
        return self._permission
    
    @property
    def request_is_denied(self) -> bool:
        return (
                self._request is None and
                self._exception is not None and
                self._permission == Permission.DENIED
        )
    
    @property
    def request_is_granted(self) -> bool:
        return (
            self._request is not None and
            self._exception is None and
            self._permission == Permission.GRANTED
        )
    
    @classmethod
    def approve(cls, request: T) -> RequestDecision:
        return cls(request=request, permission =Permission.GRANTED)
    
    @classmethod
    def deny(cls, exception: Exception) -> RequestDecision:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )
    
    
