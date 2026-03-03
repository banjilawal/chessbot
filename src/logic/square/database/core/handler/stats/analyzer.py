# src/logic/square/database/core/util/stats/analyzer.py

"""
Module: logic.square.database.core.handler.stats.analyzer
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.square import SquareStackService, SquareStackFullException
from logic.system import ComputationResult, LoggingLevelRouter, NullException


class SquareStackCountsAnalyzer:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def occupied_squares_count(cls, square_stack: SquareStackService) -> ComputationResult[int]:
        occupations = [square for square in square_stack.items if square.is_occupied]
        
        # --- Send their count. ---#
        return ComputationResult.success(len(occupations))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def empty_squares_count(cls, square_stack: SquareStackService) -> ComputationResult[int]:
        # --- List comprehend the empty squares. ---#
        empties = [square for square in square_stack.items if square.is_empty]
        
        # --- Send their count. ---#
        return ComputationResult.success(len(empties))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def available_capacity(cls, square_stack: SquareStackService) -> ComputationResult[int]:
        return ComputationResult.success(square_stack.capacity - square_stack.size)