# src/domain/metadata/unions/model/encounter/stalemate/types.py

"""
Module: domain.metadata.unions.encounter.stalemate.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import  StalemateEncounter, StalemateEncounterBlueprint
from transit import StalemateEncounterCarrier


class StalemateEncounterTypeUnion(EncounterTypeUnion[StalemateEncounter]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a StalemateEncounter.

    Attributes:
        model: Type[StalemateEncounter]
        carrier: Type[StalemateEncounterCarrier]
        blueprint: Type[StalemateEncounterBlueprint]

    Provides:

    Super Class:
        EncounterTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[StalemateEncounter]] | None = None,
            carrier: Optional[Type[StalemateEncounterCarrier]] | None = None,
            blueprint: Optional[Type[StalemateEncounterBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[StalemateEncounter]]
            carrier: Optional[Type[StalemateEncounterCarrier]]
            blueprint: Optional[Type[StalemateEncounterBlueprint]]
        """
        super().__init__(
            model=model or StalemateEncounter,
            carrier=carrier or StalemateEncounterCarrier,
            blueprint=blueprint or StalemateEncounterBlueprint
        )
    
    @property
    def model(self) -> Type[StalemateEncounter]:
        return cast(Type[StalemateEncounter], super().model)
    
    @property
    def carrier(self) -> Type[StalemateEncounterCarrier]:
        return cast(Type[StalemateEncounterCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[StalemateEncounterBlueprint]:
        return cast(Type[StalemateEncounterBlueprint], super().blueprint)