# src/space/offset/axis/north/space.py

"""
Module: space.offset.axis.north.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from register import VectorRegister
from space import AxisTraversalPattern, NorthAxisStepper


class NorthTraversalPattern(AxisTraversalPattern):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Provide a set of target vectors which are north of origin.

    Attributes:
        endpoints: VectorRegister
        stepper: NorthAxisStepper

    Provides:

    Super Class:
        Axis
    """
    _endpoints: VectorRegister
    _stepper: NorthAxisStepper
    
    def __init__(
            self,
            endpoints: VectorRegister,
            stepper: Optional[NorthAxisStepper] | None = NorthAxisStepper(),
    ):
        """
        Args:
            endpoints: VectorRegister
            stepper: NorthAxisStepper
        """
        super().__init__(endpoints=endpoints, stepper=stepper)
    
    @property
    def endpoints(self) -> VectorRegister:
        return self._endpoints
    
    @property
    def stepper(self) -> NorthAxisStepper:
        return cast(NorthAxisStepper, self.stepper)