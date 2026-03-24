# src/logic/token/database/kernel/operation/operation.py

"""
Module: logic.token.database.kernel.operation.operation
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.token import RankQuotaAnalysis, TokenCollisionAnalysis, TokenStackCrudManager


class TokenStackOpsController:
    """
    Role:
        -   Operations Controller

    Responsibilities:
        1.  Provide a single entry point for transactions TokenStackService operates.

    Attributes:
        crud: TokenStackCrudController
        rank_quota_analyzer: RankQuotaAnalysis
        collision_detector: TokenCollisionAnalysis

    Provides:
    Parent:
    """
    _crud: TokenStackCrudManager
    _rank_quota_analyzer: RankQuotaAnalysis
    _collision_detector: TokenCollisionAnalysis
    
    def __init__(
            self,
            crud: TokenStackCrudManager = TokenStackCrudManager(),
            rank_quota_analyzer: RankQuotaAnalysis = RankQuotaAnalysis(),
            collision_detector: TokenCollisionAnalysis = TokenCollisionAnalysis(),
    ):
        self._crud = crud
        self._collision_detector = collision_detector
        self._rank_quota_analyzer = rank_quota_analyzer

    @property
    def crud(self) -> TokenStackCrudManager:
        return self._crud
    
    @property
    def rank_quota_analyzer(self) -> RankQuotaAnalysis:
        return self._rank_quota_analyzer
    
    @property
    def collision_detector(self) -> TokenCollisionAnalysis:
        return self._collision_detector