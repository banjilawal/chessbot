# src/space/offset/axis/north/space.py

"""
Module: space.offset.axis.north.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from math import NorthAxisStepper
from register import VectorRegister
from space import AxisTraversalPattern


class NorthTraversalPattern(AxisTraversalPattern):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Provide a set of target vectors which are north of origin.

    Attributes:
        stepper: Optional[NorthAxisStepper]

    Provides:

    Super Class:
        AxisTraversalPattern
    """
    
    def __init__(
            self,
            stepper: Optional[NorthAxisStepper] | None = NorthAxisStepper(),
    ):
        """
        Args:
            stepper: Optional[NorthAxisStepper]
        """
        super().__init__(stepper=stepper)
    
    @property
    def stepper(self) -> NorthAxisStepper:
        return cast(NorthAxisStepper, self.stepper)