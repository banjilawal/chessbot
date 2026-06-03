# src/report/claim/report.py

"""
Module: report.claim.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from model import PawnToken, PromotionState
from report import Report
from report.promote.state import PromotionDecision


@dataclass
class PromotionPermissionReport(Report):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Presents a token's claim on an opening square.
        
    Attributes:
        requestor: PawnToken
        promotion_row: Optional[int]
        decision: PromotionDecision
        
        can_promote: bool
        cannot_promote: bool
        
    Provides:
        -   def grant_promotion(pawn: PawnToken) -> PromotionReport
        -   def deny_promotion(pawn: PawnToken) -> PromotionReport
    Super Class:
        Report
    """
    decision: PromotionDecision
    requestor: Optional[PawnToken] = None
    promotion_row: Optional[int] = None
    exception: Optional[Exception] = None
    
    
    @property
    def is_granted(self) -> bool:
        return (
                self.requestor.is_active and
                self.exception is None and
                self.decision == PromotionDecision.GRANTED and
                self.requestor.promotion_state == PromotionState.NOT_PROMOTED and
                self.requestor.current_position.row == self.promotion_row
        )
    
    @property
    def is_denied(self) -> bool:
        return not self.is_granted
    
    @classmethod
    def grant_promotion(cls, pawn: PawnToken) -> PromotionPermissionReport:
        return cls(
            requestor=pawn,
            decision=PromotionDecision.GRANTED,
            promotion_row=pawn.team.schema.enemy_schema.rank_row,
            exception=None,
        )
    
    @classmethod
    def deny_promotion(cls, exception: Exception) -> PromotionPermissionReport:
        return cls(
            decision=PromotionDecision.DENIED,
            promotion_row=None,
            requestor=None,
            exception=exception,
        )
    