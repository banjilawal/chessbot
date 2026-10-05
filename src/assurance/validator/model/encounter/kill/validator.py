# src/assurance/validator/model/encounter/kill/exception.py

"""
Module: assurance.validator.model.encounter.kill.exception
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from artifcat import ValidationResult
from assurance import EncounterValidatorToolkit
from domain import CombatantToken, KillEncounter, KillEncounterBlueprint
from err import (
    EncounterConsistencyException, KillEncounterNullException,
    KillEncounterValidatorException
)
from transit import KillEncounterCarrier, RootEncounterEnvelope

from util import LoggingLevelRouter


class KillEncounterValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a KillEncounterCarrier is safe to use.

    Attributes:
        toolkit: EncounterValidatorToolkit
        enemy_validator: EncounterEnemyValidator

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[KillEncounterCarrier]:

    Super Class:
    """
    _toolkit: EncounterValidatorToolkit
    
    def __init__(
            self,
            toolkit: Optional[EncounterValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[EncounterValidatorToolkit]
        """
        self._toolkit = toolkit or EncounterValidatorToolkit()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: RootEncounterEnvelope,
    ) -> ValidationResult[KillEncounterCarrier]:
        """
        Assure the properties can assemble a safe KillEncounterCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                fields are flagged.
                    -   captor
                    -   rank
                    -   promotion_state
                    -   combatant_readiness
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate: RootEncounterEnvelope
        Returns:
            ValidationResult[KillEncounterCarrier]
        Raises:
            KillEncounterValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the property table is null or the wrong type.
        priming = self._toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=Type[RootEncounterEnvelope],
            null_exception=RootEncounterEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterValidatorException.MSG,
                    err_code=KillEncounterValidatorException.ERR_CODE,
                    ex=priming.exception
                )
            )
        envelope = cast(RootEncounterEnvelope, candidate)
        
        if envelope.participants.victim_is_king:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterValidatorException.MSG,
                    err_code=KillEncounterValidatorException.ERR_CODE,
                    ex=KillEnemyKingException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=KillEnemyKingException.MSG,
                        err_code=KillEnemyKingException.ERR_CODE,
                    )
                )
            )
        
        participants = envelope.participants
        if (
                participants.is_not_consistent or
                (not participants.attacker == envelope.attacker_maneuver.traveler)
        ):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterValidatorException.MSG,
                    err_code=KillEncounterValidatorException.ERR_CODE,
                    ex=EncounterConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterConsistencyException.MSG,
                        err_code=EncounterConsistencyException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the kill_location and maneuver.destination are mismatched.
        if envelope.location != envelope.attacker_maneuver.destination:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterValidatorException.MSG,
                    err_code=KillEncounterValidatorException.ERR_CODE,
                    ex=EncounterConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterConsistencyException.MSG,
                        err_code=EncounterConsistencyException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the envelope does not have a KillEncounterCarrier
        carrier_validation = self._toolkit.priming_validator.execute(
            candidate=envelope.prime_extract.carrier,
            target_model=Type[KillEncounterCarrier],
            null_exception=KillEncounterNullException(),
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterValidatorException.MSG,
                    err_code=KillEncounterValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Extract validation payloads. ---#
        id = envelope.id
        location = envelope.location
        attacker_reward = envelope.attacker_reward
        attacker_maneuver = envelope.attacker_maneuver
        victim = cast(CombatantToken, participants.victim)
        carrier = cast(KillEncounterCarrier, carrier_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        # The client wants a safe KillEncounter.
        if carrier.has_model:
            payload = KillEncounter(
                id=id,
                victim=victim,
                location=location,
                attacker_reward=attacker_reward,
                attacker_maneuver=attacker_maneuver,
            )
            return ValidationResult.success(KillEncounterCarrier(model=payload))
        
        # Otherwise, the client is a VectorBuilder that needs a Blueprint.
        payload = KillEncounterBlueprint(
            id=id,
            victim=victim,
            location=location,
            attacker_reward=attacker_reward,
            attacker_maneuver=attacker_maneuver,
        )
        return ValidationResult.success(KillEncounterCarrier(blueprint=payload))