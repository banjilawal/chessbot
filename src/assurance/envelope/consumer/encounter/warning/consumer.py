# src/assurance/envelope/consumer/encounter/warning/encounter.py

"""
Module: assurance.envelope.consumer.encounter.warning.encounter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ValidationResult
from assurance import EncounterEnvelopeConsumer
from domain import EncounterWarning, EncounterWarningBlueprint, KingToken, Square
from err import (
    CheckmateCombatantException, EncounterCarrierEmptyException,
    EncounterEnvelopeRouterException, RootEncounterEnvelopeNullException,
    EncounterWarningEnvelopeConsumerException
)
from exchange import SquareValidationRequest
from transit import EncounterWarningCarrier, RootEncounterEnvelope, SquareCarrier
from util import IdFactory, LoggingLevelRouter


class EncounterWarningEnvelopeConsumer(
    EncounterEnvelopeConsumer[EncounterWarning]
):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure an EncounterWarning covered by a RootSquareEncounterEnvelope 
            is safe.

    Attributes:
        toolkit: EncounterValidatorToolkit

    Provides:
        -   def execute(
                    envelope: RootEncounterEnvelope
            ) -> ValidationResult[EncounterWarningCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    
    def __init__(self):
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            envelope: RootEncounterEnvelope
    ) -> ValidationResult[EncounterWarningCarrier]:
        """
        Assure the properties can assemble a safe EncounterWarningCarrier.

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
            ValidationResult[EncounterWarningCarrier]
        Raises:
            EncounterWarningEnvelopeConsumerException
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
                EncounterWarningEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterWarningEnvelopeConsumerException.MSG,
                    err_code=EncounterWarningEnvelopeConsumerException.ERR_CODE,
                    ex=priming.exception
                )
            )
        safe = cast(RootEncounterEnvelope, priming.payload)
        
        if not safe.for_encounter_warning_consumer:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterWarningEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterWarningEnvelopeConsumerException.MSG,
                    err_code=EncounterWarningEnvelopeConsumerException.ERR_CODE,
                    ex=EncounterEnvelopeRouterException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterEnvelopeRouterException.MSG,
                        err_code=EncounterEnvelopeRouterException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the victim is not a CombatantToken   
        if safe.victim_is_combatant:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterWarningEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterWarningEnvelopeConsumerException.MSG,
                    err_code=EncounterWarningEnvelopeConsumerException.ERR_CODE,
                    ex=CheckmateCombatantException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CheckmateCombatantException.MSG,
                        err_code=CheckmateCombatantException.ERR_CODE,
                    )
                )
            )
        carrier = cast(EncounterWarningCarrier, safe.prime_extract.reference)
        blueprint = carrier.extract_blueprint()
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterWarningEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterWarningEnvelopeConsumerException.MSG,
                    err_code=EncounterWarningEnvelopeConsumerException.ERR_CODE,
                    ex=EncounterCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterCarrierEmptyException.MSG,
                        err_code=EncounterCarrierEmptyException.ERR_CODE,
                    )
                )
            )
        danger_zone = blueprint.danger_zone
        if danger_zone is not None:
            danger_zone_validation = self.toolkit.wrapper.square.extract_model(
                request=SquareValidationRequest(
                    item=SquareCarrier(model=danger_zone),
                    id=IdFactory.next_id(class_name="SquareValidationRequest"),
                )
            )
            if danger_zone_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    EncounterWarningEnvelopeConsumerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterWarningEnvelopeConsumerException.MSG,
                        err_code=EncounterWarningEnvelopeConsumerException.ERR_CODE,
                        ex=danger_zone_validation.exception,
                    )
                )
            danger_zone = cast(Square, danger_zone_validation.payload)
            
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = safe.id
        current_safe_square = safe.location
        attacker_reward = safe.attacker_reward
        attacker_maneuver = safe.attacker_maneuver
        warning_recipient = cast(KingToken, safe.victim)
        
        # --- Forward the appropriate work product to the caller. ---#
        if safe.prime_extract.recipient_wants_model:
            carrier = EncounterWarningCarrier(
                model=EncounterWarning(
                    id=id,
                    danger_zone=danger_zone,
                    current_safe_square=current_safe_square,
                    warning_recipient=warning_recipient,
                    attacker_reward=attacker_reward,
                    attacker_maneuver=attacker_maneuver,
                )
            )
            return ValidationResult.success(carrier)
        
        # Otherwise, the client is a EncounterWarningBuilder that needs a Blueprint.
        carrier = EncounterWarningCarrier(
            blueprint=EncounterWarningBlueprint(
                id=id,
                danger_zone=danger_zone,
                current_safe_square=current_safe_square,
                warning_recipient=warning_recipient,
                attacker_reward=attacker_reward,
                attacker_maneuver=attacker_maneuver,
            )
        )
        return ValidationResult.success(carrier)
    
