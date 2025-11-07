# src/chess/visitation/service.py

"""
Module: chess.visitation.service
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""

from typing import List

from chess.visitation import VisitRecord


class VisitationService:
    """"""
    _records: List[VisitRecord]
    
    def __init__(self, records: List[VisitRecord]):
        self._records = records
        
    