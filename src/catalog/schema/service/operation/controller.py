# src/logic/schema/service/operation/controller.py

"""
Module: logic.schema.service.operation.controller
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from catalog.schema import SchemaLookupService, SchemaValidator
from catalog.schema.service.operation import SchemaPropertyValuesReporter


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
    _schema_lookup: SchemaLookupService
    _property_values_reporter: SchemaPropertyValuesReporter

    def __init__(
            self,
            validator: SchemaValidator = SchemaValidator(),
            schema_lookup: SchemaLookupService = SchemaLookupService(),
            property_values_reporter: SchemaPropertyValuesReporter = SchemaPropertyValuesReporter()
            ,
    ):
        """
        Args:
            property_values_reporter
            validator: SchemaValidator
            schema_lookup: SchemaService
        """
        self._validator = validator
        self._schema_lookup = schema_lookup
        self._property_values_reporter = property_values_reporter

    @property
    def validator(self) -> SchemaValidator:
        return self._validator
    
    @property
    def search(self) -> SchemaLookupService:
        return self._schema_lookup
        
    @property
    def property_values(self) -> SchemaPropertyValuesReporter:
        return self._property_values_reporter
