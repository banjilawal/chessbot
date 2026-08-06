# src/report/approval/report.py

"""
Module: report.approval.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from collection import LinkedList
from report import OperationApprovalReport, Permission


T = TypeVar("T", bound="ChainOperation")


class ChainOperationApprovalReport(OperationApprovalReport, ABC, Generic[T]):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Give details about a LinkedListOperationOperation approval.
        
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
    _chain: Optional[LinkedList]
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            chain: Optional[LinkedList] | None = None,
    ):
        super().__init__(permission=permission, exception=exception)
        self._chain = chain

    @property
    def chain(self) -> Optional[LinkedList]:
        return self._chain
    
    @property
    def is_denied(self) -> bool:
        return (
                self._chain is None and
                self._exception is not None and
                self._permission == Permission.DENIED
        )
    
    @property
    def is_granted(self) -> bool:
        return (
            self._chain is not None and
            self._exception is None and
            self._permission == Permission.GRANTED
        )
    
    @classmethod
    @abstractmethod
    def approve(
            cls,
            chain: LinkedList,
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
    
    
