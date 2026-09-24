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

from domain import Attack, AttackBlueprint, TypeUnion


T = TypeVar("T", bound="Attack")

class AttackTypeUnion(TypeUnion[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating an Attack.

    Attributes:
        model: Type[Attack]
        carrier: Type[AttackCarrier]
        blueprint: Type[AttackBlueprint]
        
    Provides:

    Super Class:
        TypeUnion
    """
    
    def __init__(
            self,
            model: Optional[Type[Attack]] | None = None,
            carrier: Optional[Type[AttackCarrier]] | None = None,
            blueprint: Optional[Type[AttackBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[Attack]]
            carrier: Optional[Type[AttackCarrier]]
            blueprint: Optional[Type[AttackBlueprint]]
        """
        super().__init__(
            model=model or Attack,
            carrier=carrier or AttackCarrier,
            blueprint=blueprint or AttackBlueprint,
        )
    
    @property
    def model(self) -> Type[Attack]:
        return cast(Type[Attack], super().model)
    
    @property
    def carrier(self) -> Type[AttackCarrier]:
        return cast(Type[AttackCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[AttackBlueprint]:
        return cast(Type[AttackBlueprint], super().blueprint)