# src/validator/space/validator.py

"""
Module: validator.space.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar

from result import ValidationResult
from util import LoggingLevelRouter
from validator import Validator

T = TypeVar("T", bound="Space")

class SpaceValidator(Validator, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass
    
    