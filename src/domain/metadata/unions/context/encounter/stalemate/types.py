# src/domain/metadata/unions/context/encounter/stalemate/types.py

"""
Module: domain.metadata.unions.context.encounter.stalemate.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import  StalemateEncounter, StalemateEncounterContextBlueprint
from transit import StalemateEncounterContextCarrier


class StalemateEncounterContextTypeUnion(EncounterContextTypeUnion[StalemateEncounterContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a StalemateEncounter.

    Attributes:
        model: Type[StalemateEncounterContext]
        carrier: Type[StalemateEncounterContextCarrier]
        blueprint: Type[StalemateEncounterContextBlueprint]

    Provides:

    Super Class:
        EncounterContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[StalemateEncounterContext]] | None = None,
            carrier: Optional[Type[StalemateEncounterContextCarrier]] | None = None,
            blueprint: Optional[Type[StalemateEncounterContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[StalemateEncounterContext]]
            carrier: Optional[Type[StalemateEncounterContextCarrier]]
            blueprint: Optional[Type[StalemateEncounterContextBlueprint]]
        """
        super().__init__(
            model=model or StalemateEncounterContext, 
            carrier=carrier or StalemateEncounterContextCarrier,
            blueprint=blueprint or StalemateEncounterContextBlueprint
        )
    
    @property
    def model(self) -> Type[StalemateEncounterContext]:
        return cast(Type[StalemateEncounterContext], super().model)
    
    @property
    def carrier(self) -> Type[StalemateEncounterContextCarrier]:
        return cast(Type[StalemateEncounterContextCarrier], super().reference)
    
    @property
    def blueprint(self) -> Type[StalemateEncounterContextBlueprint]:
        return cast(Type[StalemateEncounterContextBlueprint], super().contextBlueprint)