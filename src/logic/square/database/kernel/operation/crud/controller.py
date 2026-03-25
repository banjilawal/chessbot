# src/logic/square/database/kernel/operation/exception.py

"""
Module: logic.square.database.kernel.operation.handler
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations

from logic.square import SquareContext, SquareContextService, SquareStackPopper, SquareStackPush


class SquareStackCrudController:
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
                    rank_quota_analyzer: SquareStackCapacityAnalysis = SquareStackCapacityAnalysis(),
                    collision_detector: SquareCollisionAnalysis = SquareCollisionAnalysis(),
            ) -> InsertionResult

    Super Class:
    """
    
    _popper: SquareStackPopper
    _pusher: SquareStackPush
    _query: SquareContextService
    
    def __init__(
            self,
            popper: SquareStackPopper = SquareStackPopper(),
            pusher: SquareStackPush = SquareStackPush(),
            query: SquareContextService = SquareContextService(),
    ):
        self._popper = popper
        self._pusher = pusher
        self._query = query
        
    @property
    def popper(self) -> SquareStackPopper:
        return self._popper
    
    @property
    def pusher(self) -> SquareStackPush:
        return self._pusher
    
    @property
    def query(self) -> SquareContextService:
        return self._query
    