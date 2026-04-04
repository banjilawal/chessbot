# src/logic/schema/service/validator.py

"""
Module: logic.schema.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from __future__ import annotations

from logic.system import CatalogService, IdFactory
from catalog.schema import (
    Schema, SchemaLookupService, SchemaOpsController, SchemaPropertyValuesReporter, SchemaValidator
)


class SchemaService(CatalogService[Schema]):
    """
    Role:
        -   Data layer
        -   Microservice API
        -   Interface

    Responsibilities:
        1.  Adds functionality to the Schema table with without tight coupling

    Attributes:
        id: int
        name: str
        validator: Validator[E]
        search: SearchMicroservice[E]

    Provides:

    Super class:
        CatalogService
    """
    
    SERVICE_NAME = "SchemaService"
    _ops_controller: SchemaOpsController
    _schema: Schema
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="SchemaService"),
            ops_controller: SchemaOpsController = SchemaOpsController(),
    ):
        """
        Args:
            id: int
            name: str
            ops_controller: SchemaQueryOpsController
        """
        super().__init__(id=id, name=name,)
        self._ops_controller = ops_controller

        
    @property
    def schema(self) -> Schema:
        return self._schema
        
    @property
    def validator(self) -> SchemaValidator:
        return self._ops_controller.validator
    
    @property
    def search_service(self) -> SchemaLookupService:
        return self._ops_controller.search
    
    @property
    def values(self) -> SchemaPropertyValuesReporter:
        return self._ops_controller.property_values

