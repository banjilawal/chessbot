# src/space/offset/axis/south/space.py

"""
Module: space.offset.axis.south.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from register import VectorRegister
from space import AxisTraversalPattern, SouthAxisStepper


class SouthTraversalPattern(AxisTraversalPattern):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Provide a set of target vectors which are south of origin.

    Attributes:
        endpoints: VectorRegister
        stepper: SouthAxisStepper

    Provides:

    Super Class:
        Axis
    """
    _endpoints: VectorRegister
    _stepper: SouthAxisStepper
    
    def __init__(
            self,
            endpoints: VectorRegister,
            stepper: Optional[SouthAxisStepper] | None = SouthAxisStepper(),
    ):
        """
        Args:
            endpoints: VectorRegister
            stepper: SouthAxisStepper
        """
        super().__init__(endpoints=endpoints, stepper=stepper)
    
    @property
    def endpoints(self) -> VectorRegister:
        return self._endpoints
    
    @property
    def stepper(self) -> SouthAxisStepper:
        return cast(SouthAxisStepper, self.stepper)