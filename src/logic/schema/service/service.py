# src/logic/schema/service/validator.py

"""
Module: logic.schema.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from __future__ import annotations

from logic.schema import Schema, SchemaQueryOpsController, SchemaSearchService, SchemaValidator
from logic.system import CatalogService, IdFactory, SearchMicroservice, Validator
from logic.system.collection.adt.catalog.service import E


class SchemaService(CatalogService[Schema]):

    SERVICE_NAME = "SchemaService"
    _ops_controller: SchemaQueryOpsController
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="SchemaService"),
            ops_controller: SchemaQueryOpsController = SchemaQueryOpsController(),
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
    def validator(self) -> SchemaValidator:
        return self._ops_controller.validator
    
    
    @property
    def search_service(self) -> SchemaSearchService:
        return self._ops_controller.
