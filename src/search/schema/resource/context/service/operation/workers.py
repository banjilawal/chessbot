# src/logic/schema/database/search/context/service/operation/workers.py

"""
Module: logic.schema.database.search.context.service.operation.workers
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from system import GameColorValidator, IdentityService

class SchemaContextIntegrityWorkers:
    """
    Role:
        -   Container

    Responsibilities:
        1.  Reduces the number params in SchemaContext Builder and Validator entry points.

    Attributes:
        identity_service: IdentityService
        color_validator: GameColorValidator

    Provides:

    Super Class:
    """
    _identity_service: IdentityService
    _color_validator: GameColorValidator
    
    def __init__(
            self,
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ):
        """
        Args:
            identity_service: IdentityService
            color_validator: GameColorValidator
          
        """
        self._color_validator = color_validator
        self._identity_service = identity_service

    @property
    def color_validator(self) -> GameColorValidator:
        return self._color_validator
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service


    

        
