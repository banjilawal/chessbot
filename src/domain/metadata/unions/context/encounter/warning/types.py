# src/domain/metadata/unions/context/encounter/warning/types.py

"""
Module: domain.metadata.unions.context.encounter.warning.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import (
    EncounterContextTypeUnion, EncounterWarning, EncounterWarningContextBlueprint
)
from transit import EncounterWarningContextCarrier


class EncounterWarningContextTypeUnion(EncounterContextTypeUnion[EncounterWarningContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1.  Catalog of types associated with building and validating 
            an EncounterWarning.

    Attributes:
        model: Type[EncounterWarningContext]
        carrier: Type[EncounterWarningContextCarrier]
        blueprint: Type[EncounterWarningContextBlueprint]

    Provides:

    Super Class:
        EncounterContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[EncounterWarningContext]] | None = None,
            carrier: Optional[Type[EncounterWarningContextCarrier]] | None = None,
            blueprint: Optional[Type[EncounterWarningContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[EncounterWarningContext]]
            carrier: Optional[Type[EncounterWarningContextCarrier]]
            blueprint: Optional[Type[EncounterWarningContextBlueprint]]
        """
        super().__init__(
            model=model or EncounterWarningContext, 
            carrier=carrier or EncounterWarningContextCarrier,
            blueprint=blueprint or EncounterWarningContextBlueprint
        )
    
    @property
    def model(self) -> Type[EncounterWarningContext]:
        return cast(Type[EncounterWarningContext], super().model)
    
    @property
    def carrier(self) -> Type[EncounterWarningContextCarrier]:
        return cast(Type[EncounterWarningContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[EncounterWarningContextBlueprint]:
        return cast(Type[EncounterWarningContextBlueprint], super().contextBlueprint)