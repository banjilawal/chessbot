# src/blueprint/space/quadrant/blueprint.py

"""
Module: blueprint.space.quadrant.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Generic, List, Optional, Type, TypeVar, cast

from blueprint import SpaceBlueprint
from err import QuadrantNullException
from model import Vector
from space import QuadrantSpace

T = TypeVar("T", bound="QuadrantSpace")


class QuadrantBlueprint(SpaceBlueprint, Generic[T]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a QuadrantSpace object.
         2.  DTO

     Attributes:
        origin: Vector
        model_class: Type[QuadrantSpace]
        null_exception: Optional[QuadrantNullException]
         
     Provides:

     Super Class:
        SpaceBlueprint
     """
    _origin: Vector
    _terminus: Optional[Vector]
    
    def __init__(
            self,
            origin: Vector,
            model_class: Type[QuadrantSpace],
            terminus: Optional[Vector] | None = None,
            null_exception: Optional[QuadrantNullException] | None = QuadrantNullException(),
    ):
        """
        Args:
            origin: Vector
            terminus: Optional[Vector]
            model_class: Type[QuadrantSpace]
            null_exception: Optional[QuadrantNullException]
        """
        super().__init__(model_class=model_class, null_exception=null_exception)
        self._origin = origin

    @property
    def model_class(self) -> Type[QuadrantSpace]:
        return cast(Type[QuadrantSpace], super().model_class)
    
    @property
    def null_exception(self) -> QuadrantNullException:
        return cast(QuadrantNullException, super().null_exception)
    
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @@property
    def terminus(self) -> Optional[Vector]:
        return self._terminus
    
    @property
    def endpoints_to_list(self) -> List[Vector]:
        return [self._origin, self._terminus]
    
    @property
    def terminus_exists(self) -> bool:
        return self._terminus is not None
    
    @property
    def terminus_does_not_exist(self) -> bool:
        return not self.terminus_exists
