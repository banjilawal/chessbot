# src/production/endpoint/envelope/consumer/model/encounter/consumer.py

"""
Module: production.endpoint.envelope.consumer.model.encounter.consumer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ValidationResult
from assurance import EncounterLayerToolkit, RootEnvelopeConsumer
from domain import Encounter
from transit import EncounterCarrier, RootEncounterEnvelope
from util import LoggingLevelRouter

T = TypeVar("T", bound="Encounter")


class EncounterEnvelopeConsumer(RootEnvelopeConsumer[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure an Encounter covered by a RootEncounerEnvelope is safe.

    Attributes:
        toolkit: EncounterLayerToolkit

    Provides:
        -   def execute(envelope: RootEncounterEnvelope) -> ValidationResult[EncounterCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    _toolkit: EncounterLayerToolkit
    
    def __init__(self, toolkit: Optional[EncounterLayerToolkit] | None = None):
        super().__init__(toolkit=toolkit or EncounterLayerToolkit())
        
    @property
    def toolkit(self) -> EncounterLayerToolkit:
        return cast(EncounterLayerToolkit, super().toolkit)
        

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, envelope: RootEncounterEnvelope) -> ValidationResult[EncounterCarrier]:
        pass