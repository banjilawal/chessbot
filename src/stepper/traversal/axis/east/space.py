# src/space/offset/axis/east/space.py

"""
Module: space.offset.axis.east.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from math import EastAxisStepper
from space import AxisTraversalPattern


class EastTraversalPattern(AxisTraversalPattern):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Provide a set of target vectors which are east of origin.

    Attributes:
        stepper: Optional[EastAxisStepper]

    Provides:

    Super Class:
        AxisTraversalPattern
    """
    
    def __init__(
            self,
            stepper: Optional[EastAxisStepper] | None = EastAxisStepper(),
    ):
        """
        Args:
            stepper: Optional[EastAxisStepper]
        """
        super().__init__(stepper=stepper)
    
    @property
    def stepper(self) -> EastAxisStepper:
        return cast(EastAxisStepper, self.stepper)