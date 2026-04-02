# src/logic/schema/database/search/context/service/__init__.py

"""
Module: logic.schema.database.search.context.service.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from logic.schema.search import SchemaContextBuilder, SchemaContextOpsController, SchemaContextValidator
from logic.schema.search.resource.context.model import SchemaContext
from logic.system import IntegrityMicroservice, IdFactory

class SchemaContextService(IntegrityMicroservice[SchemaContext]):
    """
    Role:
        -   Microservice API
        -   Stateless Integrity Lifecycle Manager

    Responsibilities:
        1.  Mutates SchemaContext instances
        2.  Ensure SchemaContext integrity and consistency when its state changes.
        3.  Build SchemaContext instances that satisfy integrity contracts
        4.  Maintain the SchemaContext integrity lifecycle.

    Attributes:
        SERVICE_NAME: SchemaContextService

        id: int
        name: name
        controller: SchemaContextOpsController

    Provides:

    Super Class:
        IntegrityMicroservice
    """
    SERVICE_NAME = "SchemaContextService"
    _ops_controller: SchemaContextOpsController
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="SchemaContextService"),
            ops_controller: SchemaContextOpsController = SchemaContextOpsController(),
    ):
        """
        Args:
            id: int
            name: str
            ops_controller: SchemaContextOpsController
        """
        super().__init__(id=id, name=name)
        self._ops_controller = ops_controller
    
    @property
    def builder(self) ->SchemaContextBuilder:
        return self._ops_controller.builder
    
    @property
    def validator(self) ->SchemaContextValidator:
        return self._ops_controller.validator
    
    