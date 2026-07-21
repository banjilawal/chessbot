# src/space/offset/axis/west/space.py

"""
Module: space.offset.axis.west.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from register import VectorRegister
from space import AxisTraversalPattern, WestAxisStepper


class WestTraversalPattern(AxisTraversalPattern):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Provide a set of target vectors which are west of origin.

    Attributes:
        endpoints: VectorRegister
        stepper: WestAxisStepper

    Provides:

    Super Class:
        Axis
    """
    _endpoints: VectorRegister
    _stepper: WestAxisStepper
    
    def __init__(
            self,
            endpoints: VectorRegister,
            stepper: Optional[WestAxisStepper] | None = WestAxisStepper(),
    ):
        """
        Args:
            endpoints: VectorRegister
            stepper: WestAxisStepper
        """
        super().__init__(endpoints=endpoints, stepper=stepper)
    
    @property
    def endpoints(self) -> VectorRegister:
        return self._endpoints
    
    @property
    def stepper(self) -> WestAxisStepper:
        return cast(WestAxisStepper, self.stepper)