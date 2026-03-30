# src/logic/zone/service/operation/controller.py

"""
Module: logic.zone.service.operation.manager
Author: Banji Lawal
Created: 2026-03-29
version: 1.0.0
"""

from __future__ import annotations

from logic.zone import ZoneBuilder, ZoneValidator


class ZoneOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations ZoneService supports.
        
    Attributes:
        builder: ZoneBuilder
        validator: ZoneValidator

    Provides:
    
    Super Class:
    """
    _builder: ZoneBuilder
    _validator: ZoneValidator
    
    def __init__(
            self,
            builder: ZoneBuilder = ZoneBuilder(),
            validator: ZoneValidator = ZoneValidator(),
    ):
        """
        Args:
            builder: ZoneBuilder
            validator: ZoneValidator
        """
        self._builder = builder
        self._validator = validator
        
    @property
    def builder(self) -> ZoneBuilder:
        return self._builder
        
    @property
    def validator(self) ->ZoneValidator:
        return self._validator