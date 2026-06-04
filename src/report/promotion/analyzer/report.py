# src/report/promotion/analyzer/report.py

"""
Module: report.promotion.analyzer.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from report import Report
from model import PawnToken, PromotionState
from report.promotion.analyzer.state import PromotionDecision


@dataclass
class RankElevationReport(Report):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Presents a token's promotion on an opening square.

    Attributes:
        decision: PromotionDecision
        promotion_row: Optional[int]
        requestor: Optional[PawnToken]
        execption: Optional[Exception]

        can_promote: bool
        cannot_promote: bool

    Provides:
        -   def approve_promotion(cls, pawn: PawnToken) -> RankElevationReport:
        -   def deny_promotion(cls, exception: Exception) -> RankElevationReport:
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
    def approve_promotion(cls, pawn: PawnToken) -> RankElevationReport:
        return cls(
            requestor=pawn,
            decision=PromotionDecision.GRANTED,
            promotion_row=pawn.team.schema.enemy_schema.rank_row,
            exception=None,
        )
    
    @classmethod
    def deny_promotion(cls, exception: Exception) -> RankElevationReport:
        return cls(
            decision=PromotionDecision.DENIED,
            promotion_row=None,
            requestor=None,
            exception=exception,
        )
    