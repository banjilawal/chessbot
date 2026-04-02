# src/logic/square/database/kernel/operation/quota/check.py

"""
Module: logic.square.database.kernel.operation.quota.report
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.rank import Rank


class SchemaRankQuotaReport:
    """
     Role:
         - Data Report

     Responsibilities:
         1.  Report of a rank quota on a team.
            
     Attributes:
        rank: Rank
        quota: Quota
         
    Provides:
    Super:
    """
    _rank: Rank
    _quota: int
    
    def __init__(self, rank: Rank,  quota: int):
        self._rank = rank
        self._quota = quota
        
    @property
    def rank(self) -> Rank:
        return self._rank
    
    @property
    def quota(self) -> int:
        return self._quota