# src/logic/token/database/kernel/util/util.py

"""
Module: logic.token.database.kernel.operation.util
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.token import RankQuotaAnalyzer, TokenCollisionDetector, TokenStackCrudManager


class TokenStackOpsDispatcher:
    """
    Role:
        - Utilities Provider

    Responsibilities:
        1.  Provide a single entry point for transactions TokenStackService runs.

    Attributes:
        crud: TokenStackCrudManager
        rank_quota_analyzer: RankQuotaAnalyzer
        collision_detector: TokenCollisionDetector

    Provides:
    Parent:
    """
    _crud: TokenStackCrudManager
    _rank_quota_analyzer: RankQuotaAnalyzer
    _collision_detector: TokenCollisionDetector
    
    def __init__(
            self,
            crud: TokenStackCrudManager = TokenStackCrudManager(),
            rank_quota_analyzer: RankQuotaAnalyzer = RankQuotaAnalyzer(),
            collision_detector: TokenCollisionDetector = TokenCollisionDetector(),
    ):
        self._crud = crud
        self._collision_detector = collision_detector
        self._rank_quota_analyzer = rank_quota_analyzer

    @property
    def crud(self) -> TokenStackCrudManager:
        return self._crud
    
    @property
    def rank_quota_analyzer(self) -> RankQuotaAnalyzer:
        return self._rank_quota_analyzer
    
    @property
    def collision_detector(self) -> TokenCollisionDetector:
        return self._collision_detector