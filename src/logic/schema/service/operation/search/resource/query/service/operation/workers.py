# src/logic/schema/database/search/context/service/operation/workers.py

"""
Module: logic.schema.database.search.context.service.operation.workers
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from logic.persona import PersonaService
from logic.rank import RankService
from logic.schema import SchemaContextValidator, SchemaValidator
from logic.team import TeamService
from logic.coord import CoordService
from logic.square import SquareService
from logic.system import GameColorValidator, IdentityService, NumberValidator

class SchemaQueryIntegrityWorkers:
    """
    Role:
        -   Container

    Responsibilities:
        1.  Reduces the number params in SchemaQuery Builder and Validator entry points.

    Attributes:
        schema_validator: SchemaValidator
        context_validator: SchemaContextValidator

    Provides:

    Super Class:
    """
    _schema_validator: SchemaValidator
    _context_validator: SchemaContextValidator


    
    def __init__(
            self,
            schema_validator: SchemaValidator = SchemaValidator(),
            context_validator: SchemaContextValidator = SchemaContextValidator(),
    ):
        """
            Args:
            schema_validator: SchemaValidator
            context_validator: SchemaContextValidator
        """
        self._schema_validator = schema_validator
        self._context_validator = context_validator
        
    @property
    def schema_validator(self) -> SchemaValidator:
        return self._schema_validator
    
    @property
    def context_validator(self) -> SchemaContextValidator:
        return self._context_validator
    

        
