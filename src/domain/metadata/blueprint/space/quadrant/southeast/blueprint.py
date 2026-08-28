# src/domain/metadata/blueprint/space/quadrant/blueprint.py

"""
Module: domain.metadata.blueprint.space.quadrant.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain.metadata.blueprint import QuadrantBlueprint
from err import SoutheastQuadrantNullException
from domain.model import Vector
from space import SoutheastQuadrant


class SoutheastQuadrantBlueprint(QuadrantBlueprint[SoutheastQuadrant]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a SoutheastQuadrant.


     Attributes:
        origin: Vector
        domain_class: Type[SoutheastQuadrant]
        domain_null_exception: Optional[SoutheastQuadrantNullException]

     Provides:

     Super Class:
        QuadrantSpaceBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            domain_class: Type[SoutheastQuadrant] = SoutheastQuadrant,
            domain_null_exception: Optional[SoutheastQuadrantNullException] | None = None,
    ):
        """
        Args:
            origin: Vector
            domain_class: Type[SoutheastQuadrant]
            domain_null_exception: Optional[SoutheastQuadrantNullException]
        """
        super().__init__(
            origin=origin,
            domain_class=domain_class,
            domain_null_exception=domain_null_exception or SoutheastQuadrantNullException(),
        )
    
    @property
    def domain_class(self) -> Type[SoutheastQuadrant]:
        return cast(Type[SoutheastQuadrant], super().domain_class)
    
    @property
    def domain_null_exception(self) -> SoutheastQuadrantNullException:
        return cast(SoutheastQuadrantNullException, super().domain_null_exception)