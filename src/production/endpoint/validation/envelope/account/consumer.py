# src/production/endpoint/envelope/account/consumer.py

"""
Module: production.endpoint.envelope.account.consumer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ValidationResult
from assurance import AccountLayerToolkit
from domain import Account
from production import EnvelopeConsumer
from transit import AccountCarrier, AccountEnvelope
from util import LoggingLevelRouter

T = TypeVar("T", bound="Account")


class AccountEnvelopeConsumer(EnvelopeConsumer[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure an Account covered by a RootEncounerEnvelope is safe.

    Attributes:
        toolkit: AccountLayerToolkit

    Provides:
        -   def execute(envelope: RootAccountEnvelope) -> ValidationResult[AccountCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    
    def __init__(self, toolkit: Optional[AccountLayerToolkit] | None = None):
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
    def execute(self, envelope: AccountEnvelope) -> ValidationResult[AccountCarrier]:
        pass