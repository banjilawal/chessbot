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
from model import PawnToken, PromotionState, Rank
from report.promotion.analyzer.state import RankElevationDecision


@dataclass
class RankElevationReport(Report):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Presents a token's promotion on an opening square.

    Attributes:
        decision: RankElevationDecision
        pawn: Optional[PawnToken] = None
        new_rank: Optional[Rank] = None
        exception: Optional[Exception] = None

        can_promote: bool
        cannot_promote: bool

    Provides:
        -   def approve(pawn: PawnToken, new_rank: Rank) -> RankElevationReport:
        -   def deny(exception: Exception) -> RankElevationReport:
    Super Class:
        Report
    """
    decision: RankElevationDecision
    pawn: Optional[PawnToken] = None
    new_rank: Optional[Rank] = None
    exception: Optional[Exception] = None
    
    @property
    def is_granted(self) -> bool:
        return (
                self.pawn is not None and
                self.new_rank is not None and
                self.exception is None and
                self.decision == RankElevationDecision.GRANTED
        )
    
    @property
    def is_denied(self) -> bool:
        return not self.is_granted
    
    @classmethod
    def approve(cls, pawn: PawnToken, new_rank: Rank) -> RankElevationReport:
        return cls(
            pawn=pawn,
            new_rank=new_rank,
            decision=RankElevationDecision.GRANTED,
            exception=None,
        )
    
    @classmethod
    def deny(cls, exception: Exception) -> RankElevationReport:
        return cls(
            decision=RankElevationDecision.DENIED,
            exception=exception,
            new_rank=None,
            pawn=None,
        )
    