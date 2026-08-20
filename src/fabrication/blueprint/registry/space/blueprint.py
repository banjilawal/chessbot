# src/blueprint/space/reservoir/space.py

"""
Module: blueprint.space.reservoir.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar, cast

from fabrication.blueprint import Blueprint
from err import SpaceReservoirNullException
from model import Vector

from space import SpaceReservoir

T = TypeVar("T", bound="SpaceReservoir")


class SpaceReservoirBlueprint(Blueprint, ABC, Generic[T]):
    """
     Role:
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a SpaceReservoir.

     Attributes:
         space_class: Type[Space]
         null_exception: Optional[SpaceReservoirNullException]

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
            null_exception: Optional[SpaceReservoirNullException] | None = None,
            model_class: Type[SpaceReservoir] = SpaceReservoir,
    ):
        """
        Args:
            origin: Vector
            model_class: Type[Space[T]]
            terminus: Optional[Vector]
            null_exception: SpaceReservoirNullException
        """
        super().__init__(model_class=model_class, null_exception=null_exception)
        self._origin = origin
        self._terminus = terminus
    
    @property
    def space_class(self) -> Type[T]:
        return cast(Type[T], super().model_class)
    
    @property
    def null_exception(self) -> SpaceReservoirNullException:
        return cast(SpaceReservoirNullException, super().null_exception)
    
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def terminus(self) -> Optional[Vector]:
        return self._terminus