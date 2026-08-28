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
from err import NorthAxisNullException
from domain.model import Vector
from space import NorthAxis


class NorthAxisBlueprint(AxisBlueprint[NorthAxis]):
    """
     Role:
         -  DTO

     Responsibilities:
         1.  Provides values for hydrating a NorthAxis.


     Attributes:
        origin: Vector
        domain_class: Type[NorthAxis]
        domain_null_exception: Optional[NorthAxisNullException]

     Provides:

     Super Class:
        AxisBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            terminus: Optional[Vector] | None = None,
            domain_class: Type[NorthAxis] = NorthAxis,
            domain_null_exception: Optional[NorthAxisNullException] | None = None,
    ):
        """
        Args:
            origin: Vector
            terminus: Optional[Vector]
            domain_class: Type[NorthAxis]
            domain_null_exception: Optional[NorthAxisNullException]
        """
        super().__init__(
            origin=origin,
            terminus=terminus,
            domain_class=domain_class,
            domain_null_exception=domain_null_exception or NorthAxisNullException(),
        )
    
    @property
    def domain_class(self) -> Type[NorthAxis]:
        return cast(Type[NorthAxis], super().domain_class)
    
    @property
    def domain_null_exception(self) -> NorthAxisNullException:
        return cast(NorthAxisNullException, super().domain_null_exception)