# src/blueprint/space/axis/blueprint.py

"""
Module: blueprint.space.axis.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional, Type, cast

from blueprint import AxisBlueprint
from err import SouthAxisNullException
from model import Vector
from space import SouthAxis


class SouthAxisBlueprint(AxisBlueprint[SouthAxis]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a AxisSpace object.
         2.  DTO

     Attributes:
        origin: Vector
        model_class: Type[SouthAxis]
        null_exception: Optional[SouthAxisNullException]

     Provides:

     Super Class:
        AxisSpaceBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            model_class: Type[SouthAxis],
            null_exception: Optional[SouthAxisNullException] |
                            None = SouthAxisNullException(),
    ):
        """
        Args:
            origin: Vector
            model_class: Type[SouthAxis]
            null_exception: Optional[SouthAxisNullException]
        """
        super().__init__(
            origin=origin,
            model_class=model_class,
            null_exception=null_exception
        )
    
    @property
    def model_class(self) -> Type[SouthAxis]:
        return cast(Type[SouthAxis], super().model_class)
    
    @property
    def null_exception(self) -> SouthAxisNullException:
        return cast(SouthAxisNullException, super().null_exception)