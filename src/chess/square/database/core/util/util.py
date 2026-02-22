# src/chess/square/database/core/util/util.py

"""
Module: chess.square.database.core.util.util
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from chess.square import OccupationService, SquareStackAnalyzer


class SquareStackUtil:
    _stats_analyzer: SquareStackAnalyzer
    _occupation_service: OccupationService
    
    def __init__(
            self,
            stats_analyzer: SquareStackAnalyzer = SquareStackAnalyzer(),
            occupation_service: OccupationService = OccupationService(),
    ):
        self._stats_analyzer = stats_analyzer
        self._occupation_service = occupation_service
        
    @property
    def stats_analyzer(self) -> SquareStackAnalyzer:
        return self._stats_analyzer
    
    @property
    def occupation_service(self) -> OccupationService:
        return self._occupation_service