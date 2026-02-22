# src/chess/square/database/core/util/util.py

"""
Module: chess.square.database.core.util.util
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from chess.square import SquareStackAnalyzer


class SquareStackUtil:
    _stats_analyzer: SquareStackAnalyzer
    
    def __init__(
            self,
            stats_analyzer: SquareStackAnalyzer = SquareStackAnalyzer(),
    ):
        self._stats_analyzer = stats_analyzer
        
    @property
    def stats_analyzer(self) -> SquareStackAnalyzer:
        return self._stats_analyzer