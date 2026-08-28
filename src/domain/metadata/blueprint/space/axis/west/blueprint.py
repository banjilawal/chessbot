# src/domain/metadata/blueprint/space/axis/blueprint.py

"""
Module: domain.metadata.blueprint.space.axis.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain.metadata.blueprint import AxisBlueprint
from err import WestAxisNullException
from domain.model import Vector
from space import WestAxis


class WestAxisBlueprint(AxisBlueprint[WestAxis]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a WestAxis.


     Attributes:
        origin: Vector
        domain_class: Type[WestAxis]
        domain_null_exception: Optional[WestAxisNullException]

     Provides:

     Super Class:
        AxisSBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            terminus: Optional[Vector] | None = None,
            domain_class: Type[WestAxis] = WestAxis,
            domain_null_exception: Optional[WestAxisNullException] | None = None,
    ):
        """
        Args:
            origin: Vector
            terminus: Optional[Vector]
            domain_class: Type[WestAxis]
            domain_null_exception: Optional[WestAxisNullException]
        """
        super().__init__(
            origin=origin,
            terminus=terminus,
            domain_class=domain_class,
            domain_null_exception=domain_null_exception or WestAxisNullException(),
        )
    
    @property
    def domain_class(self) -> Type[WestAxis]:
        return cast(Type[WestAxis], super().domain_class)
    
    @property
    def domain_null_exception(self) -> WestAxisNullException:
        return cast(WestAxisNullException, super().domain_null_exception)