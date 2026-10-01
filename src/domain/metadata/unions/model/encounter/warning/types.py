# src/domain/metadata/unions/model/encounter/warning/types.py

"""
Module: domain.metadata.unions.encounter.warning.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import (
    EncounterTypeUnion, EncounterWarning, EncounterWarningBlueprint
)
from transit import EncounterWarningCarrier


class EncounterWarningTypeUnion(EncounterTypeUnion[EncounterWarning]):
    """
    Role:
        - Metadata

    Responsibilities:
        1.  Catalog of types associated with building and validating 
            an EncounterWarning.

    Attributes:
        model: Type[EncounterWarning]
        carrier: Type[EncounterWarningCarrier]
        blueprint: Type[EncounterWarningBlueprint]

    Provides:

    Super Class:
        EncounterTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[EncounterWarning]] | None = None,
            carrier: Optional[Type[EncounterWarningCarrier]] | None = None,
            blueprint: Optional[Type[EncounterWarningBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[EncounterWarning]]
            carrier: Optional[Type[EncounterWarningCarrier]]
            blueprint: Optional[Type[EncounterWarningBlueprint]]
        """
        super().__init__(
            model=model or EncounterWarning,
            carrier=carrier or EncounterWarningCarrier,
            blueprint=blueprint or EncounterWarningBlueprint
        )
    
    @property
    def model(self) -> Type[EncounterWarning]:
        return cast(Type[EncounterWarning], super().model)
    
    @property
    def carrier(self) -> Type[EncounterWarningCarrier]:
        return cast(Type[EncounterWarningCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[EncounterWarningBlueprint]:
        return cast(Type[EncounterWarningBlueprint], super().blueprint)