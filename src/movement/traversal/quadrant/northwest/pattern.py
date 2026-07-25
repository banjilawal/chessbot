# src/space/offset/quadrant/northwest/space.py

"""
Module: space.offset.quadrant.northwest.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from math import NorthwestQuadrantStepper
from space import QuadrantTraversalPattern


class NorthwestTraversalPattern(QuadrantTraversalPattern):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Find the set of target vectors northwest of the origin.

    Attributes:
        stepper: Optional[NorthwestQuadrantStepper]

    Provides:

    Super Class:
        QuadrantTraversalPattern
    """
    
    def __init__(
            self,
            stepper: Optional[NorthwestQuadrantStepper] | None = NorthwestQuadrantStepper(),
    ):
        """
        Args:
            stepper: Optional[NorthwestQuadrantStepper]
        """
        super().__init__(stepper=stepper)
        

    @property
    def stepper(self) -> NorthwestQuadrantStepper:
        return cast(NorthwestQuadrantStepper, self.stepper)

        
    