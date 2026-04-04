# src/logic/schema/database/search/context/service/__init__.py

"""
Module: logic.schema.database.search.context.service.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from system import IntegrityMicroservice, IdFactory
from catalog.schema import SchemaQuery, SchemaQueryBuilder, SchemaQueryOpsController, SchemaQueryValidator


class SchemaQueryService(IntegrityMicroservice[SchemaQuery]):
    """
    Role:
        -   Microservice API
        -   Stateless Integrity Lifecycle Manager

    Responsibilities:
        1.  Mutates SchemaQuery instances
        2.  Ensure SchemaQuery integrity and consistency when its state changes.
        3.  Build SchemaQuery instances that satisfy integrity contracts
        4.  Maintain the SchemaQuery integrity lifecycle.

    Attributes:
        SERVICE_NAME: SchemaQueryService

        id: int
        schema: schema
        controller: SchemaQueryOpsController

    Provides:

    Super Class:
        IntegrityMicroservice
    """
    SERVICE_NAME = "SchemaQueryService"
    _ops_controller: SchemaQueryOpsController
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="SchemaQueryService"),
            ops_controller: SchemaQueryOpsController = SchemaQueryOpsController(),
    ):
        """
        Args:
            id: int
            name: str
            ops_controller: SchemaQueryOpsController
        """
        super().__init__(id=id, name=name)
        self._ops_controller = ops_controller
    
    @property
    def builder(self) ->SchemaQueryBuilder:
        return self._ops_controller.builder
    
    @property
    def validator(self) ->SchemaQueryValidator:
        return self._ops_controller.validator
    
    