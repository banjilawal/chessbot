# src/suite/bootstrapper/toolkit.py

"""
Module: suite.bootstrapper.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from analyzer import FriendshipAnalyzer, TokenReadinessAnalyzer
from builder import TokenBuilder
from detection import TokenCollisionDetector, TokenHomeDetector
from model import Token
from operation import TokenHomePlacer, TokenPositionController
from operation.promotion import PawnPromoter
from suite import ModelOperationSuite
from toolkit import TokenToolkit
from validator import TokenValidator


class TokenOperationSuite(ModelOperationSuite[Token]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a Token.

    Attributes:
        toolkit: TokenToolkit
        builder: TokenBuilder
        validator: TokenValidator

    Provides:

    Super Class:
        Suite

    Notes:
        -   Suite for an empty class which makes managing toolkits easier.
        -   Any toolkits for a suite should be a Suite subclass.
    """
    toolkit: TokenToolkit = TokenToolkit()
    builder: TokenBuilder = TokenBuilder()
    validator: TokenValidator = TokenValidator()
    
    promoter: PawnPromoter = PawnPromoter()
    home_placer: TokenHomePlacer = TokenHomePlacer()
    friendship_analyzer: FriendshipAnalyzer = FriendshipAnalyzer()
    collision_detector: TokenCollisionDetector = TokenCollisionDetector()
    position_controller: TokenPositionController
    readiness_analyzer: TokenReadinessAnalyzer = TokenReadinessAnalyzer()
    home_detector: TokenHomeDetector = TokenHomeDetector()

