# src/space/offset/axis/west/space.py

"""
Module: space.offset.axis.west.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from math import WestAxisStepper
from space import AxisTraversalPattern


class WestTraversalPattern(AxisTraversalPattern):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Provide a set of target vectors which are west of origin.

    Attributes:
        stepper: Optional[WestAxisMapper]

    Provides:

    Super Class:
        AxisTraversalPattern
    """
    
    def __init__(
            self,
            stepper: Optional[WestAxisStepper] | None = WestAxisStepper(),
    ):
        """
        Args:
            stepper: Optional[WestAxisMapper]
        """
        super().__init__(stepper=stepper)
    
    @property
    def stepper(self) -> WestAxisStepper:
        return cast(WestAxisStepper, self.stepper)