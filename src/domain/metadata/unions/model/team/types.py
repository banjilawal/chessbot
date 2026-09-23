# src/domain/metadata/unions/team/types.py

"""
Module: domain.metadata.unions.team.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Team, TeamBlueprint, TypeUnion
from transit import TeamCarrier


class TeamTypeUnion(TypeUnion[Team]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Team.

    Attributes:
        model: Type[Team]
        carrier: Type[TeamCarrier]
        blueprint: Type[TeamBlueprint]

    Provides:

    Super Class:
        TypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[Team]] | None = None,
            carrier: Optional[Type[TeamCarrier]] | None = None, 
            blueprint: Optional[Type[TeamBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Team]]
            carrier: Optional[Type[TeamCarrier]
            blueprint: Optional[Type[TeamBlueprint] 
        """
        super().__init__(
            model=model or Team, 
            carrier=carrier or TeamCarrier, 
            blueprint=blueprint or TeamBlueprint
        )
    
    @property
    def model(self) -> Type[Team]:
        return cast(Type[Team], super().model)
    
    @property
    def carrier(self) -> Type[TeamCarrier]:
        return cast(Type[TeamCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[TeamBlueprint]:
        return cast(Type[TeamBlueprint], super().blueprint)