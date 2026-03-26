# src/logic/coord/service/operation/controller.py

"""
Module: logic.coord.service.operation.manager
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from logic.coord import CoordBuild, CoordValidation


class CoordOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations CoordService supports.
        
    Attributes:
        build: CoordBuild
        validate: CoordValidation
        deployment: CoordDeploymentProcess

    Provides:
    
    Super Class:
    """
    _build: CoordBuild
    _validation: CoordValidation
    
    def __init__(
            self,
            build: CoordBuild = CoordBuild(),
            validation: CoordValidation = CoordValidation(),
    ):
        """
        Args:
            build: CoordBuild
            validation: CoordValidation
        """
        self._build = build
        self._validation = validation
        
    @property
    def build(self) -> CoordBuild:
        return self._build
        
    @property
    def validation(self) ->CoordValidation:
        return self._validation