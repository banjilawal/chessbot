# src/root/space/reservoir/__init__.py

"""
Module: root.space.reservoir.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from domain.metadata.blueprint import SpaceReservoirBlueprint
from assurance.validator import Validator
from artifcat import ValidationResult
from operation.toolkit import SpaceReservoirToolkit
from util import LoggingLevelRouter


T = TypeVar("T", bound="SpaceReservoir")


class SpaceReservoirValidator(Validator, ABC, Generic[T]):
    """
    Role
        -  Validator
        -  Integrity Assurance
        -  Consistency Assurance

    Responsibilities:
        1.  Runs integrity checks on Spaces and SpaceBlueprints before they are used.
        2.  Pluggable validation module.

    Attributes:
        bundle: SpaceToolkit

    Provides:
        -  def execute(candidate: Any, bundle: SpaceToolkit,) -> ValidationResult[Blueprint[T]]:

    Super Class:
    """

    def __init__(self, bundle: SpaceReservoirToolkit[T],):
        super().__init__(bundle=bundle)
        
    @property
    def toolkit(self) -> SpaceReservoirToolkit[T]:
        return cast(SpaceReservoirToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult[T|SpaceReservoirBlueprint[T]]:
        pass
    
    
