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

from report.approval.state import PushPermission

T = TypeVar("T")


class OperationApprovalReport:
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Details a token needs to capture an enemy combatant.
        
    Attributes:
        item: T
        stack: StackService[T]
        
    Provides:

    Super Class:
        Report
    """
    _exception: Optional[Exception]
    _permission: PushPermission
    
    def __init__(
            self,
            permission: PushPermission,
            exception: Optional[Exception] | None = None,
    ):
        self._exception = exception
        self._permission = permission
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def permission(self) -> PushPermission:
        return self._permission
    
    @property
    def is_denied(self) -> bool:
        return (
                self._exception is not None and
                self._permission == PushPermission.DENIED
        )
    
    @property
    def is_granted(self) -> bool:
        return (
            self._exception is None and
            self._permission == PushPermission.GRANTED
        )
    
    @classmethod
    @abstractmethod
    def approve(cls, *kargs, **kwargs) -> OperationApprovalReport:
        pass
    
    @classmethod
    def deny(cls, exception: Exception) -> OperationApprovalReport:
        return cls(
            exception=exception,
            permission=PushPermission.DENIED
        )
    
    
