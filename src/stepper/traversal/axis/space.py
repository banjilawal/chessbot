# src/space/offset/axis/space.py

"""
Module: space.offset.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from math import AxisStepper
from space import TraversalPattern


class AxisTraversalPattern(TraversalPattern):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define a set of Vectors from an origin..
        2.  Provide the next point in the direction of travel.

    Attributes:
        stepper: AxisStepper

    Provides:

    Super Class:
        TraversalPattern
    """
    
    def __init__(self, stepper: AxisStepper,):
        """
        Args:
            stepper: AxisStepper
        """
        super().__init__(stepper=stepper)
    
    @property
    def stepper(self) -> AxisStepper:
        return cast(AxisStepper, self.stepper)
 
    