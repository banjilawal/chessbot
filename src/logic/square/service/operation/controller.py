# src/logic/square/service/operation/controller.py

"""
Module: logic.square.service.operation.manager
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from logic.square import (
    VisitationController, SquareBuild, SquarePositionController, SquareCollisionAnalysis,
    SquareReadinessAnalysis, SquareValidation
)


class SquareOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations SquareService supports.
        
    Attributes:
        build: SquareBuild
        validate: SquareValidation
        vistation: VisitationController
        collision_detection: SquareCollisionAnalysis
        position_controller: SquarePositionController
        readiness_analyzer: SquareReadinessAnalysis

    Provides:
    
    Parent:
    """
    _build: SquareBuild
    _validation: SquareValidation
    _vistation: VisitationController
    _collision_detection: SquareCollisionAnalysis

    
    
    def __init__(
            self,
            build: SquareBuild = SquareBuild(),
            validation: SquareValidation = SquareValidation(),
            vistation: VisitationController = VisitationController(),
            collision_detection: SquareCollisionAnalysis = SquareCollisionAnalysis(),
    ):
        """
        Args:
            vistation: VisitationController
            collision_detection: SquareCollisionAnalysis
            position_controller: SquarePositionController
            readiness_analyzer: SquareReadinessAnalysis
        """
        self._vistation = vistation
        self._collision_detection = collision_detection
        
    @property
    def build(self) -> SquareBuild:
        return self._build
        
    @property
    def validation(self) ->SquareValidation:
        return self._validation
        
    @property
    def visitation(self) -> VisitationController:
        return self._vistation
    
    @property
    def collision_detection(self) -> SquareCollisionAnalysis:
        return self._collision_detection