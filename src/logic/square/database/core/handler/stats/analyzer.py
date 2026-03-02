# src/logic/square/database/core/util/stats/analyzer.py

"""
Module: logic.square.database.core.util.stats.analyzer
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from typing import List

from logic.square import Square, SquareStackService, SquareStackFullException
from logic.system import ComputationResult, LoggingLevelRouter, NullException


class SquareStackAnalyzer:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def occupied_squares_count(cls, squares: List[Square]) -> ComputationResult[int]:
        occupations = [square for square in squares if square.is_occupied]
        
        # --- Send their count. ---#
        return ComputationResult.success(len(occupations))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def empty_squares_count(cls, squares: List[Square]) -> ComputationResult[int]:
        # --- List comprehend the empty squares. ---#
        empties = [square for square in squares if square.is_empty]
        
        # --- Send their count. ---#
        return ComputationResult.success(len(empties))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def available_capacity(cls, squares: List[Square], capacity: int) -> ComputationResult[int]:
        return ComputationResult.success(capacity - len(squares))