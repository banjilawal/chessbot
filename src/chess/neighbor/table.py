# src/chess/neighbor/table.py

"""
Module: chess.graph.neighbor.table
Author: Banji Lawal
Created: 2025-111-03
version: 1.0.0
"""

from typing import List

from chess.neighbor import NeighborTuple


class VisitationTable:
    _entries: List[NeighborTuple]
    
    def __init__(self, entries: List[NeighborTuple]=List[NeighborTuple]):
        self._entries = entries
        
    @property
    def entries(self) -> List[NeighborTuple]:
        return self._entries