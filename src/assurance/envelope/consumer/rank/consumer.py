# src/assurance/envelope/consumer/rank/consumer.py

"""
Module: assurance.envelope.consumer.rank.consumer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ValidationResult
from assurance import RankLayerToolkit, RootEnvelopeConsumer
from domain import Rank
from transit import RankCarrier, RootRankEnvelope
from util import LoggingLevelRouter

T = TypeVar("T", bound="Rank")


class RankEnvelopeConsumer(RootEnvelopeConsumer[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure an Rank covered by a RootEncounerEnvelope is safe.

    Attributes:
        toolkit: RankLayerToolkit

    Provides:
        -   def execute(envelope: RootRankEnvelope) -> ValidationResult[RankCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    _toolkit: RankLayerToolkit
    
    def __init__(self, toolkit: Optional[RankLayerToolkit] | None = None):
        super().__init__(toolkit=toolkit or RankLayerToolkit())
        
    @property
    def toolkit(self) -> RankLayerToolkit:
        return cast(RankLayerToolkit, super().toolkit)
        

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, envelope: RootRankEnvelope) -> ValidationResult[RankCarrier]:
        pass