# src/assurance/envelope/consumer/account/human/account.py

"""
Module: assurance.envelope.consumer.account.human.account
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, cast

from artifcat import ValidationResult
from assurance import AccountEnvelopeConsumer
from domain import HumanAccount, HumanAccountBlueprint
from err import (
    AccountCarrierEmptyException, AccountValidationRouterException, HumanAccountEnvelopeConsumerException,
    RootAccountEnvelopeNullException
)

from transit import HumanAccountCarrier, RootAccountEnvelope
from util import LoggingLevelRouter


class HumanAccountEnvelopeConsumer(
    AccountEnvelopeConsumer[HumanAccount]
):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure a HumanAccount covered by a RootSquareAccountEnvelope is safe.

    Attributes:
        toolkit: AccountValidatorToolkit

    Provides:
        -   def execute(
                    envelope: RootAccountEnvelope
            ) -> ValidationResult[HumanAccountCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    
    def __init__(self):
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            envelope: RootAccountEnvelope
    ) -> ValidationResult[HumanAccountCarrier]:
        """
        Assure the properties can assemble a safe HumanAccountCarrier.

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
            ValidationResult[HumanAccountCarrier]
        Raises:
            HumanAccountEnvelopeConsumerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the envelope cannot be primed.
        priming = self._toolkit.priming_validator.execute(
            candidate=envelope,
            target_model=RootAccountEnvelope,
            null_exception=RootAccountEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HumanAccountEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanAccountEnvelopeConsumerException.MSG,
                    err_code=HumanAccountEnvelopeConsumerException.ERR_CODE,
                    ex=priming.exception
                )
            )
        safe = cast(RootAccountEnvelope, priming.payload)
        if not safe.for_human_account_consumer:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HumanAccountEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanAccountEnvelopeConsumerException.MSG,
                    err_code=HumanAccountEnvelopeConsumerException.ERR_CODE,
                    ex=AccountValidationRouterException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountValidationRouterException.MSG,
                        err_code=AccountValidationRouterException.ERR_CODE,
                    )
                )
            )
        prime_extract = safe.prime_extract
        reference = cast(HumanAccountCarrier, prime_extract.reference)
        if reference.extract_blueprint() is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HumanAccountEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanAccountEnvelopeConsumerException.MSG,
                    err_code=HumanAccountEnvelopeConsumerException.ERR_CODE,
                    ex=AccountCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AccountCarrierEmptyException.MSG,
                        err_code=AccountCarrierEmptyException.ERR_CODE,
                    )
                )
            )
        fingerprint = cast(HumanAccountBlueprint, reference.extract_blueprint())
        safe_names: Dict[str, str] = {}
        for key in fingerprint.names_dict.keys():
            name_validation = self.toolkit.identity_service.validate_name(
                candidate=fingerprint.names_dict[key]
            )
            if name_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    HumanAccountEnvelopeConsumerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=HumanAccountEnvelopeConsumerException.MSG,
                        err_code=HumanAccountEnvelopeConsumerException.ERR_CODE,
                        ex=name_validation.exception,
                    )
                )
            safe_names[key] = cast(str, name_validation.payload)
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        id = safe.id
        firstname = safe_names["firstname"]
        lastname = safe_names["lastname"]
        
        # --- Forward the appropriate work product to the caller. ---#
        if safe.prime_extract.recipient_wants_model:
            model = HumanAccount(
                id=id,
                firstname=firstname,
                lastname=lastname,
            )
            carrier = HumanAccountCarrier(model=model)
            return ValidationResult.success(carrier)
        # Otherwise, the client is a HumanAccountBuilder that needs a Blueprint.
        blueprint = HumanAccountBlueprint(
            id=id,
            firstname=firstname,
            lastname=lastname,
        )
        carrier = HumanAccountCarrier(blueprint=blueprint)
        return ValidationResult.success(carrier)
    
