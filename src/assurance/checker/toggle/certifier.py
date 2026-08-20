# src/assurance/certifier/root.py

"""
Module: assurance.certifier.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar, cast

from assurance.checker import Certifier
from result import ValidationResult
from toolkit import ToggleToolkit
from util import LoggingLevelRouter


T = TypeVar("T", bound="Toggle")


class ToggleCertifier(Certifier, Generic[T]):
    """
    Role
        -   Validator
        -   Integrity Assurance
        -   Consistency Assurance

    Responsibilities:
        1.  Runs integrity checks on Toggles and ToggleBlueprints before they are used.
        2.  Pluggable validation module.

    Attributes:
        toolkit: ToggleToolkit

    Provides:
        -   def validate(candidate: Any, toolkit: ToggleToolkit,) -> ValidationResult[Blueprint[T]]:

    Super Class:
    """

    def __init__(self, toolkit: ToggleToolkit[T],):
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> ToggleToolkit[T]:
        return cast(ToggleToolkit[T], super().bundle)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult:
        pass
    
    
