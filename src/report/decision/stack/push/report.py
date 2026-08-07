# src/report/approval/stack/push/report.py

"""
Module: report.approval.stack.push.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional, TypeVar

from report import RequestDecision, Permission
from stack import StackService

T = TypeVar("T")


class PushApprovalReport(RequestDecision):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Give details about a pushOperation approval.
        
    Attributes:
        item: T
        stack: StackService[T]
        exception: Optional[Exception]
        permission: Permission
        
    Provides:
        -   def approve(item: T, stack: StackService[T]) -> OperationApprovalReport
        -   def deny(exception: Exception) -> OperationApprovalReport:
        
    Super Class:
        OperationApprovalReport
    """
    _item: Optional[T] = None
    _stack: Optional[StackService[T]] = None
    
    def __init__(
            self,
            permission: Permission,
            item: Optional[T] | None = None,
            stack: Optional[StackService[T]] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        super().__init__(exception=exception, permission=permission)
        self._item = item
        self._stack = stack
    
    
    @property
    def item(self) -> Optional[T]:
        return self._item
    
    @property
    def stack(self) -> Optional[StackService[T]]:
        return self._stack
    
    @property
    def request_is_denied(self) -> bool:
        return (
                self._item is None and
                self._stack is None and
                super().request_is_denied
        )
    
    @property
    def request_is_granted(self) -> bool:
        return (
            self._item is not None and
            self._stack is not None and
            super().request_is_granted
        )
    
    @classmethod
    def approve(cls, item: T, stack: StackService[T]) -> PushApprovalReport:
        return cls(
            item=item,
            stack=stack,
            permission=Permission.GRANTED
        )
    
    @classmethod
    def deny(cls, exception: Exception) -> PushApprovalReport:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )

    
    
