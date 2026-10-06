# src/assurance/envelope/consumer/encounter/kill/encounter.py

"""
Module: assurance.envelope.consumer.encounter.kill.encounter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ValidationResult
from assurance import EncounterEnvelopeConsumer
from domain import CombatantToken, KillEncounter, KillEncounterBlueprint
from err import (
    EncounterEnvelopeRouterException, EncounterLocationMismatchException,
    KillEncounterEnvelopeConsumerException, NonCombatantKillException,
    RootEncounterEnvelopeNullException
)
from transit import KillEncounterCarrier, RootEncounterEnvelope
from util import LoggingLevelRouter


class KillEncounterEnvelopeConsumer(EncounterEnvelopeConsumer[KillEncounter]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure a KillEncounter covered by a RootSquareEncounterEnvelope is safe.

    Attributes:
        toolkit: EncounterValidatorToolkit

    Provides:
        -   def execute(envelope: RootEncounterEnvelope) -> ValidationResult[EncounterCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    
    def __init__(self):
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            envelope: RootEncounterEnvelope
    ) -> ValidationResult[KillEncounterCarrier]:
        """
        Assure the properties can assemble a safe KillEncounterCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the
                following occur.
                    -   The consumer cannot be primed.
                    -   The envelope is not meant for the consumer. 
                    -   the victim is a KingToken.
                    -   The location is not consistent.
            2.  Otherwise, Send a Carrier with the correct type of payload in
                the success result.
        Args:
             envelope: RootEncounterEnvelope
        Returns:
            ValidationResult[KillEncounterCarrier]
        Raises:
            KillEncounterEnvelopeConsumerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the property table is null or the wrong type.
        priming = self._toolkit.priming_validator.execute(
            candidate=envelope,
            target_model=RootEncounterEnvelope,
            null_exception=RootEncounterEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillEncounterEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterEnvelopeConsumerException.MSG,
                    err_code=KillEncounterEnvelopeConsumerException.ERR_CODE,
                    ex=priming.exception
                )
            )
        safe = cast(RootEncounterEnvelope, priming.payload)
        
        if not safe.for_kill_encounter_consumer:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillEncounterEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterEnvelopeConsumerException.MSG,
                    err_code=KillEncounterEnvelopeConsumerException.ERR_CODE,
                    ex=EncounterEnvelopeRouterException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterEnvelopeRouterException.MSG,
                        err_code=EncounterEnvelopeRouterException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the victim is not a CombatantToken   
        if safe.participants.victim_is_king:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillEncounterEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterEnvelopeConsumerException.MSG,
                    err_code=KillEncounterEnvelopeConsumerException.ERR_CODE,
                    ex=NonCombatantKillException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=NonCombatantKillException.MSG,
                        err_code=NonCombatantKillException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the kill_location and maneuver.destination are mismatched.
        if safe.location != safe.attacker_maneuver.destination:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillEncounterEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterEnvelopeConsumerException.MSG,
                    err_code=KillEncounterEnvelopeConsumerException.ERR_CODE,
                    ex=EncounterLocationMismatchException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterLocationMismatchException.MSG,
                        err_code=EncounterLocationMismatchException.ERR_CODE,
                    )
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = safe.id
        location = safe.location
        attacker_reward = safe.attacker_reward
        attacker_maneuver = safe.attacker_maneuver
        victim = cast(CombatantToken, safe.participants.victim)
        
        # --- Forward the appropriate work product to the caller. ---#
        if safe.prime_extract.recipient_wants_model:
            carrier = KillEncounterCarrier(
                model=KillEncounter(
                    id=id,
                    victim=victim,
                    location=location,
                    attacker_reward=attacker_reward,
                    attacker_maneuver=attacker_maneuver,
                )
            )
            return ValidationResult.success(carrier)
        
        # Otherwise, the client is a KillEncounterBuilder that needs a Blueprint.
        carrier = KillEncounterCarrier(
            blueprint=KillEncounterBlueprint(
                id=id,
                victim=victim,
                location=location,
                attacker_reward=attacker_reward,
                attacker_maneuver=attacker_maneuver,
            )
        )
        return ValidationResult.success(carrier)
    
