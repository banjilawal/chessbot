# src/blueprint/space/axis/blueprint.py

"""
Module: blueprint.space.axis.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Generic, Optional, Type, TypeVar, cast

from blueprint import AxisBlueprint, SpaceBlueprint
from err import westAxisNullException, AxisNullException
from model import Vector
from space import westAxis, Space, AxisSpace


class WestAxisBlueprint(AxisBlueprint[westAxis]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a AxisSpace object.
         2.  DTO

     Attributes:
        origin: Vector
        model_class: Type[westAxis]
        null_exception: Optional[westAxisNullException]

     Provides:

     Super Class:
        AxisSpaceBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            model_class: Type[westAxis],
            null_exception: Optional[westAxisNullException] |
                            None = westAxisNullException(),
    ):
        """
        Args:
            origin: Vector
            model_class: Type[westAxis]
            null_exception: Optional[westAxisNullException]
        """
        super().__init__(
            origin=origin,
            model_class=model_class,
            null_exception=null_exception
        )
        
    
    @property
    def model_class(self) -> Type[westAxis]:
        return cast(Type[westAxis], super().model_class)
    
    @property
    def null_exception(self) -> westAxisNullException:
        return cast(westAxisNullException, super().null_exception)