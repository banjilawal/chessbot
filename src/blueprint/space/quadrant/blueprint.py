# src/blueprint/space/quadrant/blueprint.py

"""
Module: blueprint.space.quadrant.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Generic, Optional, Type, TypeVar, cast

from blueprint import SpaceBlueprint
from err import QuadrantNullException, SpaceNullException
from model import Vector
from space import Space, QuadrantSpace

T = TypeVar("T", bound="QuadrantSpace")


class QuadrantSpaceBlueprint(SpaceBlueprint, Generic[T]):
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
    
    def __init__(
            self,
            origin: Vector,
            model_class: Type[QuadrantSpace],
            null_exception: Optional[QuadrantNullException] | None = QuadrantNullException(),
    ):
        """
        Args:
            origin: Vector
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
        return cast(Type[QuadrantNullException], super().null_exception)
    
    @property
    def origin(self) -> Vector:
        return self._origin
