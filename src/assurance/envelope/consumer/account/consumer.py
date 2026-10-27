# src/assurance/envelope/consumer/account/consumer.py

"""
Module: assurance.envelope.consumer.account.consumer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ValidationResult
from assurance import AccountLayerToolkit, RootEnvelopeConsumer
from domain import Account
from transit import AccountCarrier, RootAccountEnvelope
from util import LoggingLevelRouter

T = TypeVar("T", bound="Account")


class AccountEnvelopeConsumer(RootEnvelopeConsumer[T], ABC, Generic[T]):
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
    _toolkit: AccountLayerToolkit
    
    def __init__(self, toolkit: Optional[AccountLayerToolkit] | None = None):
        super().__init__(toolkit=toolkit or AccountLayerToolkit())
        
    @property
    def toolkit(self) -> AccountLayerToolkit:
        return cast(AccountLayerToolkit, super().toolkit)
        

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, envelope: RootAccountEnvelope) -> ValidationResult[AccountCarrier]:
        pass