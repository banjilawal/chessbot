# src/chess/neighbor/service.py

"""
Module: chess.neighbor.service
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""

from typing import List

from chess.neighbor import NeighborTuple


class VisitationService:
    """"""
    _records: List[NeighborTuple]
    
    def __init__(self, records: List[NeighborTuple]):
        self._records = records
        
    