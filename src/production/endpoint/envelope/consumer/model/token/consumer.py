# src/production/endpoint/envelope/consumer/model/token/consumer.py

"""
Module: production.endpoint.envelope.consumer.model.token.consumer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ValidationResult
from assurance import TokenLayerToolkit
from domain import Token
from production import ModelEnvelopeConsumer
from transit import TokenCarrier, TokenEnvelope
from util import LoggingLevelRouter

T = TypeVar("T", bound="Token")


class TokenEnvelopeConsumer(ModelEnvelopeConsumer[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure an Token covered by a RootEncounerEnvelope is safe.

    Attributes:
        toolkit: TokenLayerToolkit

    Provides:
        -   def execute(envelope: RootTokenEnvelope) -> ValidationResult[TokenCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    _toolkit: TokenLayerToolkit
    
    def __init__(self, toolkit: Optional[TokenLayerToolkit] | None = None):
        """
        Args:
            toolkit: Optional[TokenLayerToolkit]
        """
        super().__init__(toolkit=toolkit or TokenLayerToolkit())
        
    @property
    def toolkit(self) -> TokenLayerToolkit:
        return cast(TokenLayerToolkit, super().toolkit)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, envelope: TokenEnvelope) -> ValidationResult[TokenCarrier]:
        pass