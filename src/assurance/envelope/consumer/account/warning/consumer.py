# src/assurance/envelope/consumer/account/warning/account.py

"""
Module: assurance.envelope.consumer.account.warning.account
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ValidationResult
from assurance import AccountEnvelopeConsumer
from domain import AccountWarning, AccountWarningBlueprint, KingToken, Square
from err import (
    CheckmateCombatantException, AccountCarrierEmptyException,
    AccountEnvelopeRouterException, RootAccountEnvelopeNullException,
    AccountWarningEnvelopeConsumerException
)
from exchange import SquareValidationRequest
from transit import AccountWarningCarrier, RootAccountEnvelope, SquareCarrier
from util import IdFactory, LoggingLevelRouter


class AccountWarningEnvelopeConsumer(
    AccountEnvelopeConsumer[AccountWarning]
):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure an AccountWarning covered by a RootSquareAccountEnvelope 
            is safe.

    Attributes:
        toolkit: AccountValidatorToolkit

    Provides:
        -   def execute(
                    envelope: RootAccountEnvelope
            ) -> ValidationResult[AccountWarningCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    
    def __init__(self):
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            envelope: RootAccountEnvelope
    ) -> ValidationResult[AccountWarningCarrier]:
        """
        Assure the properties can assemble a safe AccountWarningCarrier.

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
            ValidationResult[AccountWarningCarrier]
        Raises:
            AccountWarningEnvelopeConsumerException
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
                AccountWarningEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountWarningEnvelopeConsumerException.MSG,
                    err_code=AccountWarningEnvelopeConsumerException.ERR_CODE,
                    ex=priming.exception
                )
            )
        safe = cast(RootAccountEnvelope, priming.payload)
        
        if not safe.for_account_warning_consumer:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountWarningEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountWarningEnvelopeConsumerException.MSG,
                    err_code=AccountWarningEnvelopeConsumerException.ERR_CODE,
                    ex=AccountEnvelopeRouterException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountEnvelopeRouterException.MSG,
                        err_code=AccountEnvelopeRouterException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the victim is not a CombatantToken   
        if safe.victim_is_combatant:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountWarningEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountWarningEnvelopeConsumerException.MSG,
                    err_code=AccountWarningEnvelopeConsumerException.ERR_CODE,
                    ex=CheckmateCombatantException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CheckmateCombatantException.MSG,
                        err_code=CheckmateCombatantException.ERR_CODE,
                    )
                )
            )
        carrier = cast(AccountWarningCarrier, safe.prime_extract.reference)
        blueprint = carrier.extract_blueprint()
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AccountWarningEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountWarningEnvelopeConsumerException.MSG,
                    err_code=AccountWarningEnvelopeConsumerException.ERR_CODE,
                    ex=AccountCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountCarrierEmptyException.MSG,
                        err_code=AccountCarrierEmptyException.ERR_CODE,
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
                    AccountWarningEnvelopeConsumerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountWarningEnvelopeConsumerException.MSG,
                        err_code=AccountWarningEnvelopeConsumerException.ERR_CODE,
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
            carrier = AccountWarningCarrier(
                model=AccountWarning(
                    id=id,
                    danger_zone=danger_zone,
                    current_safe_square=current_safe_square,
                    warning_recipient=warning_recipient,
                    attacker_reward=attacker_reward,
                    attacker_maneuver=attacker_maneuver,
                )
            )
            return ValidationResult.success(carrier)
        
        # Otherwise, the client is a AccountWarningBuilder that needs a Blueprint.
        carrier = AccountWarningCarrier(
            blueprint=AccountWarningBlueprint(
                id=id,
                danger_zone=danger_zone,
                current_safe_square=current_safe_square,
                warning_recipient=warning_recipient,
                attacker_reward=attacker_reward,
                attacker_maneuver=attacker_maneuver,
            )
        )
        return ValidationResult.success(carrier)
    
