# src/integrity/toolkit/rank/toolkit.py

"""
Module: integrity.toolkit.rank.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from microservice import IdentityService, PersonaService
from model import Rank
from toolkit import Toolkit


class RankToolkit(Toolkit[Rank]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for Arena tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.
    
    Attributes:
        identity_service: IdentityService
        persona_service: PersonaService
        
    Provides:
    
    Super Class:
        Toolkit
    """
    _identity_service: IdentityService
    _persona_service: PersonaService

    def __init__(
            self,
            identity_service: IdentityService | None = None,
            persona_service: PersonaService | None = None,
    ):
        """
        Args:
            identity_service: IdentityService
            persona_service: PersonaService
        """
        self._identity_service = identity_service or IdentityService()
        self._persona_service = persona_service or PersonaService()
        
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
    
    @property
    def persona_service(self) -> PersonaService:
        return self._persona_service
        