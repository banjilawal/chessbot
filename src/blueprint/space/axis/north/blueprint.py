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
from err import NorthAxisNullException, AxisNullException
from model import Vector
from space import NorthAxis, Space, AxisSpace


class NorthAxisBlueprint(AxisBlueprint[NorthAxis]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a AxisSpace object.
         2.  DTO

     Attributes:
        origin: Vector
        model_class: Type[NorthAxis]
        null_exception: Optional[NorthAxisNullException]

     Provides:

     Super Class:
        AxisSpaceBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            model_class: Type[NorthAxis],
            null_exception: Optional[NorthAxisNullException] |
                            None = NorthAxisNullException(),
    ):
        """
        Args:
            origin: Vector
            model_class: Type[NorthAxis]
            null_exception: Optional[NorthAxisNullException]
        """
        super().__init__(
            origin=origin,
            model_class=model_class,
            null_exception=null_exception
        )
        
    
    @property
    def model_class(self) -> Type[NorthAxis]:
        return cast(Type[NorthAxis], super().model_class)
    
    @property
    def null_exception(self) -> NorthAxisNullException:
        return cast(NorthAxisNullException, super().null_exception)