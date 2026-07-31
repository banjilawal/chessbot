# src/root/space/quadrant/root/space.py

"""
Module: root.space.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar, cast

from blueprint import Blueprint
from result import ValidationResult
from root import SpaceRootCertifier
from toolkit import QuadrantToolkit

from util import LoggingLevelRouter

T = TypeVar("T", bound="Quadrant")

class QuadrantRootCertifier(SpaceRootCertifier, Generic[T]):
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

    def __init__(self, toolkit: QuadrantToolkit[T]):
        """
        Args:
            toolkit: QuadrantToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> QuadrantToolkit[T]:
        return cast(QuadrantToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T|Blueprint[T]]:
        pass
        

        
    