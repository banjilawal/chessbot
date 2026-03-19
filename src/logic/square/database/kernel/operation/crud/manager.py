# src/logic/square/database/kernel/operation/process.py

"""
Module: logic.square.database.kernel.operation.handler
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations

from logic.square import SquareStackPopper, SquareStackPusher


class SquareStackCrudManager:
    """
    Role:
        - Utilities Provider

    Responsibilities:
        1.  Manage insertion/deletion operations for SquareStackService.

    Attributes:
        popper: SquareStackPopper
        pusher: SquareStackServicePusher

    Provides:
        -   push(
                    square: Square,
                    square_stack: SquareStackService,
                    rank_quota_analyzer: SquareStackCapacityAnalyzer = SquareStackCapacityAnalyzer(),
                    collision_detector: SquareCollisionDetectionProcess = SquareCollisionDetectionProcess(),
            ) -> InsertionResult

    Super Class:
    """
    
    _popper: SquareStackPopper
    _pusher: SquareStackPusher
    
    def __init__(
            self,
            popper: SquareStackPopper = SquareStackPopper(),
            pusher: SquareStackPusher = SquareStackPusher(),
    ):
        self._popper = popper
        self._pusher = pusher
        
    @property
    def popper(self) -> SquareStackPopper:
        return self._popper
    
    @property
    def pusher(self) -> SquareStackPusher:
        return self._pusher
    