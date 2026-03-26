# src/logic/coord/service/operation/controller.py

"""
Module: logic.coord.service.operation.manager
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from logic.coord import CoordArithmeticController, CoordBuildProcess, CoordValidationProcess


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
    _build: CoordBuildProcess
    _validation: CoordValidationProcess
    _arithmetic: CoordArithmeticController
    
    def __init__(
            self,
            build: CoordBuildProcess = CoordBuildProcess(),
            validation: CoordValidationProcess = CoordValidationProcess(),
            arithmetic_controller: CoordArithmeticController = CoordArithmeticController(),
    ):
        """
        Args:
            build: CoordBuild
            validation: CoordValidation
        """
        self._build = build
        self._validation = validation
        self._arithmetic = arithmetic_controller
        
    @property
    def build(self) -> CoordBuildProcess:
        return self._build
        
    @property
    def validation(self) ->CoordValidationProcess:
        return self._validation
    
    @property
    def arithmetic(self) -> CoordArithmeticController:
        return self._arithmetic