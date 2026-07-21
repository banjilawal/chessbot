# src/space/offset/quadrant/northeast/space.py

"""
Module: space.offset.quadrant.northeast.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from register import VectorRegister
from space import NortheastQuadrantStepper, QuadrantTraversalPattern


class NortheastTraversalPattern(QuadrantTraversalPattern):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Find the set of target vectors northeast of the origin.

    Attributes:
        endpoints: VectorRegister,
        stepper: Optional[NortheastQuadrantStepper]

    Provides:

    Super Class:
        Quadrant
    """
    
    def __init__(
            self,
            endpoints: VectorRegister,
            stepper: Optional[NortheastQuadrantStepper] | None = NortheastQuadrantStepper(),
    ):
        """
        Args:
            endpoints: VectorRegister,
            stepper: Optional[NortheastQuadrantStepper]
        """
        super().__init__(endpoints=endpoints, stepper=stepper)
        

    @property
    def stepper(self) -> NortheastQuadrantStepper:
        return cast(NortheastQuadrantStepper, self.stepper)

        
    