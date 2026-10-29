# src/production/endpoint/validation/context/id/inspector.py

"""
Module: production.endpoint.validation.context.id.inspector
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

class IdContextInspector(ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a ContextCarrier with an id payload is safe to use.

    Attributes:
        identity_service: IdentityService
        
    Provides:
        -   def execute(
                    candidate: Any,
                    prime_extract: AccountContextPrimeExtract,
            ) -> ValidationResult[AccountContextCarrier]

    Super Class:
    """

    _identity_service: IdentityService
    
    def __init__(self, identity_service: Optional[IdentityService] | None = None):
        """
        Args:
            identity_service: Optional[IdentityService]
        """
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
        """
        Assure a candidate is a safe Id-Context to use or build.

        Args:
            candidate: Any
            prime_extract: AccountContextPrimeExtract
        Returns:
            ValidationResult[ContextCarrier[T]]
        Raises:
            IdContextInspectorException
        """
        pass