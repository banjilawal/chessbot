# src/logic/zone/service/operation/controller.py

"""
Module: logic.zone.service.operation.manager
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from logic.zone import ZoneArithmeticController, ZoneBuilder, ZoneValidationTransaction


class ZoneOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations ZoneService supports.
        
    Attributes:
        build: ZoneBuilder
        validation: ZoneValidationTransaction
        arithmetic_controller: ZoneArithmeticController

    Provides:
    
    Super Class:
    """
    _build: ZoneBuilder
    _validation: ZoneValidationTransaction
    _arithmetic_controller: ZoneArithmeticController
    
    def __init__(
            self,
            build: ZoneBuilder = ZoneBuilder(),
            validation: ZoneValidationTransaction = ZoneValidationTransaction(),
            arithmetic_controller: ZoneArithmeticController = ZoneArithmeticController(),
    ):
        """
        Args:
            build: ZoneBuilder
            validation: ZoneValidationTransaction
            arithmetic_controller: ZoneArithmeticController
        """
        self._build = build
        self._validation = validation
        self._arithmetic = arithmetic_controller
        
    @property
    def build(self) -> ZoneBuilder:
        return self._build
        
    @property
    def validation(self) ->ZoneValidationTransaction:
        return self._validation
    
    @property
    def arithmetic(self) -> ZoneArithmeticController:
        return self._arithmetic