# src/report/approval/promote/report.py

"""
Module: report.approval.promote.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import PawnToken, Rank
from report import OperationApprovalReport, Permission



class PromotionApprovalReport(OperationApprovalReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provides details about the outcome of a promote approval request.
        
    Attributes:
        pawn: T
        rank: Rank
        exception: Optional[Exception]
        permission: Permission
        
    Provides:
        -   def approve(pawn: T, rank: Rank) -> OperationApprovalReport
        -   def deny(exception: Exception) -> OperationApprovalReport:
        
    Super Class:
        OperationApprovalReport
    """
    _pawn: Optional[PawnToken] = None
    _rank: Optional[Rank] = None
    
    def __init__(
            self,
            permission: Permission,
            pawn: Optional[PawnToken] | None = None,
            rank: Optional[Rank] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        super().__init__(exception=exception, permission=permission)
        self._pawn = pawn
        self._rank = rank
    
    
    @property
    def pawn(self) -> Optional[PawnToken]:
        return self._pawn
    
    @property
    def rank(self) -> Optional[Rank]:
        return self._rank
    
    @property
    def is_denied(self) -> bool:
        return (
                self._pawn is None and
                self._rank is None and
                super().is_denied
        )
    
    @property
    def is_granted(self) -> bool:
        return (
            self._pawn is not None and
            self._rank is not None and
            super().is_granted
        )
    
    @classmethod
    def approve(cls, pawn: T, rank: Rank) -> PromotionApprovalReport:
        return cls(
            pawn=pawn,
            rank=rank,
            permission=Permission.GRANTED
        )
    
    @classmethod
    def deny(cls, exception: Exception) -> PromotionApprovalReport:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )

    
    
