# src/logic/token/service/operation/manager.py

"""
Module: logic.token.service.operation.manager
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from logic.token import (
    PawnPromotionProcess, TokenBuild, TokenPositionController, TokenDeploymentProcess,
    TokenReadinessAnalysis, TokenValidation
)


class TokenOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations TokenService supports.
        
    Attributes:
        build: TokenBuild
        validate: TokenValidation
        promotion: PawnPromotionProcess
        deployment: TokenDeploymentProcess
        position_controller: TokenPositionController
        readiness_analyzer: TokenReadinessAnalysis

    Provides:
    
    Parent:
    """
    _build: TokenBuild
    _validation: TokenValidation
    _promotion: PawnPromotionProcess
    _deployment: TokenDeploymentProcess
    _position_controller: TokenPositionController
    _readiness_analyzer: TokenReadinessAnalysis
    
    
    def __init__(
            self,
            build: TokenBuild = TokenBuild(),
            validation: TokenValidation = TokenValidation(),
            promotion: PawnPromotionProcess = PawnPromotionProcess(),
            deployment: TokenDeploymentProcess = TokenDeploymentProcess(),
            position_controller: TokenPositionController = TokenPositionController(),
            readiness_analyzer: TokenReadinessAnalysis = TokenReadinessAnalysis(),
    ):
        """
        Args:
            promotion: PawnPromotionProcess
            deployment: TokenDeploymentProcess
            position_controller: TokenPositionController
            readiness_analyzer: TokenReadinessAnalysis
        """
        self._promotion = promotion
        self._deployment = deployment
        self._position_controller = position_controller
        self._readiness_analyzer = readiness_analyzer
        
    @property
    def build(self) -> TokenBuild:
        return self._build
        
    @property
    def validation(self) ->TokenValidation:
        return self._validation
        
    @property
    def pawn_promotion(self) -> PawnPromotionProcess:
        return self._promotion
    
    @property
    def deployment(self) -> TokenDeploymentProcess:
        return self._deployment
    
    @property
    def position(self) -> TokenPositionController:
        return self._position_controller
    
    @property
    def readiness_analyzer(self) -> TokenReadinessAnalysis:
        return self._readiness_analyzer