# src/validator/space/span/validator.py

"""
Module: validator.space.span.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar

from result import ValidationResult
from validator import SpaceValidator

T = TypeVar("T", bound="Span")

class SpanValidator(SpaceValidator, Generic[T]):
    
    @abstractmethod
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass
    
    