# src/domain/metadata/unions/context/team/types.py

"""
Module: domain.metadata.unions.context.team.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import ContextLayer, Team, TeamContextBlueprint
from transit import TeamContextCarrier


class TeamContextLayer(ContextLayer[TeamContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Team.

    Attributes:
        model: Type[TeamContext]
        carrier: Type[TeamContextCarrier]
        blueprint: Type[TeamContextBlueprint]

    Provides:

    Super Class:
        ContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[TeamContext]] | None = None,
            carrier: Optional[Type[TeamContextCarrier]] | None = None,
            blueprint: Optional[Type[TeamContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[TeamContext]]
            carrier: Optional[Type[TeamContextCarrier]
            blueprint: Optional[Type[TeamContextBlueprint] 
        """
        super().__init__(
            model=model or TeamContext, 
            carrier=carrier or TeamContextCarrier, 
            blueprint=blueprint or TeamContextBlueprint
        )
    
    @property
    def model(self) -> Type[TeamContext]:
        return cast(Type[TeamContext], super().model)
    
    @property
    def carrier(self) -> Type[TeamContextCarrier]:
        return cast(Type[TeamContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[TeamContextBlueprint]:
        return cast(Type[TeamContextBlueprint], super().contextBlueprint)