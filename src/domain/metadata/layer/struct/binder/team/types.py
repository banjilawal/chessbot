# src/domain/metadata/unions/struct/binder/team/types.py

"""
Module: domain.metadata.unions.struct.binder.team.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import BinderLayer, TeamBinder, TeamBinderBlueprint
from transit import TeamBinderCarrier

class TeamBinderLayer(BinderLayer[TeamBinder]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a TeamBinder.

    Attributes:
        model: Type[TeamBinder]
        carrier: Type[StructCarrier[TeamBinder]]
        blueprint: Type[TeamBinderBlueprint]
        
    Provides:

    Super Class:
        TeamBinderTypeUnion
    """
    
    def __init__(
            self,
            model: Optional[Type[TeamBinder]] | None = None,
            carrier: Optional[Type[TeamBinderCarrier]] | None = None,
            blueprint: Optional[Type[TeamBinderBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[TeamBinder]]
            carrier: Optional[Type[TeamBinderCarrier]]
            blueprint: Optional[Type[TeamBinderBlueprint]]
        """
        super().__init__(
            model=model or TeamBinder,
            carrier=carrier or Type[TeamBinderCarrier],
            blueprint=blueprint or Type[TeamBinderBlueprint],
        )
        
    @property
    def model(self) -> Type[TeamBinder]:
        return cast(Type[TeamBinder], super().model)
    
    @property
    def carrier(self) -> Type[TeamBinderCarrier]:
        return cast(Type[TeamBinderCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[TeamBinderBlueprint]:
        return cast(Type[TeamBinderBlueprint], super().model)