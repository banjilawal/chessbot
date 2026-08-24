# src/root/space/axis/root/space.py

"""
Module: root.space.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar, cast


from artifcat import ValidationResult
from assurance.checker import SpaceChecker
from operation.toolkit import AxisToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Axis")

class AxisRootChecker(SpaceChecker, Generic[T]):
    """
    Role:
        -   Definition

    Responsibilities:
        1.  A horizontal or vertical line whose root is the Space's origin.

    Attributes:
        origin: Vector
        terminus: Vector
        
    Provides:

    Super Class:
        SpaceRootChecker
    """

    def __init__(self, bundle: AxisToolkit[T]):
        """
        Args:
            bundle: AxisToolkit[T]
        """
        super().__init__(bundle=bundle)
    
    @property
    def toolkit(self) -> AxisToolkit[T]:
        return cast(AxisToolkit[T], super().ruleset)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass
        

        
    