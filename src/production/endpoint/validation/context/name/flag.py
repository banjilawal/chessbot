# src/production/endpoint/validation/context/flag.py

"""
Module: production.endpoint.validation.context.flag
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from artifcat import ValidationResult
from domain import Context, ContextPrimeExtract
from microservice import IdentityService
from transit import ContextCarrier
from util import LoggingLevelRouter

T = TypeVar("T", bound="Context")

class NameContextFlagValidator(ABC, Generic[T]):

    identity_service: IdentityService
    
    def __init__(self, identity_service: Optional[IdentityService] | None = None):
        self._identity_service = identity_service or IdentityService()
        
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
            prime_extract: ContextPrimeExtract[T],
    ) -> ValidationResult[ContextCarrier[T]]:
        pass