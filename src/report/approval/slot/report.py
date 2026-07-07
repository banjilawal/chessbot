# src/report/approval/slot/report.py

"""
Module: report.approval.slot.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Rank
from report import OperationApprovalReport, Permission
from stack import TokenStackService


class RankSlotApprovalReport(OperationApprovalReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provides details about the outcome of a slot approval request.
        
    Attributes:
        rank: Optional[Rank]
        stack: Optional[TokenStackService]
        exception: Optional[Exception]
        permission: Permission
        
    Provides:
        -   def approve(rank: T, stack: Optional[TokenStackService]) -> OperationApprovalReport
        -   def deny(exception: Exception) -> OperationApprovalReport:
        
    Super Class:
        OperationApprovalReport
    """
    _rank: Optional[Rank]
    _stack: Optional[TokenStackService]
    
    def __init__(
            self,
            permission: Permission,
            rank: Optional[Rank],
            stack: Optional[Rank],
            exception: Optional[Exception],
    ):
        """
        Args:
            rank: Optional[Rank]
            stack: Optional[TokenStackService]
            exception: Optional[Exception]
            permission: Permission
        """
        super().__init__(exception=exception, permission=permission)
        self._rank = rank
        self._stack = stack
    
    @property
    def rank(self) -> Optional[Rank]:
        return self._rank
    
    @property
    def stack(self) -> Optional[TokenStackService]:
        return self._stack
    
    @property
    def is_denied(self) -> bool:
        return (
                self._rank is None and
                self._stack is None and
                super().is_denied
        )
    
    @property
    def is_granted(self) -> bool:
        return (
            self._rank is not None and
            self._stack is not None and
            super().is_granted
        )
    
    @classmethod
    def approve(cls, rank: Rank, token_stack: TokenStackService) -> RankSlotApprovalReport:
        return cls(
            rank=rank,
            stack=token_stack,
            permission=Permission.GRANTED
        )
    
    @classmethod
    def deny(cls, exception: Exception) -> RankSlotApprovalReport:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )

    
    
