# src/space/linear/quadrant/northwest/space.py

"""
Module: space.linear.quadrant.northwest.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from math import NorthwestQuadrantStepper
from register import VectorRegister
from space import Quadrant


class NorthwestQuadrant(Quadrant):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Find the set of target vectors northwest of the origin.

    Attributes:
        endpoints: VectorRegister,
        stepper: Optional[NorthwestQuadrantStepper]

    Provides:

    Super Class:
        Quadrant
    """
    
    def __init__(
            self,
            endpoints: VectorRegister,
            stepper: Optional[NorthwestQuadrantStepper] | None = NorthwestQuadrantStepper(),
    ):
        """
        Args:
            endpoints: VectorRegister,
            stepper: Optional[NorthwestQuadrantStepper]
        """
        super().__init__(endpoints=endpoints, stepper=stepper)
        

    @property
    def stepper(self) -> NorthwestQuadrantStepper:
        return cast(NorthwestQuadrantStepper, self.stepper)

        
    