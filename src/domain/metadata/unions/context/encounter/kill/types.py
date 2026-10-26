# src/domain/metadata/unions/context/encounter/kill/types.py

"""
Module: domain.metadata.unions.context.encounter.kill.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Encounter, EncounterContextTypeUnion, KillEncounter, KillEncounterContextBlueprint
from transit import KillEncounterContextCarrier


class KillEncounterContextTypeUnion(EncounterContextTypeUnion[EncounterContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1.  Catalog of types associated with building and validating a
            KillEncounter.

    Attributes:
        model: Type[KillEncounterContext]
        carrier: Type[KillEncounterContextCarrier]
        blueprint: Type[KillEncounterContextBlueprint]

    Provides:

    Super Class:
        EncounterContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[KillEncounterContext]] | None = None,
            carrier: Optional[Type[KillEncounterContextCarrier]] | None = None,
            blueprint: Optional[Type[KillEncounterContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[KillEncounterContext]]
            carrier: Optional[Type[KillEncounterContextCarrier]]
            blueprint: Optional[Type[KillEncounterContextBlueprint]]
        """
        super().__init__(
            model=model or KillEncounterContext, 
            carrier=carrier or KillEncounterContextCarrier,
            blueprint=blueprint or KillEncounterContextBlueprint
        )
    
    @property
    def model(self) -> Type[KillEncounterContext]:
        return cast(Type[KillEncounterContext], super().model)
    
    @property
    def carrier(self) -> Type[KillEncounterContextCarrier]:
        return cast(Type[KillEncounterContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[KillEncounterContextBlueprint]:
        return cast(Type[KillEncounterContextBlueprint], super().contextBlueprint)