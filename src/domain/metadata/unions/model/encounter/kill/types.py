# src/domain/metadata/unions/model/encounter/kill/types.py

"""
Module: domain.metadata.unions.encounter.kill.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Encounter, EncounterTypeUnion, KillEncounter, KillEncounterBlueprint
from transit import KillEncounterCarrier


class KillEncounterTypeUnion(EncounterTypeUnion[Encounter]):
    """
    Role:
        - Metadata

    Responsibilities:
        1.  Catalog of types associated with building and validating a
            KillEncounter.

    Attributes:
        model: Type[KillEncounter]
        carrier: Type[KillEncounterCarrier]
        blueprint: Type[KillEncounterBlueprint]

    Provides:

    Super Class:
        EncounterTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[KillEncounter]] | None = None,
            carrier: Optional[Type[KillEncounterCarrier]] | None = None,
            blueprint: Optional[Type[KillEncounterBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[KillEncounter]]
            carrier: Optional[Type[KillEncounterCarrier]]
            blueprint: Optional[Type[KillEncounterBlueprint]]
        """
        super().__init__(
            model=model or KillEncounter,
            carrier=carrier or KillEncounterCarrier,
            blueprint=blueprint or KillEncounterBlueprint
        )
    
    @property
    def model(self) -> Type[KillEncounter]:
        return cast(Type[KillEncounter], super().model)
    
    @property
    def carrier(self) -> Type[KillEncounterCarrier]:
        return cast(Type[KillEncounterCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[KillEncounterBlueprint]:
        return cast(Type[KillEncounterBlueprint], super().blueprint)