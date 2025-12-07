# src/chess/checkmate/entity_service.py

"""
Module: chess.checkmate.table
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""

from typing import List

from chess.checkmate import KingLocationRecord
from chess.checkmate.service.location.search import KingLocationSearch


class KingMonitoringService:
    
    _search_service: KingLocationSearch
    _location_table: List[KingLocationRecord]
    
    def __init__(self):
        self._posts = []
        
    @property
    def location_table(self) -> List[KingLocationRecord]:
        return self._location_table