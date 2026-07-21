# src/space/offset/quadrant/northeast/space.py

"""
Module: space.offset.quadrant.northeast.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from math import NortheastQuadrantStepper
from space import QuadrantTraversalPattern


class NortheastTraversalPattern(QuadrantTraversalPattern):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Find the set of target vectors northeast of the origin.

    Attributes:
        stepper: Optional[NortheastQuadrantStepper]

    Provides:

    Super Class:
        QuadrantTraversalPattern
    """
    
    def __init__(
            self,
            stepper: Optional[NortheastQuadrantStepper] | None = NortheastQuadrantStepper(),
    ):
        """
        Args:,
            stepper: Optional[NortheastQuadrantStepper]
        """
        super().__init__(stepper=stepper)
        

    @property
    def stepper(self) -> NortheastQuadrantStepper:
        return cast(NortheastQuadrantStepper, self.stepper)

        
    