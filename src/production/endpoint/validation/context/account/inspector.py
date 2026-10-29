# src/production/endpoint/validation/context/account/inspector.py

"""
Module: production.endpoint.validation.context.account.inspector
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar, cast

from artifcat import ValidationResult
from assurance import AccountLayerToolkit
from domain import AccountContextPrimeExtract
from production import ContextInspector
from transit import AccountContextCarrier
from util import LoggingLevelRouter

T = TypeVar("T")

class AccountContextInspector(ContextInspector[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure an AccountContextCarrier and its payload are safe to use.

    Attributes:
        toolkit: AccountLayerToolkit

    Provides:
        -   def execute(
                    candidate: Any,
                    prime_extract: AccountContextPrimeExtract,
            ) -> ValidationResult[AccountContextCarrier]

    Super Class:
        ContextInspector
    """
    
    def __init__(
            self,
            toolkit: Optional[AccountLayerToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[AccountLayerToolkit]
        """
        super().__init__(toolkit=toolkit or AccountLayerToolkit())
        
    @property
    def toolkit(self) -> AccountLayerToolkit:
        return cast(AccountLayerToolkit, super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
            prime_extract: AccountContextPrimeExtract,
    ) -> ValidationResult[AccountContextCarrier]:
        """
        Assure a candidate is a safe AccountContext to use or build.
        
        Args:
            candidate: Any
            prime_extract: AccountContextPrimeExtract
        Returns:
            ValidationResult[AccountContextCarrier]
        Raises:
            AccountContextInspectorException
        """
        pass