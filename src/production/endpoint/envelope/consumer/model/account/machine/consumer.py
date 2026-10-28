# src/production/endpoint/envelope/consumer/model/account/machine/consumer.py

"""
Module: production.endpoint.envelope.consumer.model.account.machine.consumer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ValidationResult
from domain import MachineAccount, MachineAccountBlueprint
from err import (
    AccountCarrierEmptyException, AccountValidationRouterException, MachineAccountEnvelopeConsumerException,
    AccountEnvelopeNullException
)
from production import AccountEnvelopeConsumer
from transit import MachineAccountCarrier, AccountEnvelope
from util import LoggingLevelRouter


class MachineAccountEnvelopeConsumer(
    AccountEnvelopeConsumer[MachineAccount]
):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure a MachineAccount covered by a RootSquareAccountEnvelope is safe.

    Attributes:
        toolkit: AccountLayerToolkit

    Provides:
        -   def execute(
                    envelope: RootAccountEnvelope
            ) -> ValidationResult[MachineAccountCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    
    def __init__(self):
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            envelope: AccountEnvelope
    ) -> ValidationResult[MachineAccountCarrier]:
        """
        Assure the properties can assemble a safe MachineAccountCarrier.

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
            ValidationResult[MachineAccountCarrier]
        Raises:
            MachineAccountEnvelopeConsumerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the envelope cannot be primed.
        priming = self._toolkit.priming_validator.execute(
            candidate=envelope,
            target_model=AccountEnvelope,
            null_exception=AccountEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                MachineAccountEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=MachineAccountEnvelopeConsumerException.MSG,
                    err_code=MachineAccountEnvelopeConsumerException.ERR_CODE,
                    ex=priming.exception
                )
            )
        safe = cast(AccountEnvelope, priming.payload)
        if not safe.for_machine_account_consumer:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                MachineAccountEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=MachineAccountEnvelopeConsumerException.MSG,
                    err_code=MachineAccountEnvelopeConsumerException.ERR_CODE,
                    ex=AccountValidationRouterException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountValidationRouterException.MSG,
                        err_code=AccountValidationRouterException.ERR_CODE,
                    )
                )
            )
        extract = safe.prime_extract
        reference = cast(MachineAccountCarrier, extract.reference)
        fingerprint = reference.extract_blueprint()
        if fingerprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                MachineAccountEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=MachineAccountEnvelopeConsumerException.MSG,
                    err_code=MachineAccountEnvelopeConsumerException.ERR_CODE,
                    ex=AccountCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountCarrierEmptyException.MSG,
                        err_code=AccountCarrierEmptyException.ERR_CODE,
                    )
                )
            )
        name_validation = self.toolkit.identity_service.validate_name(
            candidate=fingerprint.name
        )
        if name_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                MachineAccountEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=MachineAccountEnvelopeConsumerException.MSG,
                    err_code=MachineAccountEnvelopeConsumerException.ERR_CODE,
                    ex=name_validation.exception,
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = safe.id
        name = cast(str, name_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        if safe.prime_extract.recipient_wants_model:
            model = MachineAccount(id=id, name=name)
            payload = MachineAccountCarrier(model=model)
            return ValidationResult.success(payload)
        # Otherwise, the client is a MachineAccountBuilder that needs a Blueprint.
        blueprint = MachineAccountBlueprint(id=id, name=name)
        blueprint.mark_as_validated()
        payload = MachineAccountCarrier(blueprint=blueprint)
        return ValidationResult.success(payload)
    
