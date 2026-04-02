# src/logic/schema/service/operation/controller.py

"""
Module: logic.schema.service.operation.controller
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations


from logic.schema import (
    PawnPromoter, SchemaBuilder, SchemaPositionController, SchemaDeployer,
    SchemaReadinessAnalyzer, SchemaService, SchemaValidator
)
from logic.schema.service.operation.properties.reporter import SchemaPropertyValuesReporter


class SchemaOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations SchemaService supports.
        
    Attributes:
        property_values_reporter
        validator: SchemaValidator
        search_service: SchemaService

    Provides:
    
    Parent:
    """
    
    _validator: SchemaValidator
    _search_service: SchemaService
    _property_values_reporter: SchemaPropertyValuesReporter

    
    
    def __init__(
            self,
            validator: SchemaValidator = SchemaValidator(),
            search_service: SchemaService = SchemaService(),
            property_values_reporter: SchemaPropertyValuesReporter 
                = SchemaPropertyValuesReporter()
            ,
    ):
        """
        Args:
            property_values_reporter
            validator: SchemaValidator
            search_service: SchemaService
        """
        self._validator = validator
        self._search_service = search_service
        self._property_values_reporter = property_values_reporter

    @property
    def validator(self) ->SchemaValidator:
        return self._validator
    
    @property
    def search_service(self) -> SchemaService:
        return self._search_service
        
    @property
    def property_values_(self) -> SchemaPropertyValuesReporter:
        return self._property_values_reporter
