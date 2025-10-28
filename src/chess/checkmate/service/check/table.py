# src/chess/checkmate/service.py

"""
Module: chess.checkmate.table
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""

from typing import List

from chess.checkmate import CheckRecord


class CheckRecordTable:
    _posts: List[CheckRecord]
    
    def __init__(self):
        self._posts = []
        
    @property
    def postings(self) -> List[CheckRecord]:
        return self._posts