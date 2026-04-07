# src/model/report/capacity/stack/square/report.py

"""
Module: model.report.capacity.stack.square.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Rank


class OpeningSquareAvailabilityReport:
    """
     Role:
         - Data Report

     Responsibilities:
         1.  Record of a rank's
                - Quota
                - The number of open slots
            that a SquareStackService can support
            
     Attributes:
         
         number_of_openings: int
         
     Provides:
     Super:
     """
    _rank: Rank
    _number_of_openings: int
    
    def report(self, rank: Rank,  number_of_openings: int):
        self._rank = rank
        self._number_of_openings = number_of_openings
        
    @property
    def rank(self) -> Rank:
        return self._rank
    
    @property
    def number_of_openings(self) -> int:
        return self._number_of_openings
    
    @property
    def openings_exist(self) -> bool:
        return self._rank.persona.quota - self._number_of_openings > 0
    
    @property
    def rank_is_full(self) -> bool:
        return not self.openings_exist