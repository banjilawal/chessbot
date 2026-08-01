# src/root/space/axis/root/space.py

"""
Module: root.space.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar, cast


from result import ValidationResult
from core.certifier import SpaceCertifier
from toolkit import AxisToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Axis")

class AxisRootCertifier(SpaceCertifier, Generic[T]):
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
        SpaceRootCertifier
    """

    def __init__(self, toolkit: AxisToolkit[T]):
        """
        Args:
            toolkit: AxisToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> AxisToolkit[T]:
        return cast(AxisToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass
        

        
    