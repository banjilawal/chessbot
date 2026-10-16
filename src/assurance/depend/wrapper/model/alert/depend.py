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
from domain import Alert
from exchange import EncounterValidationServer, PlayerValidationServer


class AlertWrapperDependency(ModelWrapperDependency[Alert]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy AlertValidator's ResponseWrapper dependencies.

    Attributes:
        encounter: EncounterValidationServer

    Provides:

    Super Class:
        ModelWrapperDependency
    """
    
    _encounter: EncounterValidationServer
    
    def __init__(
            self,
            encounter: Optional[EncounterValidationServer] | None = None,
    ):
        """
        Args:
            encounter: Optional[EncounterValidatorClient]
        """
        super().__init__()
        self._encounter = encounter or EncounterValidationServer()
        
    @property
    def encounter(self) -> EncounterValidationServer:
        return self._encounter