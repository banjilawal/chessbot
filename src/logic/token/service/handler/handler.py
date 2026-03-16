# src/logic/token/service/handler.manager.py

"""
Module: logic.token.service.handler.manager
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from logic.token import PawnPromoter, TokenDeployer, TokenReadinessAnalyzer
from logic.token.service.handler.coord.handler import TokenCoordHandler


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
    _promoter: PawnPromoter
    _deployer: TokenDeployer
    _coord_handler: TokenCoordHandler
    _readiness_analyzer: TokenReadinessAnalyzer
    
    
    def __init__(
            self,
            promoter: PawnPromoter = PawnPromoter(),
            coord_handler: TokenCoordHandler = TokenCoordHandler(),
            readiness_analyzer: TokenReadinessAnalyzer = TokenReadinessAnalyzer(),
    ):
        """
        Args:
            promoter: PawnPromoter
            coord_handler: TokenCoordHandler
            readiness_analyzer: TokenReadinessAnalyzer
        """
        self._promoter = promoter
        self._coord_handler = coord_handler
        self._readiness_analyzer = readiness_analyzer
        
    @property
    def pawn_promoter(self) -> PawnPromoter:
        return self._promoter
    
    @property
    def coord(self) -> TokenCoordHandler:
        return self._coord_handler
    
    @property
    def readiness_analyzer(self) -> TokenReadinessAnalyzer:
        return self._readiness_analyzer