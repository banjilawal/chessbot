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
from microservice import TokenService
from operation import TokenDeployer, TokenPopper, TokenPusher



class TokenStackController:
    """
    Role:
        -   Operations Controller

    Responsibilities:
        1.  Provide a single entry point for transactions TokenStackService operates.

    Attributes:
        crud: TokenStackCrudController
        rank_quota_analyzer: RankQuotaAnalyzer
        collision_detector: TokenCollisionAnalyst

    Provides:
    Parent:
    """
    _crud: TokenStackCrudController
    _token_deployer: TokenDeployer
    _microservice: TokenService
    _pusher: TokenPusher
    _popper: TokenPopper
    _rank_quota_analyzer: RankQuotaAnalyzer
    _collision_detector: TokenCollisionDetector
    
    def __init__(
            self,
            crud: TokenStackCrudController | None = TokenStackCrudController(),
            microservice: TokenService = TokenService(),
            token_deployer: TokenDeployer | None = TokenDeployer(),
            popper: TokenPopper | None = TokenPopper(),
            pusher: TokenPusher | None = TokenPusher(),
            rank_quota_analyzer: RankQuotaAnalyzer | None = RankQuotaAnalyzer(),
            collision_detector: TokenCollisionDetector | None = None,
    ):
        self._crud = crud
        self._token_deployer = token_deployer
        self._microservice = microservice
        self._pusher = pusher
        self._popper = popper
        self._collision_detector = collision_detector
        self._rank_quota_analyzer = rank_quota_analyzer

    @property
    def crud(self) -> TokenStackCrudController:
        return self._crud
    
    @property
    def token_deployer(self) -> TokenDeployer:
        return self._token_deployer
    
    @property
    def microservice(self) -> TokenService:
        return self._microservice
    
    @property
    def rank_quota_analyzer(self) -> RankQuotaAnalyzer:
        return self._rank_quota_analyzer
    
    @property
    def collision_detector(self) -> TokenCollisionDetector:
        return self._collision_detector