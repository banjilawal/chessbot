# src/space/space.py

"""
Module: space.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from model import Vector
from space import SpaceBounds, SpaceStepper


class Space(ABC):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define points in a bounded space.
        2.  Provide a function that steps through every point in the plane,

    Attributes:
        bounds: SpaceBounds
        stepper: Stepper

    Provides:

    Super Class:
    """
    _bounds: SpaceBounds
    _stepper: SpaceStepper
    
    def __init__(self, bounds: SpaceBounds, stepper: SpaceStepper):
        """
        Args:
            bounds: SpaceBounds
            stepper: Stepper
        """
        self._bounds = bounds
        self._stepper = stepper
    
    @property
    def bounds(self) -> SpaceBounds:
        return self._bounds
    
    @property
    def stepper(self) -> SpaceStepper:
        return self._stepper
    
    @property
    @abstractmethod
    def origin(self) -> Vector:
        pass
    
    @property
    @abstractmethod
    def terminus(self) -> Vector:
        pass
    