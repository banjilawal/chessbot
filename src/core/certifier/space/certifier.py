# src/root/space/core/certifier.py

"""
Module: root.space.certifier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar, cast

from blueprint import SpaceBlueprint
from core.certifier import Certifier
from result import ValidationResult
from toolkit import SpaceToolkit
from util import LoggingLevelRouter


T = TypeVar("T", bound="Space")


class SpaceCertifier(Certifier, Generic[T]):
    """
    Role
        -   Validator
        -   Integrity Assurance
        -   Consistency Assurance

    Responsibilities:
        1.  Runs integrity checks on Spaces and SpaceBlueprints before they are used.
        2.  Pluggable validation module.

    Attributes:
        toolkit: SpaceToolkit

    Provides:
        -   def execute(candidate: Any, toolkit: SpaceToolkit,) -> ValidationResult[Blueprint[T]]:

    Super Class:
    """

    def __init__(self, toolkit: SpaceToolkit[T],):
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> SpaceToolkit[T]:
        return cast(SpaceToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult[T|SpaceBlueprint[T]]:
        pass
    
    
