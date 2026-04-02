# src/logic/schema/database/search/context/service/operation/controller.py

"""
Module: logic.schema.database.search.context.service.operation.controller
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from logic.schema import SchemaContextBuilder, SchemaContextIntegrityWorkers, SchemaContextValidator


class SchemaContextOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations SchemaService supports.
        
    Attributes:
        builder: SchemaContextBuilder
        validator: SchemaContextValidator
        workers: SchemaContextIntegrityWorkers

    Provides:
    
    Super Class:
    """
    _builder: SchemaContextBuilder
    _validator: SchemaContextValidator
    _workers: SchemaContextIntegrityWorkers
    
    def __init__(
            self,
            builder: SchemaContextBuilder = SchemaContextBuilder(),
            validator: SchemaContextValidator = SchemaContextValidator(),
            workers: SchemaContextIntegrityWorkers = SchemaContextIntegrityWorkers(),
    ):
        """
        Args:
            builder: SchemaContextBuilder
            validator: SchemaContextValidator
            workers: SchemaContextIntegrityWorkers
        """
        self._build = builder
        self._validation = validator
        self._arithmetic = workers
        
    @property
    def builder(self) -> SchemaContextBuilder:
        return self._builder
        
    @property
    def validator(self) ->SchemaContextValidator:
        return self._validator
    
    @property
    def arithmetic(self) -> SchemaContextIntegrityWorkers:
        return self._arithmetic