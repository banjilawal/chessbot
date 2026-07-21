# src/space/offset/axis/east/space.py

"""
Module: space.offset.axis.east.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from register import VectorRegister
from space import AxisTraversalPattern, EastAxisStepper


class EastTraversalPattern(AxisTraversalPattern):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Provide a set of target vectors which are east of origin.

    Attributes:
        endpoints: VectorRegister
        stepper: EastAxisStepper

    Provides:

    Super Class:
        Axis
    """
    _endpoints: VectorRegister
    _stepper: EastAxisStepper
    
    def __init__(
            self,
            endpoints: VectorRegister,
            stepper: Optional[EastAxisStepper] | None = EastAxisStepper(),
    ):
        """
        Args:
            endpoints: VectorRegister
            stepper: EastAxisStepper
        """
        super().__init__(endpoints=endpoints, stepper=stepper)
    
    @property
    def endpoints(self) -> VectorRegister:
        return self._endpoints
    
    @property
    def stepper(self) -> EastAxisStepper:
        return cast(EastAxisStepper, self.stepper)