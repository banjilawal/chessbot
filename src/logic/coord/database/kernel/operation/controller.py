# src/logic/coord/database/kernel/operation/operation.py

"""
Module: logic.coord.database.kernel.operation.operation
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.system import IntegrityService
from logic.coord import RankQuotaAnalysis, CoordCollisionAnalysis, CoordStackCrudController, CoordService
from logic.coord.database.kernel.operation.deployment.process import CoordStackDeployment


class CoordStackOpsController:
    """
    Role:
        -   Operations Controller

    Responsibilities:
        1.  Provide a single entry point for transactions CoordStackService operates.

    Attributes:
        crud: CoordStackCrudController
        rank_quota_analyzer: RankQuotaAnalysis
        collision_detector: CoordCollisionAnalysis

    Provides:
    Parent:
    """
    _crud: CoordStackCrudController
    _deployment: CoordStackDeployment
    _integrity_service: IntegrityService
    _rank_quota_analyzer: RankQuotaAnalysis
    _collision_detector: CoordCollisionAnalysis
    
    def __init__(
            self,
            crud: CoordStackCrudController = CoordStackCrudController(),
            integrity_service: IntegrityService = IntegrityService(),
            deployment: CoordStackDeployment = CoordStackDeployment(),
            rank_quota_analyzer: RankQuotaAnalysis = RankQuotaAnalysis(),
            collision_detector: CoordCollisionAnalysis = CoordCollisionAnalysis(),
    ):
        self._crud = crud
        self._deployment = deployment
        self._integrity_service = integrity_service
        self._collision_detector = collision_detector
        self._rank_quota_analyzer = rank_quota_analyzer

    @property
    def crud(self) -> CoordStackCrudController:
        return self._crud
    
    @property
    def deployment(self) -> CoordStackDeployment:
        return self._deployment
    
    @property
    def integrity_service(self) -> CoordService:
        return self._integrity_service
    
    @property
    def rank_quota_analyzer(self) -> RankQuotaAnalysis:
        return self._rank_quota_analyzer
    
    @property
    def collision_detector(self) -> CoordCollisionAnalysis:
        return self._collision_detector