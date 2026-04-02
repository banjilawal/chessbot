# src/logic/coord/service/operation/controller.py

"""
Module: logic.coord.service.operation.controller
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from logic.coord import CoordArithmeticController, CoordBuilder, CoordValidator


class CoordOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations CoordService supports.
        
    Attributes:
        builder: CoordBuilder
        validator: CoordValidator
        arithmetic_controller: CoordArithmeticController

    Provides:
    
    Super Class:
    """
    _builder: CoordBuilder
    _validator: CoordValidator
    _arithmetic_controller: CoordArithmeticController
    
    def __init__(
            self,
            builder: CoordBuilder = CoordBuilder(),
            validator: CoordValidator = CoordValidator(),
            arithmetic_controller: CoordArithmeticController = CoordArithmeticController(),
    ):
        """
        Args:
            builder: CoordBuilder
            validator: CoordValidator
            arithmetic_controller: CoordArithmeticController
        """
        self._build = builder
        self._validation = validator
        self._arithmetic = arithmetic_controller
        
    @property
    def builder(self) -> CoordBuilder:
        return self._builder
        
    @property
    def validator(self) ->CoordValidator:
        return self._validatior
    
    @property
    def arithmetic(self) -> CoordArithmeticController:
        return self._arithmetic