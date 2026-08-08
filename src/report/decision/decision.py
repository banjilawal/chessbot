# src/report/decision/report.py

"""
Module: report.decision.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from authorization import Request
from report import Permission, Report


class RequestDecision(Report):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Give details about an operationOperation decision.
        
    Attributes:
        permission: Permission
        request: Optional[T]
        exception: Optional[Exception]
        
    Provides:
        -   def approve(request: Request) -> RequestDecision
        -   def deny(exception: Exception) -> RequestDecision

    Super Class:
        Report
    """
    _permission: Permission
    _request: Optional[Request]
    _exception: Optional[Exception]

    
    def __init__(
            self,
            permission: Permission,
            request: Optional[Request] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            request: Optional[Request]
            exception: Optional[Exception]
        """
        self._request = request
        self._exception = exception
        self._permission = permission
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def request(self) -> Optional[Request]:
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
    def approve(cls, request: Request) -> RequestDecision:
        return cls(request=request, permission =Permission.GRANTED)
    
    @classmethod
    def deny(cls, exception: Exception) -> RequestDecision:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )
    
    
