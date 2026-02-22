# src/chess/square/database/core/util/stats/analyzer.py

"""
Module: chess.square.database.core.util.stats.analyzer
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from chess.square import SquareStack, SquareStackFullException
from chess.system import ComputationResult, LoggingLevelRouter, NullException


class SquareStackAnalyzer:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def occupied_squares_count(cls, stack: SquareStack) -> ComputationResult[int]:
        """
        # ACTION:
            1.  Iterate through the squares. If a square is occupied increment the counter.
            2.  After the loop send total in the ComputationResult.
        # PARAMETERS:
            None
        # RETURNS:
            *   ComputationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int.
        # RAISES:
            None
        """
        method = "SquareStack.occupied_square_count"
        
        # Handle the case that the stack is null
        if stack is None:
            # Send the exception chain on failure.
            return ComputationResult.failure(
                NullException(f"{method}: Cannot count occupied squares in a null SquareStack.")
            )
        
        occupied_square_count = 0
        # Loop through the squares to get tally of occupied squares.
        for square in stack:
            if square.is_occupied:
                occupied_square_count += 1
        # Send the total in the ComputationResult.
        return ComputationResult.success(occupied_square_count)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def empty_squares_count(cls, stack: SquareStack) -> ComputationResult[int]:
        """
        # ACTION:
            1.  Iterate through the squares. If a square is occupied increment the counter.
            2.  After the loop send total in the ComputationResult.
        # PARAMETERS:
            None
        # RETURNS:
            *   ComputationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int.
        # RAISES:
            None
        """
        method = "SquareStack.occupied_square_count"
        
        # Handle the case that the stack is null
        if stack is None:
            # Send the exception chain on failure.
            return ComputationResult.failure(
                NullException(f"{method}: Cannot count empty squares in a null SquareStack.")
            )
        
        empty_square_count = 0
        # Loop through the squares to get tally of occupied squares.
        for square in stack:
            if square.is_empty:
                empty_square_count += 1
        # Send the total in the ComputationResult.
        return ComputationResult.success(empty_square_count)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def available_capacity(cls, stack: SquareStack) -> ComputationResult[int]:
        """
        # ACTION:
            1.  Iterate through the squares. If a square is occupied increment the counter.
            2.  After the loop send total in the ComputationResult.
        # PARAMETERS:
            None
        # RETURNS:
            *   ComputationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int.
        # RAISES:
            None
        """
        method = "SquareStack.occupied_square_count"
        
        # Handle the case that the stack is null
        if stack is None:
            # Send the exception chain on failure.
            return ComputationResult.failure(
                NullException(f"{method}: Cannot count empty squares in a null SquareStack.")
            )
        
        available_capacity = stack.capacity - stack.size
        # Handle the case that no more squares can be added to the stack
        if available_capacity < 1:
            # Send the exception chain on failure.
            return ComputationResult.failure(
                SquareStackFullException(f"{method}: {SquareStackFullException.DEFAULT_MESSAGE}")
            )
        
        return ComputationResult.success(available_capacity)