# src/report/approval/token/promotion/report.py

"""
Module: report.approval.token.promotion.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import PawnToken, Rank
from report import TokenRequestDecision, Permission



class PromotionRequestDecision(TokenRequestDecision):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Give details about a promoteOperation approval.
        
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
    def request_is_denied(self) -> bool:
        return (
                self._pawn is None and
                self._rank is None and
                super().request_is_denied
        )
    
    @property
    def request_is_granted(self) -> bool:
        return (
            self._pawn is not None and
            self._rank is not None and
            super().request_is_granted
        )
    
    @classmethod
    def approve(cls, pawn: T, rank_level: Rank) -> PromotionRequestDecision:
        return cls(
            pawn=pawn,
            rank=rank_level,
            permission=Permission.GRANTED
        )
    
    @classmethod
    def deny(cls, exception: Exception) -> PromotionRequestDecision:
        return cls(
            exception=exception,
            permission=Permission.DENIED
        )

    
    
