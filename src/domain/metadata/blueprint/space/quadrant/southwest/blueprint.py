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
from err import SouthwestQuadrantNullException
from domain.model import Vector
from space import SouthwestQuadrant


class SouthwestQuadrantBlueprint(QuadrantBlueprint[SouthwestQuadrant]):
    """
     Role:
         -  DTO

     Responsibilities:
         1.  Provides values for hydrating a SouthwestQuadrant.


     Attributes:
        origin: Vector
        domain_class: Type[SouthwestQuadrant]
        domain_null_exception: Optional[SouthwestQuadrantNullException]

     Provides:

     Super Class:
        QuadrantSpaceBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            domain_class: Type[SouthwestQuadrant] = SouthwestQuadrant,
            domain_null_exception: Optional[SouthwestQuadrantNullException] | None = None,
    ):
        """
        Args:
            origin: Vector
            domain_class: Type[SouthwestQuadrant]
            domain_null_exception: Optional[SouthwestQuadrantNullException]
        """
        super().__init__(
            origin=origin,
            domain_class=domain_class,
            domain_null_exception=domain_null_exception or SouthwestQuadrantNullException(),
        )
    
    @property
    def domain_class(self) -> Type[SouthwestQuadrant]:
        return cast(Type[SouthwestQuadrant], super().domain_class)
    
    @property
    def domain_null_exception(self) -> SouthwestQuadrantNullException:
        return cast(SouthwestQuadrantNullException, super().domain_null_exception)