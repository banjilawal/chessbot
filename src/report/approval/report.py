# src/report/approval/report.py

"""
Module: report.approval.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Optional, TypeVar

from report import Permission, Report

T = TypeVar("T")


class OperationApprovalReport(Report):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provides details about the outcome of an operation approval request.
        
    Attributes:
        exception: Optional[Exception]
        permission: Permission
        is_denied: bool
        is_granted: bool
        
    Provides:
        -   def approve(*args, **kwargs) -> OperationApprovalReport
        -   def deny(exception: Exception) -> OperationApprovalReport:

    Super Class:
        Report
    """
    _exception: Optional[Exception]
    _permission: Permission
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
    ):
        self._exception = exception
        self._permission = permission
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def permission(self) -> Permission:
        return self._permission
    
    @property
    def is_denied(self) -> bool:
        return (
                self._exception is not None and
                self._permission == Permission.DENIED
        )
    
    @property
    def is_granted(self) -> bool:
        return (
            self._exception is None and
            self._permission == Permission.GRANTED
        )
    
    @classmethod
    @abstractmethod
    def approve(cls, *args, **kwargs) -> OperationApprovalReport:
        pass
    
    @classmethod
    def deny(cls, exception: Exception) -> OperationApprovalReport:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )
    
    
