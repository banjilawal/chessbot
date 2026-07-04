# src/logic/token/service/operation/controller.py

"""
Module: logic.token.service.operation.controller
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass

from analyzer import FriendshipAnalyzer, TokenReadinessAnalyzer
from builder import TokenBuilder
from detection import HomeSquareDetector, TokenCollisionDetector
from operation import TokenHomePlacer, TokenPositionController
from operation.promotion import PawnPromoter
from validation import TokenValidator


@dataclass
class TokenController:
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
        home_placer: TokenDeployer
        position_controller: TokenPositionController
        readiness_analyzer: TokenReadinessAnalyzer

    Provides:
    
    Parent:
    """
    builder: TokenBuilder
    validator: TokenValidator
    promoter: PawnPromoter
    home_placer: TokenHomePlacer
    friendship_analyzer: FriendshipAnalyzer
    collision_detector: TokenCollisionDetector
    position_controller: TokenPositionController
    readiness_analyzer: TokenReadinessAnalyzer
    home_square_detector: HomeSquareDetector
