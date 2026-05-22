# src/logic/token/database/kernel/operation/quota/check.py

"""
Module: logic.token.database.kernel.operation.quota.report
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass

from model import Rank
from report import Report

@dataclass
class RankQuotaReport(Report):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Indicate the number of slots available for a Rank in a TokenStack.

    Attributes:
         rank: Rank
         number_of_openings: int

        openings_exist: bool
        rank_is_full: bool

    Provides:

    Super Class:
        Report
    """
    rank: Rank
    number_of_openings: int

    @property
    def openings_exist(self) -> bool:
        return self.rank.persona.quota - self.number_of_openings > 0
    
    @property
    def rank_is_full(self) -> bool:
        return not self.openings_exist