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
from err import EastAxisNullException
from domain.model import Vector
from space import EastAxis


class EastAxisBlueprint(AxisBlueprint[EastAxis]):
    """
     Role:
         -  DTO

     Responsibilities:
         1.  Provides values for hydrating a EastAxis.


     Attributes:
        origin: Vector
        domain_class: Type[EastAxis]
        domain_null_exception: Optional[EastAxisNullException]

     Provides:

     Super Class:
        AxisBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            terminus: Optional[Vector] | None = None,
            domain_class: Type[EastAxis] = EastAxis,
            domain_null_exception: Optional[EastAxisNullException] | None = None,
    ):
        """
        Args:
            origin: Vector
            terminus: Optional[Vector]
            domain_class: Type[EastAxis]
            domain_null_exception: Optional[EastAxisNullException]
        """
        super().__init__(
            origin=origin,
            domain_class=domain_class,
            domain_null_exception=domain_null_exception or EastAxisNullException(),
        )
    
    @property
    def domain_class(self) -> Type[EastAxis]:
        return cast(Type[EastAxis], super().domain_class)
    
    @property
    def domain_null_exception(self) -> EastAxisNullException:
        return cast(EastAxisNullException, super().domain_null_exception)