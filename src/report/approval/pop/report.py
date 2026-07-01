# src/report/approval/pop/report.py

"""
Module: report.approval.pop.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional, TypeVar

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
        item_attribute: T
        stack: StackService[T]
        exception: Optional[Exception]
        permission: Permission
        
    Provides:
        -   def approve(item_attribute: T, stack: StackService[T]) -> OperationApprovalReport
        -   def deny(exception: Exception) -> OperationApprovalReport:
        
    Super Class:
        OperationApprovalReport
    """
    _item_attribute: Optional[Any] = None
    _stack: Optional[StackService[T]] = None
    
    def __init__(
            self,
            permission: Permission,
            item_attribute: Optional[T] | None = None,
            stack: Optional[StackService] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        super().__init__(exception=exception, permission=permission)
        self._item_attribute = item_attribute
        self._stack = stack
    
    
    @property
    def item_attribute(self) -> Optional[Any]:
        return self._item_attribute
    
    @property
    def stack(self) -> Optional[StackService[T]]:
        return self._stack
    
    @property
    def is_denied(self) -> bool:
        return (
                self._item_attribute is None and
                self._stack is None and
                super().is_denied
        )
    
    @property
    def is_granted(self) -> bool:
        return (
            self._item_attribute is not None and
            self._stack is not None and
            super().is_granted
        )
    
    @classmethod
    def approve(cls, item_attribute: T, stack: StackService[T]) -> PopApproval:
        return cls(
            item_attribute=item_attribute,
            stack=stack,
            permission=Permission.GRANTED
        )

    
    
