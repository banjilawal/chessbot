# src/space/offset/axis/south/space.py

"""
Module: space.offset.axis.south.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from math import SouthAxisStepper
from space import AxisTraversalPattern


class SouthTraversalPattern(AxisTraversalPattern):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Provide a set of target vectors which are south of origin.

    Attributes:
        stepper: Optional[SouthAxisStepper]

    Provides:

    Super Class:
        AxisTraversalPattern
    """
    
    def __init__(
            self,
            stepper: Optional[SouthAxisStepper] | None = SouthAxisStepper(),
    ):
        """
        Args:
            stepper: Optional[SouthAxisStepper]
        """
        super().__init__(stepper=stepper,)

    @property
    def stepper(self) -> SouthAxisStepper:
        return cast(SouthAxisStepper, self.stepper)