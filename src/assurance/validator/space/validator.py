# src/assurance/validator/space/validator.py

"""
Module: assurance.validator.space.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from util import LoggingLevelRouter
from assurance.validator import Validator

T = TypeVar("T", bound="Space")

class SpaceValidator(Validator, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[T]:
        pass
    
    