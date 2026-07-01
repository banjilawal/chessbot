# src/report/approval/pop/report.py

"""
Module: report.approval.pop.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional, TypeVar

from report import OperationApprovalReport, Permission
from stack import StackService

T = TypeVar("T")


class PopApproval(OperationApprovalReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provides details about the outcome of a pop approval request.
        
    Attributes:
        id: T
        stack: StackService[T]
        exception: Optional[Exception]
        permission: Permission
        
    Provides:
        -   def approve(id: T, stack: StackService[T]) -> OperationApprovalReport
        -   def deny(exception: Exception) -> OperationApprovalReport:
        
    Super Class:
        OperationApprovalReport
    """
    _stack: Optional[StackService[T]]
    
    def __init__(
            self,
            permission: Permission,
            stack: Optional[StackService] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        super().__init__(exception=exception, permission=permission)
        self._stack = stack
    
    @property
    def stack(self) -> Optional[StackService[T]]:
        return self._stack
    
    @property
    def is_denied(self) -> bool:
        return (
                self._stack is None and
                super().is_denied
        )
    
    @property
    def is_granted(self) -> bool:
        return (
            self._stack is not None and
            super().is_granted
        )
    
    @classmethod
    def approve(cls, stack: StackService[T]) -> PopApproval:
        return cls(
            stack=stack,
            permission=Permission.GRANTED
        )
    
    @classmethod
    def deny(cls, exception: Exception) -> PopApproval:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )

    
    
