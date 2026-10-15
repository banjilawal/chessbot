# src/assurance/envelope/consumer/account/kill/account.py

"""
Module: assurance.envelope.consumer.account.kill.account
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ValidationResult
from assurance import AccountEnvelopeConsumer
from domain import CombatantToken, KillAccount, KillAccountBlueprint
from err import (
    AccountEnvelopeRouterException, AccountLocationMismatchException,
    KillAccountEnvelopeConsumerException, KillKingException,
    RootAccountEnvelopeNullException
)
from transit import KillAccountCarrier, RootAccountEnvelope
from util import LoggingLevelRouter


class KillAccountEnvelopeConsumer(
    AccountEnvelopeConsumer[KillAccount]
):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure a KillAccount covered by a RootSquareAccountEnvelope is safe.

    Attributes:
        toolkit: AccountValidatorToolkit

    Provides:
        -   def execute(envelope: RootAccountEnvelope) -> ValidationResult[AccountCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    
    def __init__(self):
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            envelope: RootAccountEnvelope
    ) -> ValidationResult[KillAccountCarrier]:
        """
        Assure the properties can assemble a safe KillAccountCarrier.

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
             envelope: RootAccountEnvelope
        Returns:
            ValidationResult[KillAccountCarrier]
        Raises:
            KillAccountEnvelopeConsumerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the property table is null or the wrong type.
        priming = self._toolkit.priming_validator.execute(
            candidate=envelope,
            target_model=RootAccountEnvelope,
            null_exception=RootAccountEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillAccountEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillAccountEnvelopeConsumerException.MSG,
                    err_code=KillAccountEnvelopeConsumerException.ERR_CODE,
                    ex=priming.exception
                )
            )
        safe = cast(RootAccountEnvelope, priming.payload)
        
        if not safe.for_kill_account_consumer:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillAccountEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillAccountEnvelopeConsumerException.MSG,
                    err_code=KillAccountEnvelopeConsumerException.ERR_CODE,
                    ex=AccountEnvelopeRouterException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountEnvelopeRouterException.MSG,
                        err_code=AccountEnvelopeRouterException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the victim is not a CombatantToken   
        if safe.victim_is_king:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillAccountEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillAccountEnvelopeConsumerException.MSG,
                    err_code=KillAccountEnvelopeConsumerException.ERR_CODE,
                    ex=KillKingException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=KillKingException.MSG,
                        err_code=KillKingException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the kill_location and maneuver.destination are mismatched.
        if safe.location != safe.attacker_maneuver.destination:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillAccountEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillAccountEnvelopeConsumerException.MSG,
                    err_code=KillAccountEnvelopeConsumerException.ERR_CODE,
                    ex=AccountLocationMismatchException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountLocationMismatchException.MSG,
                        err_code=AccountLocationMismatchException.ERR_CODE,
                    )
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = safe.id
        location = safe.location
        attacker_reward = safe.attacker_reward
        attacker_maneuver = safe.attacker_maneuver
        victim = cast(CombatantToken, safe.victim)
        
        # --- Forward the appropriate work product to the caller. ---#
        if safe.prime_extract.recipient_wants_model:
            carrier = KillAccountCarrier(
                model=KillAccount(
                    id=id,
                    victim=victim,
                    location=location,
                    attacker_reward=attacker_reward,
                    attacker_maneuver=attacker_maneuver,
                )
            )
            return ValidationResult.success(carrier)
        # Otherwise, the client is a KillAccountBuilder that needs a Blueprint.
        carrier = KillAccountCarrier(
            blueprint=KillAccountBlueprint(
                id=id,
                victim=victim,
                location=location,
                attacker_reward=attacker_reward,
                attacker_maneuver=attacker_maneuver,
            )
        )
        return ValidationResult.success(carrier)
    
