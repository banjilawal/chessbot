# src/tool/rank/tool.py

"""
Module: tool.rank.tool
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import PersonaService
from model import Rank
from system import IdentityService
from tool import toolkit


class Ranktoolkit(toolkit[Rank]):
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


    

        
