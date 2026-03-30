# src/logic/coord/query/context/service/operation/controller.py

"""
Module: logic.coord.query.context.service.operation.controller
Author: Banji Lawal
Created: 2026-03-29
version: 1.0.0
"""

from __future__ import annotations

from logic.coord import CoordContextBuilder, CoordContextValidator


class CoordContextContextOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations CoordContextService supports.
        
    Attributes:
        builder: CoordContextBuilder
        validator: CoordContextValidator

    Provides:
    
    Super Class:
    """
    _builder: CoordContextBuilder
    _validator: CoordContextValidator
    
    def __init__(
            self,
            builder: CoordContextBuilder = CoordContextBuilder(),
            validator: CoordContextValidator = CoordContextValidator(),
    ):
        """
        Args:
            builder: CoordContextBuilder
            validator: CoordContextValidator
        """
        self._builder = builder
        self._validator = validator
        
    @property
    def builder(self) -> CoordContextBuilder:
        return self._builder
        
    @property
    def validator(self) ->CoordContextValidator:
        return self._validator