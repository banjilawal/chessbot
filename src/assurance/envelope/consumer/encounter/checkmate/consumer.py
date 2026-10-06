# src/assurance/envelope/consumer/encounter/checkmate/encounter.py

"""
Module: assurance.envelope.consumer.encounter.checkmate.encounter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ValidationResult
from assurance import EncounterEnvelopeConsumer
from domain import CheckmateEncounter, CheckmateEncounterBlueprint, KingToken
from err import (
    CheckmateCombatantException, EncounterEnvelopeRouterException,
    CheckmateEncounterEnvelopeConsumerException,
    RootEncounterEnvelopeNullException
)
from transit import CheckmateEncounterCarrier, RootEncounterEnvelope
from util import LoggingLevelRouter


class CheckmateEncounterEnvelopeConsumer(
    EncounterEnvelopeConsumer[CheckmateEncounter]
):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure a CheckmateEncounter covered by a RootSquareEncounterEnvelope is safe.

    Attributes:
        toolkit: EncounterValidatorToolkit

    Provides:
        -   def execute(
                    envelope: RootEncounterEnvelope
            ) -> ValidationResult[CheckmateEncounterCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    
    def __init__(self):
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            envelope: RootEncounterEnvelope
    ) -> ValidationResult[CheckmateEncounterCarrier]:
        """
        Assure the properties can assemble a safe CheckmateEncounterCarrier.

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
            ValidationResult[CheckmateEncounterCarrier]
        Raises:
            CheckmateEncounterEnvelopeConsumerException
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
                CheckmateEncounterEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CheckmateEncounterEnvelopeConsumerException.MSG,
                    err_code=CheckmateEncounterEnvelopeConsumerException.ERR_CODE,
                    ex=priming.exception
                )
            )
        safe = cast(RootEncounterEnvelope, priming.payload)
        
        if not safe.for_checkmate_encounter_consumer:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CheckmateEncounterEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CheckmateEncounterEnvelopeConsumerException.MSG,
                    err_code=CheckmateEncounterEnvelopeConsumerException.ERR_CODE,
                    ex=EncounterEnvelopeRouterException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterEnvelopeRouterException.MSG,
                        err_code=EncounterEnvelopeRouterException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the victim is not a CombatantToken   
        if safe.participants.victim_is_combatant:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CheckmateEncounterEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CheckmateEncounterEnvelopeConsumerException.MSG,
                    err_code=CheckmateEncounterEnvelopeConsumerException.ERR_CODE,
                    ex=CheckmateCombatantException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CheckmateCombatantException.MSG,
                        err_code=CheckmateCombatantException.ERR_CODE,
                    )
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = safe.id
        location = safe.location
        attacker_reward = safe.attacker_reward
        attacker_maneuver = safe.attacker_maneuver
        victim = cast(KingToken, safe.participants.victim)
        
        # --- Forward the appropriate work product to the caller. ---#
        if safe.prime_extract.recipient_wants_model:
            carrier = CheckmateEncounterCarrier(
                model=CheckmateEncounter(
                    id=id,
                    victim=victim,
                    location=location,
                    attacker_reward=attacker_reward,
                    attacker_maneuver=attacker_maneuver,
                )
            )
            return ValidationResult.success(carrier)
        
        # Otherwise, the client is a CheckmateEncounterBuilder that needs a Blueprint.
        carrier = CheckmateEncounterCarrier(
            blueprint=CheckmateEncounterBlueprint(
                id=id,
                victim=victim,
                location=location,
                attacker_reward=attacker_reward,
                attacker_maneuver=attacker_maneuver,
            )
        )
        return ValidationResult.success(carrier)
    
