# src/logic/token/database/kernel/operation/quota/report.py

"""
Module: logic.token.database.kernel.operation.quota.report
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.rank import Rank


class RankQuotaReport:
    """
     Role:
         - Data Report

     Responsibilities:
         1.  Record of a rank's
                - Quota
                - The number of open slots
            that a TokenStackService can support
            
     Attributes:
         rank: Rank
         quota: int
         opernings: int
         
     Provides:
     Super:
     """
    _rank: Rank
    _quota: int
    _openings: int
    
    def __init__(self, rank: Rank, quota: int, openings: int):
        self._rank = rank
        self._quota = quota
        self._openings = openings
        
    @property
    def rank(self) -> Rank:
        return self._rank
    
    @property
    def quota(self) -> int:
        return self._quota
    
    @property
    def openings(self) -> int:
        return self._openings