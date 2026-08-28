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
from err import NorthwestQuadrantNullException
from domain.model import Vector
from space import NorthwestQuadrant


class NorthwestQuadrantBlueprint(QuadrantBlueprint[NorthwestQuadrant]):
    """
     Role:
         -  DTO

     Responsibilities:
         1.  Provides values for hydrating a NorthwestQuadrant.


     Attributes:
        origin: Vector
        domain_class: Type[NorthwestQuadrant]
        domain_null_exception: Optional[NorthwestQuadrantNullException]

     Provides:

     Super Class:
        QuadrantSpaceBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            domain_class: Type[NorthwestQuadrant] = NorthwestQuadrant,
            domain_null_exception: Optional[NorthwestQuadrantNullException] | None = None,
    ):
        """
        Args:
            origin: Vector
            domain_class: Type[NorthwestQuadrant]
            domain_null_exception: Optional[NorthwestQuadrantNullException]
        """
        super().__init__(
            origin=origin,
            domain_class=domain_class,
            domain_null_exception=domain_null_exception or NorthwestQuadrantNullException(),
        )
    
    @property
    def domain_class(self) -> Type[NorthwestQuadrant]:
        return cast(Type[NorthwestQuadrant], super().domain_class)
    
    @property
    def domain_null_exception(self) -> NorthwestQuadrantNullException:
        return cast(NorthwestQuadrantNullException, super().domain_null_exception)