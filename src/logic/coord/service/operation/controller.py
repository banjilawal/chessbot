# src/logic/coord/service/operation/controller.py

"""
Module: logic.coord.service.operation.manager
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from logic.coord import CoordArithmeticController, CoordBuildTransaction, CoordValidationTransaction


class CoordOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations CoordService supports.
        
    Attributes:
        build: CoordBuildTransaction
        validation: CoordValidationTransaction
        arithmetic_controller: CoordArithmeticController

    Provides:
    
    Super Class:
    """
    _build: CoordBuildTransaction
    _validation: CoordValidationTransaction
    _arithmetic_controller: CoordArithmeticController
    
    def __init__(
            self,
            build: CoordBuildTransaction = CoordBuildTransaction(),
            validation: CoordValidationTransaction = CoordValidationTransaction(),
            arithmetic_controller: CoordArithmeticController = CoordArithmeticController(),
    ):
        """
        Args:
            build: CoordBuildTransaction
            validation: CoordValidationTransaction
            arithmetic_controller: CoordArithmeticController
        """
        self._build = build
        self._validation = validation
        self._arithmetic = arithmetic_controller
        
    @property
    def build(self) -> CoordBuildTransaction:
        return self._build
        
    @property
    def validation(self) ->CoordValidationTransaction:
        return self._validation
    
    @property
    def arithmetic(self) -> CoordArithmeticController:
        return self._arithmetic