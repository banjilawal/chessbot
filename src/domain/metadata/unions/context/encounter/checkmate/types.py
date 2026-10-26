# src/domain/metadata/unions/context/encounter/checkmate/types.py

"""
Module: domain.metadata.unions.context.encounter.checkmate.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import  CheckmateEncounter, CheckmateEncounterContextBlueprint
from transit import CheckmateEncounterContextCarrier


class CheckmateEncounterContextTypeUnion(EncounterContextTypeUnion[CheckmateEncounterContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a CheckmateEncounter.

    Attributes:
        model: Type[CheckmateEncounterContext]
        carrier: Type[CheckmateEncounterContextCarrier]
        blueprint: Type[CheckmateEncounterContextBlueprint]

    Provides:

    Super Class:
        EncounterContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[CheckmateEncounterContext]] | None = None,
            carrier: Optional[Type[CheckmateEncounterContextCarrier]] | None = None,
            blueprint: Optional[Type[CheckmateEncounterContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[CheckmateEncounterContext]]
            carrier: Optional[Type[CheckmateEncounterContextCarrier]]
            blueprint: Optional[Type[CheckmateEncounterContextBlueprint]]
        """
        super().__init__(
            model=model or CheckmateEncounterContext, 
            carrier=carrier or CheckmateEncounterContextCarrier,
            blueprint=blueprint or CheckmateEncounterContextBlueprint
        )
    
    @property
    def model(self) -> Type[CheckmateEncounterContext]:
        return cast(Type[CheckmateEncounterContext], super().model)
    
    @property
    def carrier(self) -> Type[CheckmateEncounterContextCarrier]:
        return cast(Type[CheckmateEncounterContextCarrier], super().reference)
    
    @property
    def blueprint(self) -> Type[CheckmateEncounterContextBlueprint]:
        return cast(Type[CheckmateEncounterContextBlueprint], super().contextBlueprint)