# src/logic/token/database/core/util/stats/analyzer.py

"""
Module: logic.token.database.core.handler.stats.analyzer
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.token import TokenStackService, TokenStackFullException
from logic.system import ComputationResult, LoggingLevelRouter, NullException


class TokenStackCountsAnalyzer:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def occupied_tokens_count(cls, token_stack: TokenStackService) -> ComputationResult[int]:
        occupations = [token for token in token_stack.items if token.is_occupied]
        
        # --- Send their count. ---#
        return ComputationResult.success(len(occupations))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def empty_tokens_count(cls, token_stack: TokenStackService) -> ComputationResult[int]:
        # --- List comprehend the empty tokens. ---#
        empties = [token for token in token_stack.items if token.is_empty]
        
        # --- Send their count. ---#
        return ComputationResult.success(len(empties))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def available_capacity(cls, token_stack: TokenStackService) -> ComputationResult[int]:
        return ComputationResult.success(token_stack.capacity - token_stack.size)