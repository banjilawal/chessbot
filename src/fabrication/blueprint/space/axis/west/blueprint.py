# src/blueprint/space/axis/blueprint.py

"""
Module: blueprint.space.axis.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type, cast

from fabrication.blueprint import AxisBlueprint
from err import WestAxisNullException
from model import Vector
from geometry.space import WestAxis


class WestAxisBlueprint(AxisBlueprint[WestAxis]):
    """
     Role:
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a WestAxis.


     Attributes:
        origin: Vector
        model_class: Type[WestAxis]
        null_exception: Optional[WestAxisNullException]

     Provides:

     Super Class:
        AxisSBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            terminus: Optional[Vector] | None = None,
            model_class: Type[WestAxis] = WestAxis,
            null_exception: Optional[WestAxisNullException] | None = None,
    ):
        """
        Args:
            origin: Vector
            terminus: Optional[Vector]
            model_class: Type[WestAxis]
            null_exception: Optional[WestAxisNullException]
        """
        super().__init__(
            origin=origin,
            terminus=terminus,
            model_class=model_class,
            null_exception=null_exception or WestAxisNullException(),
        )
    
    @property
    def model_class(self) -> Type[WestAxis]:
        return cast(Type[WestAxis], super().model_class)
    
    @property
    def null_exception(self) -> WestAxisNullException:
        return cast(WestAxisNullException, super().null_exception)