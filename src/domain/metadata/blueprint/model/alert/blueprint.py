# src/domain/metadata/blueprint/model/alert/blueprint.py

"""
Module: domain.metadata.blueprint.model.alert.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Alert, CheckmateEncounter, EncounterWarning, ModelBlueprint
from err import AlertNullException


class AlertBlueprint(ModelBlueprint[Alert]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating an Alert object.

    Attributes:
        threat: Optional[EncounterWarning]
        checkmate: Optional[CheckmateEncounter]
        domain_class: Type[Alert]
        domain_null_exception: AlertNullException
        
    Provides:

     Super Class:
        ModelBlueprint
     """
    _threat: Optional[EncounterWarning]
    _checkmate: Optional[CheckmateEncounter]
    
    def __init__(
            self,
            threat: Optional[EncounterWarning] | None = None,
            checkmate: Optional[CheckmateEncounter] | None = None,
            domain_class: Optional[Type[Alert]] | None = None,
            domain_null_exception: Optional[AlertNullException]| None = None,
    ):
        """
        Args:
            threat: Optional[EncounterWarning]
            checkmate: Optional[CheckmateEncounter]
            domain_class: Optional[Type[Alert]]
            domain_null_exception: Optional[AlertNullException]
        """
        super().__init__(
            domain_class=domain_class or Type[Alert],
            domain_null_exception=domain_null_exception or AlertNullException(),
        )
        self._threat = threat
        self._checkmate = checkmate
    
    @property
    def threat(self) -> Optional[EncounterWarning]:
        return self._threat
    
    @property
    def checkmate(self) -> Optional[CheckmateEncounter]:
        return self._checkmate

    @property
    def domain_class(self) -> Type[Alert]:
        return cast(Type[Alert], super().domain_class)
    
    @property
    def domain_null_exception(self) -> AlertNullException:
        return cast(AlertNullException, super().domain_null_exception)
