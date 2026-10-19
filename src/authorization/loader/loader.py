# src/authorization/loader/loader.py

"""
Module: authorization.loader.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from assurance import PrimingValidator
from exchange import Request
from util import LoggingLevelRouter

T = TypeVar("T", bound="Request")

class AuthorizationLoader(ABC, Generic[T]):
    _priming_validator: PrimingValidator
    
    def __init__(self, priming_validator: Optional[PrimingValidator] | None = None):
        """
        Args:
            priming_validator: Optional[PrimingValidator]
        """
        self._priming_validator = priming_validator
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> T:
        pass