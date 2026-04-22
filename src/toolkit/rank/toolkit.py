# src/toolkit/rank/toolkit.py

"""
Module: toolkit.rank.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Rank
from toolkit import Toolkit
from integrity import PersonaValidator
from microservice import IdentityService
from operation import ValidationBootstrapper


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
        persona_validator: PersonaValidator
        validation_bootstrapper: ValidationBootstrapper
        
    Provides:
    
    Super Class:
        Toolkit
    """
    _identity_service: IdentityService
    _persona_validator: PersonaValidator
    _validation_bootstrapper: ValidationBootstrapper

    def __init__(
            self,
            persona_validator: PersonaValidator | None = None,
            identity_service: IdentityService | None = None,
            validation_bootstrapper: ValidationBootstrapper | None = None,
    ):
        """
        Args:
            identity_service: IdentityService
            persona_validator: PersonaValidator
            validation_bootstrapper: ValidationBootstrapper
        """
        super().__init__()
        self._persona_validator = persona_validator or PersonaValidator()
        self._identity_service = identity_service or IdentityService()
        self._validation_bootstrapper = validation_bootstrapper or ValidationBootstrapper()
        
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
    
    @property
    def persona_validator(self) -> PersonaValidator:
        return self._persona_validator
    
    @property
    def validation_bootstrapper(self) -> ValidationBootstrapper:
        return self._validation_bootstrapper
        