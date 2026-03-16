# src/logic/token/service/handler.manager.py

"""
Module: logic.token.service.handler.manager
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from assurance import Deployment
from logic.token import PawnPromotion, TokenCoordHandler, TokenDeployment, TokenReadinessAnalyzer


class TokenHandler:
    """
    # ROLE: Update Handler, Consistency, Integrity Maintenance, Lifecycle Management

    # RESPONSIBILITIES:
    1.  Ensure integrity and consistency are maintained during the pawn's promotion lifecycle.

    # PARENT:
    None

    # PROVIDES:
    None

    Attributes:
    None

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
    None

    # LOCAL METHODS:

    # INHERITED METHODS:
    None
    """

    _promotion: PawnPromotion
    _deployment: TokenDeployment
    _coord_handler: TokenCoordHandler
    _readiness_analyzer: TokenReadinessAnalyzer
    
    
    def __init__(
            self,
            promotion: PawnPromotion = PawnPromotion(),
            deployment: TokenDeployment = TokenDeployment(),
            coord_handler: TokenCoordHandler = TokenCoordHandler(),
            readiness_analyzer: TokenReadinessAnalyzer = TokenReadinessAnalyzer(),
    ):
        """
        Args:
            promotion: PawnPromotion
            deployment: TokenDeployment
            coord_handler: TokenCoordHandler
            readiness_analyzer: TokenReadinessAnalyzer
        """
        self._promotion = promotion
        self._deployment = deployment
        self._coord_handler = coord_handler
        self._readiness_analyzer = readiness_analyzer
        
    @property
    def pawn_promotion(self) -> PawnPromotion:
        return self._promotion
    
    @property
    def deployment(self) -> TokenDeployment:
        return self._deployment
    
    @property
    def coord(self) -> TokenCoordHandler:
        return self._coord_handler
    
    @property
    def readiness_analyzer(self) -> TokenReadinessAnalyzer:
        return self._readiness_analyzer