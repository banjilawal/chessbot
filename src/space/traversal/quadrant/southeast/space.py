# src/space/offset/quadrant/southeast/space.py

"""
Module: space.offset.quadrant.southeast.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from register import VectorRegister
from space import SoutheastQuadrantStepper, QuadrantTraversalPattern


class SoutheastTraversalPattern(QuadrantTraversalPattern):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Find the set of target vectors southeast of the origin.

    Attributes:
        endpoints: VectorRegister,
        stepper: Optional[SoutheastQuadrantStepper]

    Provides:

    Super Class:
        Quadrant
    """
    
    def __init__(
            self,
            endpoints: VectorRegister,
            stepper: Optional[SoutheastQuadrantStepper] | None = SoutheastQuadrantStepper(),
    ):
        """
        Args:
            endpoints: VectorRegister,
            stepper: Optional[SoutheastQuadrantStepper]
        """
        super().__init__(endpoints=endpoints, stepper=stepper)
        

    @property
    def stepper(self) -> SoutheastQuadrantStepper:
        return cast(SoutheastQuadrantStepper, self.stepper)

        
    