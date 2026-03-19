# src/logic/token/service/operation/manager.py

"""
Module: logic.token.service.operation.manager
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from logic.token import PawnPromotionProcess, TokenCoordHandler, TokenDeploymentProcess, TokenReadinessAnalyzer


class TokenOpsDispatcher:
    """
    Role:
        - Utilities Provider
        
    Responsibilities:
        1.  Provide a single entry point for transactions TokenService runs.
        
    Attributes:
        promotion: PawnPromotionProcess
        deployment: TokenDeploymentProcess
        coord_handler: TokenCoordHandler
        readiness_analyzer: TokenReadinessAnalyzer

    Provides:
    
    Parent:
    """

    _promotion: PawnPromotionProcess
    _deployment: TokenDeploymentProcess
    _coord_handler: TokenCoordHandler
    _readiness_analyzer: TokenReadinessAnalyzer
    
    
    def __init__(
            self,
            promotion: PawnPromotionProcess = PawnPromotionProcess(),
            deployment: TokenDeploymentProcess = TokenDeploymentProcess(),
            coord_handler: TokenCoordHandler = TokenCoordHandler(),
            readiness_analyzer: TokenReadinessAnalyzer = TokenReadinessAnalyzer(),
    ):
        """
        Args:
            promotion: PawnPromotionProcess
            deployment: TokenDeploymentProcess
            coord_handler: TokenCoordHandler
            readiness_analyzer: TokenReadinessAnalyzer
        """
        self._promotion = promotion
        self._deployment = deployment
        self._coord_handler = coord_handler
        self._readiness_analyzer = readiness_analyzer
        
    @property
    def pawn_promotion(self) -> PawnPromotionProcess:
        return self._promotion
    
    @property
    def deployment(self) -> TokenDeploymentProcess:
        return self._deployment
    
    @property
    def coord(self) -> TokenCoordHandler:
        return self._coord_handler
    
    @property
    def readiness_analyzer(self) -> TokenReadinessAnalyzer:
        return self._readiness_analyzer