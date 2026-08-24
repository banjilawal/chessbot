# src/assurance/validator/space/linear/validator.py

"""
Module: assurance.validator.space.linear.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from util import LoggingLevelRouter
from assurance.validator import SpaceValidator

T = TypeVar("T", bound="LinearSpace")

class LinearSpaceValidator(SpaceValidator, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass
    
    