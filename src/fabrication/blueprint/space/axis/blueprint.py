# src/blueprint/space/axis/blueprint.py

"""
Module: blueprint.space.axis.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations
from typing import Generic, List, Optional, Type, TypeVar, cast

from fabrication.blueprint import SpaceBlueprint
from err import AxisNullException
from domain.model import Vector

T = TypeVar("T", bound="Axis")


class AxisBlueprint(SpaceBlueprint, Generic[T]):
    """
     Role:
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating an Axis.

     Attributes:
        origin: Vector
        model_class: Type[Axis]
        null_exception: Optional[AxisNullException]
         
     Provides:

     Super Class:
        SpaceBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            model_class: Type[T],
            terminus: Optional[Vector] | None = None,
            null_exception: Optional[AxisNullException] | None = AxisNullException(),
    ):
        """
        Args:
            origin: Vector
            terminus: Optional[Vector]
            model_class: Type[Axis]
            null_exception: Optional[AxisNullException]
        """
        super().__init__(
            origin=origin,
            terminus=terminus,
            model_class=model_class,
            null_exception=null_exception
        )

    @property
    def model_class(self) -> Type[T]:
        return cast(Type[T], super().model_class)
    
    @property
    def null_exception(self) -> AxisNullException:
        return cast(AxisNullException, super().null_exception)
    
    @property
    def endpoints_to_list(self) -> List[Vector]:
        return [self._origin, self._terminus]
    
    @property
    def terminus_exists(self) -> bool:
        return self._terminus is not None
    
    @property
    def terminus_does_not_exist(self) -> bool:
        return not self.terminus_exists
    

