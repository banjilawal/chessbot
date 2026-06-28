# src/logic/token/database/kernel/operation/operation.py

"""
Module: logic.token.database.kernel.operation.operation
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from analyzer import RankQuotaAnalyzer
from controller.stack.crud.token import TokenStackCrudController
from detector import TokenCollisionDetector
from operation import TokenPusher

from model.token import TokenDeployer


class TokenStackController:
    """
    Role:
        -   Operations Controller

    Responsibilities:
        1.  Provide a single entry point for transactions TokenStackService operates.

    Attributes:
        crud: TokenStackCrudController
        rank_quota_analyzer: RankQuotaAnalysis
        collision_detector: TokenCollisionAnalyst

    Provides:
    Parent:
    """
    _crud: TokenStackCrudController
    _token_deployer: TokenDeployer
    _integrity_service: IntegrityMicroservice
    _pusher: TokenPusher
    _rank_quota_analyzer: RankQuotaAnalyzer
    _collision_detector: TokenCollisionDetector
    
    def __init__(
            self,
            crud: TokenStackCrudController | None = TokenStackCrudController(),
            integrity_service: IntegrityMicroservice = IntegrityMicroservice(),
            token_deployer: TokenDeployer | None = TokenDeployer(),
            pusher: TokenPusher | None = TokenPusher(),
            rank_quota_analyzer: RankQuotaAnalyzer | None = RankQuotaAnalyzer(),
            collision_detector: TokenCollisionDetector | None = None,
    ):
        self._crud = crud
        self._token_deployer = token_deployer
        self._integrity_service = integrity_service
        self._pusher = pusher
        self._collision_detector = collision_detector
        self._rank_quota_analyzer = rank_quota_analyzer

    @property
    def crud(self) -> TokenStackCrudController:
        return self._crud
    
    @property
    def token_deployer(self) -> TokenDeployer:
        return self._token_deployer
    
    @property
    def integrity_service(self) -> TokenService:
        return self._integrity_service
    
    @property
    def rank_quota_analyzer(self) -> RankQuotaAnalysis:
        return self._rank_quota_analyzer
    
    @property
    def collision_detector(self) -> TokenCollisionDetector:
        return self._collision_detector