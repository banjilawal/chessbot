# src/logic/schema/database/search/context/service/operation/controller.py

"""
Module: logic.schema.database.search.context.service.operation.controller
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from model.catalog import SchemaQueryBuilder, SchemaQueryIntegrityWorkers, SchemaQueryValidator


class SchemaQueryOpsController:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations SchemaService supports.
        
    Attributes:
        builder: SchemaQueryBuilder
        validator: SchemaQueryValidator
        workers: SchemaQueryIntegrityWorkers

    Provides:
    
    Super Class:
    """
    _builder: SchemaQueryBuilder
    _validator: SchemaQueryValidator
    _workers: SchemaQueryIntegrityWorkers
    
    def __init__(
            self,
            builder: SchemaQueryBuilder = SchemaQueryBuilder(),
            validator: SchemaQueryValidator = SchemaQueryValidator(),
            workers: SchemaQueryIntegrityWorkers = SchemaQueryIntegrityWorkers(),
    ):
        """
        Args:
            builder: SchemaQueryBuilder
            validator: SchemaQueryValidator
            workers: SchemaQueryIntegrityWorkers
        """
        self._build = builder
        self._validation = validator
        self._arithmetic = workers
        
    @property
    def builder(self) -> SchemaQueryBuilder:
        return self._builder
        
    @property
    def validator(self) ->SchemaQueryValidator:
        return self._validator
    
    @property
    def arithmetic(self) -> SchemaQueryIntegrityWorkers:
        return self._arithmetic