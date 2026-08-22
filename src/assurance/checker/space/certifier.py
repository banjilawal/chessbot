# src/root/space/assurance/checker.py

"""
Module: root.space.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar, cast

from domain.metadata.blueprint import SpaceBlueprint
from assurance.checker import Checker
from result import ValidationResult
from toolkit import SpaceToolkit
from util import LoggingLevelRouter


T = TypeVar("T", bound="Space")


class SpaceChecker(Checker, Generic[T]):
    """
    Role
        -   Validator
        -   Integrity Assurance
        -   Consistency Assurance

    Responsibilities:
        1.  Runs integrity checks on Spaces and SpaceBlueprints before they are used.
        2.  Pluggable validation module.

    Attributes:
        bundle: SpaceToolkit

    Provides:
        -   def execute(candidate: Any, bundle: SpaceToolkit,) -> ValidationResult[Blueprint[T]]:

    Super Class:
    """

    def __init__(self, bundle: SpaceToolkit[T],):
        super().__init__(bundle=bundle)
        
    @property
    def toolkit(self) -> SpaceToolkit[T]:
        return cast(SpaceToolkit[T], super().bundle)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult[T|SpaceBlueprint[T]]:
        pass
    
    
