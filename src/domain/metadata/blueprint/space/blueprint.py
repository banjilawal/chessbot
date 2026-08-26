# src/domain/metadata/blueprint/space/blueprint.py

"""
Module: domain.metadata.blueprint.space.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, List, Type, TypeVar, cast

from domain.metadata.blueprint import Blueprint
from err import SpaceNullException
from domain.model import Vector


T = TypeVar("T", bound="Space")

class SpaceBlueprint(Blueprint, ABC, Generic[T]):
    """
     Role:
         -  DTO

     Responsibilities:
         1.  Provides values for instantiating a Space object
         2.  DTO

     Attributes:
         model_class: Type[T]
         null_exception: Optional[SpaceNullException]
         
     Provides:

     Super Class:
        Blueprint
     """
    _origin: Vector
    _terminus: Vector
    
    def __init__(
            self,
            origin: Vector,
            terminus: Vector,
            model_class: Type[T],
            null_exception: SpaceNullException,
    ):
        """
        Args:
            origin: Vector
            model_class: Type[Space[T]]
            terminus: Optional[Vector]
            null_exception: SpaceNullException
        """
        super().__init__(model_class=model_class, null_exception=null_exception)
        self._origin = origin
        self._terminus = terminus
        
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def terminus(self) -> Vector:
        return self._terminus

    @property
    def space_class(self) -> Type[T]:
        return cast(Type[T], super().model_class)
    
    @property
    def null_exception(self) -> SpaceNullException:
        return cast(SpaceNullException, super().null_exception)
    
    @property
    def endpoints_to_list(self) -> List[Vector]:
        return [self._origin, self._terminus]
    
    @property
    def terminus_exists(self) -> bool:
        return self._terminus is not None
    
    @property
    def terminus_does_not_exist(self) -> bool:
        return not self.terminus_exists