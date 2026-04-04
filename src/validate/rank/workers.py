# src/logic/schema/database/search/context/service/operation/workers.py

"""
Module: logic.schema.database.search.context.service.operation.workers
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from catalog.persona import PersonaService
from logic.system import IdentityService


class RankIntegrityWorkers:
    """
    Role:
        -   Container

    Responsibilities:
        1.  Reduces the number params in SchemaContext Builder and Validator entry points.

    Attributes:
        persona_service: PersonaService
        identity_service: IdentityService


    Provides:

    Super Class:
    """
    _persona_service: PersonaService
    _identity_service: IdentityService



    
    def __init__(
            self,
            persona_service: PersonaService = PersonaService(),
            identity_service: IdentityService = IdentityService(),
    ):
        """
        Args:
            persona_service: PersonaService
            identity_service: IdentityService
        """
        self._persona_service = persona_service
        self._identity_service = identity_service

    @property
    def persona_service(self) -> PersonaService:
        return self._persona_service
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service


    

        
