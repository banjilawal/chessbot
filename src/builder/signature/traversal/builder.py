# src/blueprint/pattern/traversal/blueprint.py

"""
Module: blueprint.pattern.traversal.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from blueprint import SignatureBlueprint
from util import LoggingLevelRouter

T = TypeVar("T", bound="TraversalSignature")

class TraversalBlueprint(SignatureBlueprint, ABC, Generic[T]):
    """
    Role:
        -   Iteration


    Responsibilities:
        1.  Stepping function which gives the next vector in a series.

    Attributes:
        stepper: Stepper
        math_toolkit: Optional[MathToolkit]

    Provides:

    Super Class:
    """
    
    def __init__(self, blueprint_toolkit: TraversalBlueprintToolkit[T]):
        super().__init__(blueprint_toolkit=blueprint_toolkit)
        
    @property
    def blueprint_toolkit(self) -> TraversalBlueprintToolkit[T]:
        return cast(TraversalBlueprintToolkit[T], super().blueprint_toolkit)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: TraversalBlueprint[T]) -> BuildResult[T]:
        pass