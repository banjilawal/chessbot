# src/domain/metadata/unions/strcture/register/manifest.py

"""
Module: domain.metadata.unions.structure.register.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Register, RegisterBlueprint, StructureTypeUnion
from transit import EntityCarrier

T = TypeVar("T", bound="Register")


class RegisterTypeUnion(StructureTypeUnion[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Register.

    Attributes:
        model: Type[T]
        carrier: Type[EntityCarrier[T]]
        blueprint: Type[RegisterBlueprint[T]]
        
    Provides:

    Super Class:
        StructureTypeUnion
    """
    
    def __init__(
            self,
            model: Type[T],
            carrier: Type[EntityCarrier[T]],
            blueprint: Type[RegisterBlueprint[T]],
    ):
        """
        Args:
            model: Type[T]
            carrier: Type[EntityCarrier[T]]
            blueprint: Type[RegisterBlueprint[T]]
        """
        super().__init__(model=model, blueprint=blueprint, carrier=carrier)
        
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier(self) -> Type[EntityCarrier[T]]:
        return self._carrier
    
    @property
    def blueprint(self) -> Type[RegisterBlueprint[T]]:
        return cast(Type[RegisterBlueprint[T]], super().model)