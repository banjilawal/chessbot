# src/root/space/quadrant/root/space.py

"""
Module: root.space.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar, cast

from domain.metadata.blueprint import Blueprint
from artifcat.result import ValidationResult
from assurance.checker import SpaceChecker
from operation.toolkit import QuadrantToolkit

from util import LoggingLevelRouter

T = TypeVar("T", bound="Quadrant")

class QuadrantRootChecker(SpaceChecker, Generic[T]):
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

    def __init__(self, bundle: QuadrantToolkit[T]):
        """
        Args:
            bundle: QuadrantToolkit[T]
        """
        super().__init__(bundle=bundle)
    
    @property
    def toolkit(self) -> QuadrantToolkit[T]:
        return cast(QuadrantToolkit[T], super().ruleset)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T|Blueprint[T]]:
        pass
        

        
    