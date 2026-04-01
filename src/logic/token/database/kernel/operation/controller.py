# src/logic/token/database/kernel/operation/operation.py

"""
Module: logic.token.database.kernel.operation.operation
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.system import IntegrityMicroservice
from logic.token import RankQuotaAnalysis, TokenCollisionAnalysis, TokenStackCrudController, TokenService
from logic.token.database.kernel.operation.deployment.process import TokenStackDeployment


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
    _crud: TokenStackCrudController
    _deployment: TokenStackDeployment
    _integrity_service: IntegrityMicroservice
    _rank_quota_analyzer: RankQuotaAnalysis
    _collision_detector: TokenCollisionAnalysis
    
    def __init__(
            self,
            crud: TokenStackCrudController = TokenStackCrudController(),
            integrity_service: IntegrityMicroservice = IntegrityMicroservice(),
            deployment: TokenStackDeployment = TokenStackDeployment(),
            rank_quota_analyzer: RankQuotaAnalysis = RankQuotaAnalysis(),
            collision_detector: TokenCollisionAnalysis = TokenCollisionAnalysis(),
    ):
        self._crud = crud
        self._deployment = deployment
        self._integrity_service = integrity_service
        self._collision_detector = collision_detector
        self._rank_quota_analyzer = rank_quota_analyzer

    @property
    def crud(self) -> TokenStackCrudController:
        return self._crud
    
    @property
    def deployment(self) -> TokenStackDeployment:
        return self._deployment
    
    @property
    def integrity_service(self) -> TokenService:
        return self._integrity_service
    
    @property
    def rank_quota_analyzer(self) -> RankQuotaAnalysis:
        return self._rank_quota_analyzer
    
    @property
    def collision_detector(self) -> TokenCollisionAnalysis:
        return self._collision_detector