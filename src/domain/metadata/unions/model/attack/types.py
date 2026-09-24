# src/domain/metadata/unions/model/attack/types.py

"""
Module: domain.metadata.unions.attack.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar, cast

from domain import Attack, AttackBlueprint, ModelTypeUnion
from transit import AttackCarrier

T = TypeVar("T", bound="Attack")

class AttackTypeUnion(ModelTypeUnion[T], Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Attack.

    Attributes:
        model: Type[T]
        carrier: Type[AttackCarrier[T]
        blueprint: Type[AttackBlueprint[T]
        
    Provides:

    Super Class:
        ModelTypeUnion
    """
    
    def __init__(
            self,
            model: Optional[Type[T]] | None = None,
            carrier: Optional[Type[AttackCarrier[T]]] | None = None,
            blueprint: Optional[Type[AttackBlueprint[T]]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[T]]
            carrier: Optional[Type[AttackCarrier[T]]
            blueprint: Optional[Type[AttackBlueprint[T]]
        """
        super().__init__(
            model=model or Attack,
            carrier=carrier or AttackCarrier,
            blueprint=blueprint or AttackBlueprint,
        )
    
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier(self) -> Type[AttackCarrier[T]]:
        return cast(Type[AttackCarrier[T]], super().carrier)
    
    @property
    def blueprint(self) -> Type[AttackBlueprint[T]]:
        return cast(Type[AttackBlueprint[T]], super().blueprint)