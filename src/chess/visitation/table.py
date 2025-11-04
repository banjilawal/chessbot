# src/chess/visitation/table.py

"""
Module: chess.graph.visitation.table
Author: Banji Lawal
Created: 2025-111-03
version: 1.0.0
"""

from typing import List

from chess.visitation import VisitRecord


class VisitationTable:
    _entries: List[VisitRecord]
    
    def __init__(self, entries: List[VisitRecord]=List[VisitRecord]):
        self._entries = entries
        
    @property
    def entries(self) -> List[VisitRecord]:
        return self._entries