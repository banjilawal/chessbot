# src/report/approval/stack/report.py

"""
Module: report.approval.stack.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from report import OperationApprovalReport, Permission
from stack import StackService

T = TypeVar("T", bound="StackOperation")


class StackOperationApprovalReport(OperationApprovalReport, ABC, Generic[T]):
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
    _stack: Optional[StackService]
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            stack: Optional[StackService] | None = None,
    ):
        super().__init__(permission=permission, exception=exception)
        self._stack = stack

    @property
    def stack(self) -> Optional[StackService]:
        return self._stack
    
    @property
    def is_denied(self) -> bool:
        return (
                self._stack is None and
                self._exception is not None and
                self._permission == Permission.DENIED
        )
    
    @property
    def is_granted(self) -> bool:
        return (
            self._stack is not None and
            self._exception is None and
            self._permission == Permission.GRANTED
        )
    
    @classmethod
    @abstractmethod
    def approve(
            cls,
            stack: StackService,
            *args: Optional[tuple[Any, ...]],
            **kwargs: Optional[dict[str, Any]],
    ) -> OperationApprovalReport:
        pass
    
    @classmethod
    def deny(cls, exception: Exception) -> OperationApprovalReport:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )
    
    
