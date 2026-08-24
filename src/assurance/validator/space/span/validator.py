# src/assurance/validator/space/span/validator.py

"""
Module: assurance.validator.space.span.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from assurance.validator import SpaceValidator

T = TypeVar("T", bound="Span")

class SpanValidator(SpaceValidator, Generic[T]):
    
       @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass
    
    