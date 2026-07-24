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
from err import EastAxisNullException
from model import Vector
from space import EastAxis


class EastAxisBlueprint(AxisBlueprint[EastAxis]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a AxisSpace object.
         2.  DTO

     Attributes:
        origin: Vector
        model_class: Type[EastAxis]
        null_exception: Optional[EastAxisNullException]

     Provides:

     Super Class:
        AxisSpaceBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            model_class: Type[EastAxis],
            null_exception: Optional[EastAxisNullException] |
                            None = EastAxisNullException(),
    ):
        """
        Args:
            origin: Vector
            model_class: Type[EastAxis]
            null_exception: Optional[EastAxisNullException]
        """
        super().__init__(
            origin=origin,
            model_class=model_class,
            null_exception=null_exception
        )
        
    
    @property
    def model_class(self) -> Type[EastAxis]:
        return cast(Type[EastAxis], super().model_class)
    
    @property
    def null_exception(self) -> EastAxisNullException:
        return cast(EastAxisNullException, super().null_exception)