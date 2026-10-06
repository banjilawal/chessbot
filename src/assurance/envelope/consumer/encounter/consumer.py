# src/assurance/envelope/consumer/encounter/consumer.py

"""
Module: assurance.envelope.consumer.encounter.consumer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ValidationResult
from assurance import EncounterValidatorToolkit, RootEnvelopeConsumer
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
        toolkit: EncounterValidatorToolkit

    Provides:
        -   def execute(envelope: RootEncounterEnvelope) -> ValidationResult[EncounterCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    _toolkit: EncounterValidatorToolkit
    
    def __init__(self, toolkit: Optional[EncounterValidatorToolkit] | None = None):
        super().__init__(toolkit=toolkit or EncounterValidatorToolkit())
        
    @property
    def toolkit(self) -> EncounterValidatorToolkit:
        return cast(EncounterValidatorToolkit, super().toolkit)
        

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, envelope: RootEncounterEnvelope) -> ValidationResult[EncounterCarrier]:
        pass