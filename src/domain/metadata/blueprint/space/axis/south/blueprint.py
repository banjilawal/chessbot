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
from err import SouthAxisNullException
from domain.model import Vector
from space import SouthAxis


class SouthAxisBlueprint(AxisBlueprint[SouthAxis]):
    """
     Role:
         -  DTO

     Responsibilities:
         1.  Provides values for hydrating a SouthAxis.


     Attributes:
        origin: Vector
        domain_class: Type[SouthAxis]
        domain_null_exception: Optional[SouthAxisNullException]

     Provides:

     Super Class:
        AxisBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            terminus: Optional[Vector] | None = None,
            domain_class: Type[SouthAxis] = SouthAxis,
            domain_null_exception: Optional[SouthAxisNullException] | None = None,
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
            domain_null_exception=domain_null_exception or SouthAxisNullException(),
        )
    
    @property
    def domain_class(self) -> Type[SouthAxis]:
        return cast(Type[SouthAxis], super().domain_class)
    
    @property
    def domain_null_exception(self) -> SouthAxisNullException:
        return cast(SouthAxisNullException, super().domain_null_exception)