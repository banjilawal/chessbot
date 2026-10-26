# src/domain/metadata/unions/context/encounter/types.py

"""
Module: domain.metadata.unions.context.encounter.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Generic, Optional, Type, TypeVar, cast

from domain import ContextTypeUnion, Encounter, EncounterContextBlueprint
from transit import EncounterContextCarrier

T = TypeVar("T", bound="Encounter")


class EncounterContextTypeUnion(ContextTypeUnion[TContext], Generic[TContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Encounter.

    Attributes:
        model: Type[EncounterContext]
        carrier: Type[EncounterContextCarrier]
        blueprint: Type[EncounterContextBlueprint]

    Provides:

    Super Class:
        ContextTypeUnion
    """
    
    def __init__(
            self,
            model: Optional[Type[TContext]] | None = None,
            carrier: Optional[Type[EncounterContextCarrier[TContext]]Context] | None = None,
            blueprint: Optional[Type[EncounterContextBlueprint[TContext]]Context] | None = None,
    ):
        """
        Args:
            model: Optional[Type[TContext]]
            carrier: Optional[Type[EncounterContextCarrier[TContext]]Context]
            blueprint: Optional[Type[EncounterContextBlueprint[TContext]]Context]
        """
        super().__init__(
            model=model or EncounterContext, 
            carrier=carrier or EncounterContextCarrier,
            blueprint=blueprint or EncounterContextBlueprint,
        )
    
    @property
    def model(self) -> Type[TContext]:
        return cast(Type[TContext], super().model)
    
    @property
    def carrier(self) -> Type[EncounterContextCarrier[TContext]]:
        return cast(Type[EncounterContextCarrier[TContext]], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[EncounterContextBlueprint[TContext]]:
        return cast(Type[EncounterContextBlueprint[TContext]], super().contextBlueprint)