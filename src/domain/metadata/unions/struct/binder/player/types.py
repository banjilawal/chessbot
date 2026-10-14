# src/domain/metadata/unions/strcture/binder/player/manifest.py

"""
Module: domain.metadata.unions.struct.binder.player.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import BinderTypeUnion, PlayerBinder, PlayerBinderBlueprint
from transit import PlayerBinderCarrier, StructCarrier

class PlayerBinderTypeUnion(BinderTypeUnion[PlayerBinder]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a PlayerBinder.

    Attributes:
        model: Type[PlayerBinder]
        carrier: Type[StructCarrier[PlayerBinder]]
        blueprint: Type[PlayerBinderBlueprint]
        
    Provides:

    Super Class:
        PlayerBinderTypeUnion
    """
    
    def __init__(
            self,
            model: Optional[Type[PlayerBinder]] | None = None,
            carrier: Optional[Type[PlayerBinderCarrier]] | None = None,
            blueprint: Optional[Type[PlayerBinderBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[PlayerBinder]]
            carrier: Optional[Type[PlayerBinderCarrier]]
            blueprint: Optional[Type[PlayerBinderBlueprint]]
        """
        super().__init__(
            model=model or PlayerBinder,
            blueprint=blueprint or Type[PlayerBinderBlueprint],
            carrier=carrier or Type[PlayerBinderCarrier],
        )
        
    @property
    def model(self) -> Type[PlayerBinder]:
        return cast(Type[PlayerBinder], super().model)
    
    @property
    def carrier(self) -> Type[PlayerBinder]:
        return cast(Type[PlayerBinder], super().carrier)
    
    @property
    def blueprint(self) -> Type[PlayerBinderBlueprint]:
        return cast(Type[PlayerBinderBlueprint], super().model)