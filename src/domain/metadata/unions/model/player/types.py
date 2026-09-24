# src/domain/metadata/unions/model/player/types.py

"""
Module: domain.metadata.unions.player.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Type, TypeVar, cast

from domain import ModelTypeUnion, Player, PlayerBlueprint
from transit import PlayerCarrier

T = TypeVar("T", bound="Player")


class PlayerTypeUnion(ModelTypeUnion[T], Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Player.

    Attributes:
        model: Type[T]
        carrier: Type[PlayerCarrier[T]]
        blueprint: Type[Blueprint[T]]

    Provides:

    Super Class:
        ModelTypeUnion
    """
    
    def __init__(
            self,
            model: Type[T],
            carrier: Type[PlayerCarrier[T]],
            blueprint: Type[PlayerBlueprint[T]],
    ):
        """
        Args:
            model: Type[T]
            carrier: Type[PlayerCarrier[T]]
            blueprint: Type[PlayerBlueprint[T]]
        """
        super().__init__(model=model, carrier=carrier, blueprint=blueprint)
    
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier(self) -> Type[PlayerCarrier[T]]:
        return cast(Type[PlayerCarrier[T]], super().carrier)
    
    @property
    def blueprint(self) -> Type[PlayerBlueprint[T]]:
        return cast(Type[PlayerBlueprint[T]], super().blueprint)