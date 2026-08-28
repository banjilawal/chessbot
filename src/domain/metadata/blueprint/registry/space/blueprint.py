# src/domain/metadata/blueprint/space/reservoir/space.py

"""
Module: domain.metadata.blueprint.space.reservoir.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar, cast

from domain.metadata.blueprint import Blueprint
from err import SpaceReservoirNullException
from domain.model import Vector

from space import SpaceReservoir

T = TypeVar("T", bound="SpaceReservoir")


class SpaceReservoirBlueprint(Blueprint, ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a SpaceReservoir.

     Attributes:
         space_class: Type[Space]
         domain_null_exception: Optional[SpaceReservoirNullException]

     Provides:

     Super Class:
        Blueprint
     """
    _origin: Vector
    _terminus: Optional[Vector]
    
    def __init__(
            self,
            origin: Vector,
            terminus: Optional[Vector] | None = None,
            domain_null_exception: Optional[SpaceReservoirNullException] | None = None,
            domain_class: Type[SpaceReservoir] = SpaceReservoir,
    ):
        """
        Args:
            origin: Vector
            domain_class: Type[Space[T]]
            terminus: Optional[Vector]
            domain_null_exception: SpaceReservoirNullException
        """
        super().__init__(domain_class=domain_class, domain_null_exception=domain_null_exception)
        self._origin = origin
        self._terminus = terminus
    
    @property
    def space_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> SpaceReservoirNullException:
        return cast(SpaceReservoirNullException, super().domain_null_exception)
    
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def terminus(self) -> Optional[Vector]:
        return self._terminus