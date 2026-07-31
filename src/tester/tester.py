# src/tester/tester.py

"""
Module: tester.tester
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from result import ValidationResult
from util import LoggingLevelRouter
from validator import PrimingValidator


T = TypeVar("T", bound="Request")

class RequestTester(ABC, Generic[T]):
    
    _bootstrapper: Optional[PrimingValidator]
    
    def __init__(self, bootstrapper: Optional[PrimingValidator] | None = None):
        self._bootstrapper = bootstrapper or PrimingValidator()
        
    @property
    def bootstrapper(self) -> PrimingValidator:
        return self._bootstrapper
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def exception(self, candidate: Any) -> ValidationResult[T]:
        pass