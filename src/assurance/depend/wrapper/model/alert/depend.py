# src/assurance/depend/wrapper/model/alert/depend.py

"""
Module: assurance.depend.wrapper.model.alert.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelWrapperDependency
from domain import AlertTable
from exchange import EncounterValidationResponseWrapper, PlayerValidationResponseWrapper


class AlertTableWrapperDependency(ModelWrapperDependency[AlertTable]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy AlertTableValidator's ResponseWrapper dependencies.

    Attributes:
        encounter: EncounterValidationResponseWrapper

    Provides:

    Super Class:
        ModelWrapperDependency
    """
    
    _encounter: EncounterValidationResponseWrapper
    
    def __init__(
            self,
            encounter: Optional[EncounterValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            encounter: Optional[EncounterValidatorClient]
        """
        super().__init__()
        self._encounter = encounter or EncounterValidationResponseWrapper()
        
    @property
    def encounter(self) -> EncounterValidationResponseWrapper:
        return self._encounter