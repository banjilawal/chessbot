# src/domain/metadata/unions/model/encounter/checkmate/types.py

"""
Module: domain.metadata.unions.encounter.checkmate.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import  CheckmateEncounter, CheckmateEncounterBlueprint
from transit import CheckmateEncounterCarrier


class CheckmateEncounterTypeUnion(EncounterTypeUnion[CheckmateEncounter]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a CheckmateEncounter.

    Attributes:
        model: Type[CheckmateEncounter]
        carrier: Type[CheckmateEncounterCarrier]
        blueprint: Type[CheckmateEncounterBlueprint]

    Provides:

    Super Class:
        EncounterTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[CheckmateEncounter]] | None = None,
            carrier: Optional[Type[CheckmateEncounterCarrier]] | None = None,
            blueprint: Optional[Type[CheckmateEncounterBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[CheckmateEncounter]]
            carrier: Optional[Type[CheckmateEncounterCarrier]]
            blueprint: Optional[Type[CheckmateEncounterBlueprint]]
        """
        super().__init__(
            model=model or CheckmateEncounter,
            carrier=carrier or CheckmateEncounterCarrier,
            blueprint=blueprint or CheckmateEncounterBlueprint
        )
    
    @property
    def model(self) -> Type[CheckmateEncounter]:
        return cast(Type[CheckmateEncounter], super().model)
    
    @property
    def carrier(self) -> Type[CheckmateEncounterCarrier]:
        return cast(Type[CheckmateEncounterCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[CheckmateEncounterBlueprint]:
        return cast(Type[CheckmateEncounterBlueprint], super().blueprint)