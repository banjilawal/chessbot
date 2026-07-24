# src/blueprint/space/axis/blueprint.py

"""
Module: blueprint.space.axis.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Generic, List, Optional, Type, TypeVar, cast

from blueprint import SpaceBlueprint
from err import AxisNullException
from model import Vector
from space import AxisSpace

T = TypeVar("T", bound="AxisSpace")


class AxisBlueprint(SpaceBlueprint, Generic[T]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a AxisSpace object.
         2.  DTO

     Attributes:
        origin: Vector
        model_class: Type[AxisSpace]
        null_exception: Optional[AxisNullException]
         
     Provides:

     Super Class:
        SpaceBlueprint
     """
    _origin: Vector
    _terminus: Optional[Vector]
    
    def __init__(
            self,
            origin: Vector,
            model_class: Type[AxisSpace],
            terminus: Optional[Vector] | None = None,
            null_exception: Optional[AxisNullException] | None = AxisNullException(),
    ):
        """
        Args:
            origin: Vector
            model_class: Type[AxisSpace]
            null_exception: Optional[AxisNullException]
        """
        super().__init__(model_class=model_class, null_exception=null_exception)
        self._origin = origin
        self._terminus = terminus
        
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def terminus(self) -> Optional[Vector]:
        return self._terminus

    @property
    def model_class(self) -> Type[AxisSpace]:
        return cast(Type[AxisSpace], super().model_class)
    
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
    

