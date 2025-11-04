# src/chess/visitation/table.py

"""
Module: chess.graph.visitation.table
Author: Banji Lawal
Created: 2025-111-03
version: 1.0.0
"""

from typing import List

from chess.graph import Visitation


class VisitationTable:
    _entries: List[Visitation]
    
    def __init__(self, entries: List[Visitation]=List[Visitation]):
        self._entries = entries
        
    @property
    def entries(self) -> List[Visitation]:
        return self._entries