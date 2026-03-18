# src/logic/square/database/kernel/util/util.py

"""
Module: logic.square.database.kernel.operation.util
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.square import SquareStackCapacityAnalyzer, SquareCollisionDetector, SquareStackCrudManager


class SquareStackOpsDispatcher:
    """
    Role:
        - Utilities Provider

    Responsibilities:
        1.  Provide a single entry point for transactions SquareStackService operates.

    Attributes:
        crud: SquareStackCrudManager
        rank_quota_analyzer: SquareStackCapacityAnalyzer
        collision_detector: SquareCollisionDetector

    Provides:
    Parent:
    """
    _crud: SquareStackCrudManager
    _rank_quota_analyzer: SquareStackCapacityAnalyzer
    _collision_detector: SquareCollisionDetector
    
    def __init__(
            self,
            crud: SquareStackCrudManager = SquareStackCrudManager(),
            rank_quota_analyzer: SquareStackCapacityAnalyzer = SquareStackCapacityAnalyzer(),
            collision_detector: SquareCollisionDetector = SquareCollisionDetector(),
    ):
        self._crud = crud
        self._collision_detector = collision_detector
        self._rank_quota_analyzer = rank_quota_analyzer

    @property
    def crud(self) -> SquareStackCrudManager:
        return self._crud
    
    @property
    def rank_quota_analyzer(self) -> SquareStackCapacityAnalyzer:
        return self._rank_quota_analyzer
    
    @property
    def collision_detector(self) -> SquareCollisionDetector:
        return self._collision_detector