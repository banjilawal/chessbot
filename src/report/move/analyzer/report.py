# src/report/move/analyzer/report.py

"""
Module: report.move.analyzer.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from report import RankElevationDecision, Report
from model import PawnToken, Rank


@dataclass
class RankLevelApproval(Report):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Presents a token's move on an opening square.

    Attributes:
        decision: RankElevationDecision
        new_rank: Optional[Rank] = None
        exception: Optional[Exception] = None

        is_granted: bool
        is_denied: bool

    Provides:
        -   def approve(new_rank: Rank) -> RankElevationReport:
        -   def deny(exception: Exception) -> RankElevationReport:
        
    Super Class:
        Report
    """
    decision: RankElevationDecision
    new_rank: Optional[Rank] = None
    exception: Optional[Exception] = None
    
    @property
    def is_granted(self) -> bool:
        return (
                self.exception is None and
                self.new_rank is not None and
                self.decision == RankElevationDecision.GRANTED
        )
    
    @property
    def is_denied(self) -> bool:
        return not self.is_granted
    
    @classmethod
    def approve(cls, new_rank: Rank) -> RankLevelApproval:
        return cls(
            exception=None,
            new_rank=new_rank,
            decision=RankElevationDecision.GRANTED,
        )
    
    @classmethod
    def deny(cls, exception: Exception) -> RankLevelApproval:
        return cls(
            decision=RankElevationDecision.DENIED,
            exception=exception,
            new_rank=None,
        )
    