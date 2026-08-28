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
from err import NortheastQuadrantNullException
from domain.model import Vector
from space import NortheastQuadrant


class NortheastQuadrantBlueprint(QuadrantBlueprint[NortheastQuadrant]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a NortheastQuadrant.


     Attributes:
        origin: Vector
        domain_class: Type[NortheastQuadrant]
        domain_null_exception: Optional[NortheastQuadrantNullException]

     Provides:

     Super Class:
        QuadrantSpaceBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            domain_class: Type[NortheastQuadrant] = NortheastQuadrant,
            domain_null_exception: Optional[NortheastQuadrantNullException] | None = None,
    ):
        """
        Args:
            origin: Vector
            domain_class: Type[NortheastQuadrant]
            domain_null_exception: Optional[NortheastQuadrantNullException]
        """
        super().__init__(
            origin=origin,
            domain_class=domain_class,
            domain_null_exception=domain_null_exception or NortheastQuadrantNullException(),
        )
    
    @property
    def domain_class(self) -> Type[NortheastQuadrant]:
        return cast(Type[NortheastQuadrant], super().domain_class)
    
    @property
    def domain_null_exception(self) -> NortheastQuadrantNullException:
        return cast(NortheastQuadrantNullException, super().domain_null_exception)