# src/logic/token/service/operation/controller.py

"""
Module: logic.token.service.operation.controller
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from analyzer import FriendshipAnalyzer, TokenReadinessAnalyzer
from builder import TokenBuilder
from detection import TokenCollisionDetector
from operation import TokenDeployer, TokenPositionController
from operation.promotion import PawnPromoter
from validation import TokenValidator


class TokenServiceController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations TokenService supports.
        
    Attributes:
        WORKER_OP_MENU = Dict[str, Any]
        
        builder: TokenBuilder
        validator: TokenValidator
        promoter: PawnPromoter
        deployer: TokenDeployer
        position_controller: TokenPositionController
        readiness_analyzer: TokenReadinessAnalyzer

    Provides:
    
    Parent:
    """
    WORKER_OP_MENU = {
        "build": TokenBuilder,
        "validate": TokenValidator,
        "promote": PawnPromoter,
        "deploy": TokenDeployer,
        "readiness_analysis": TokenReadinessAnalyzer,
        "control_position": TokenPositionController,
    }
    
    _builder: TokenBuilder
    _validator: TokenValidator
    _promoter: PawnPromoter
    _deployer: TokenDeployer
    _friendship_analyzer: FriendshipAnalyzer
    _collision_detector: TokenCollisionDetector
    _position_controller: TokenPositionController
    _readiness_analyzer: TokenReadinessAnalyzer
    
    
    def __init__(
            self,
            builder: TokenBuilder | None = TokenBuilder(),
            promoter: PawnPromoter = PawnPromoter(),
            deployer: TokenDeployer = TokenDeployer(),
            validator: TokenValidator = TokenValidator(),
            friendship_analyzer: FriendshipAnalyzer =FriendshipAnalyzer(),
            position_controller: TokenPositionController = TokenPositionController(),
            readiness_analyzer: TokenReadinessAnalyzer = TokenReadinessAnalyzer(),
    ):
        """
        Args:
            promoter: PawnPromoter
            deployer: TokenDeployer
            position_controller: TokenPositionController
            readiness_analyzer: TokenReadinessAnalyzer
        """
        self._builder = builder
        self._promoter = promoter
        self._deployer = deployer
        self._validator = validator
        self._friendship_analyzer = friendship_analyzer
        self._position_controller = position_controller
        self._readiness_analyzer = readiness_analyzer
        
    @property
    def builder(self) -> TokenBuilder:
        return self._builder
        
    @property
    def validator(self) ->TokenValidator:
        return self._validator
        
    @property
    def pawn_promoter(self) -> PawnPromoter:
        return self._promoter
    
    @property
    def friendship_analyzer(self) -> FriendshipAnalyzer:
        return self._frienship_analyzer
    
    @property
    def deployer(self) -> TokenDeployer:
        return self._deployer
    
    @property
    def position(self) -> TokenPositionController:
        return self._position_controller
    
    @property
    def readiness_analyzer(self) -> TokenReadinessAnalyzer:
        return self._readiness_analyzer
