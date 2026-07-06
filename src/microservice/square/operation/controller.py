# src/logic/square/service/operation/controller.py

"""
Module: logic.square.service.operation.manager
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass

from detection import SquareCollisionDetector
from builder import SquareBuilder
from validator import SquareValidator


@dataclass
class SquareOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations SquareService supports.
        
    Attributes:
        builder: SquareBuilder
        validator: SquareValidator
        vistation_controller: VisitationController
        collision_detector: SquareCollisionAnalyst
        position_controller: SquarePositionController
        readiness_analyzer: SquareReadinessAnalysis

    Provides:
    
    Parent:
    """
    builder: SquareBuilder
    validator: SquareValidator
    visitation_controller: VisitationController
    collision_detector: SquareCollisionDetector
