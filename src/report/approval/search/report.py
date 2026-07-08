# src/report/approval/search/report.py

"""
Module: report.approval.search.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional, TypeVar

from context import Context
from report import OperationApprovalReport, Permission
from stack import StackService

T = TypeVar("T")


class SearchApprovalReport(OperationApprovalReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provides details about the outcome of a search approval request.
        
    Attributes:
        context: T
        stack: StackService[T]
        exception: Optional[Exception]
        permission: Permission
        
    Provides:
        -   def approve(context: T, stack: StackService[T]) -> OperationApprovalReport
        -   def deny(exception: Exception) -> OperationApprovalReport:
        
    Super Class:
        OperationApprovalReport
    """
    _context: Optional[Context[T]] = None
    _stack: Optional[StackService[T]] = None
    
    def __init__(
            self,
            permission: Permission,
            context: Optional[Context[T]] | None = None,
            stack: Optional[StackService[T]] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        super().__init__(exception=exception, permission=permission)
        self._context = context
        self._stack = stack
    
    
    @property
    def context(self) -> Optional[Context[T]]:
        return self._context
    
    @property
    def stack(self) -> Optional[StackService[T]]:
        return self._stack
    
    @property
    def is_denied(self) -> bool:
        return (
                self._context is None and
                self._stack is None and
                super().is_denied
        )
    
    @property
    def is_granted(self) -> bool:
        return (
            self._context is not None and
            self._stack is not None and
            super().is_granted
        )
    
    @classmethod
    def approve(cls, context: Context[T], stack: StackService[T]) -> SearchApprovalReport:
        return cls(
            context=context,
            stack=stack,
            permission=Permission.GRANTED
        )
    
    @classmethod
    def deny(cls, exception: Exception) -> SearchApprovalReport:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )

    
    
