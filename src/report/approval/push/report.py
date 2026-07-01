# src/report/approval/push/report.py

"""
Module: report.approval.push.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional, TypeVar

from report import OperationApprovalReport, Permission
from stack import StackService

T = TypeVar("T")


class PushApproval(OperationApprovalReport):
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
    _item: Optional[T] = None
    _stack: Optional[StackService[T]] = None
    
    def __init__(
            self,
            permission: Permission,
            item: Optional[T] | None = None,
            stack: Optional[StackService] | None = None,
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
    def is_denied(self) -> bool:
        return (
                self._item is None and
                self._stack is None and
                super().is_denied
        )
    
    @property
    def is_granted(self) -> bool:
        return (
            self._item is not None and
            self._stack is not None and
            super().is_granted
        )
    
    @classmethod
    def approve(cls, item: T, stack: StackService[T]) -> PushApproval:
        return cls(
            item=item,
            stack=stack,
            permission=Permission.GRANTED
        )

    
    
