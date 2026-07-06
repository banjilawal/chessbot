# src/microservice/catalog/schema/microservice.py

"""
Module: microservice.catalog.schema.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model.catalog import Schema
from microservice import CatalogService


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
        return self._ops_controller.execute
    
    @property
    def search_service(self) -> SchemaLookupService:
        return self._ops_controller.build
    
    @property
    def values(self) -> SchemaPropertyValuesReporter:
        return self._ops_controller.property_values

