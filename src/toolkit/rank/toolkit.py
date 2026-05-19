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
from operation import PersonaValidator



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
        validation_primer: ValidationPrimer
        
    Provides:
    
    Super Class:
        Toolkit
    """
    _persona_validator: PersonaValidator

    def __init__(
            self,
            persona_validator: PersonaValidator | None = None,
    ):
        """
        Args:
            persona_validator: PersonaValidator
        """
        super().__init__()
        self._persona_validator = persona_validator or PersonaValidator()
    
    @property
    def persona_validator(self) -> PersonaValidator:
        return self._persona_validator
        