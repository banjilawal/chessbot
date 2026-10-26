# src/assurance/depend/service/model/alert/depend.py

"""
Module: assurance.depend.service.model.alert.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelDependency
from domain import Alert
from exchange import EncounterValidationService, PlayerValidationService


class AlertDependency(ModelDependency[Alert]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy AlertValidator's ResponseService dependencies.

    Attributes:
        encounter: EncounterValidationService

    Provides:

    Super Class:
        ModelDependency
    """
    
    _encounter: EncounterValidationService
    
    def __init__(
            self,
            encounter: Optional[EncounterValidationService] | None = None,
    ):
        """
        Args:
            encounter: Optional[EncounterValidatorClient]
        """
        super().__init__()
        self._encounter = encounter or EncounterValidationService()
        
    @property
    def encounter(self) -> EncounterValidationService:
        return self._encounter