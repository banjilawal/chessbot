# src/logic/token/service/operation/manager.py

"""
Module: logic.token.service.operation.manager
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from logic.token import PawnPromotionProcess, TokenPositionController, TokenDeploymentProcess, TokenReadinessAnalysis


class TokenOpsController:
    """
    Role:
        - Utilities Provider
        
    Responsibilities:
        1.  Provide a single entry point for transactions TokenService runs.
        
    Attributes:
        promotion: PawnPromotionProcess
        deployment: TokenDeploymentProcess
        position_controller: TokenPositionController
        readiness_analyzer: TokenReadinessAnalysis

    Provides:
    
    Parent:
    """

    _promotion: PawnPromotionProcess
    _deployment: TokenDeploymentProcess
    _position_controller: TokenPositionController
    _readiness_analyzer: TokenReadinessAnalysis
    
    
    def __init__(
            self,
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