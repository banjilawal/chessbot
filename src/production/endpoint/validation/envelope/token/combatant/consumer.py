# src/production/endpoint/envelope/token/combatant/consumer.py

"""
Module: production.endpoint.envelope.token.combatant.consumer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ValidationResult
from domain import CombatantReadiness, CombatantToken, CombatantTokenBlueprint, Token, TokenPrimeExtract
from err import (
    CombatantReadinessNullException, CombatantTokenEnvelopeConsumerException, TokenEnvelopeNullException,
    TokenCarrierEmptyException,
    TokenConsistencyException, TokenNullException, TokenValidationRouterException
)
from production import TokenEnvelopeConsumer
from transit import CombatantTokenCarrier, TokenEnvelope
from util import LoggingLevelRouter


class CombatantTokenEnvelopeConsumer(
    TokenEnvelopeConsumer[CombatantToken]
):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure a CombatantToken covered by a RootTokenEnvelope is safe.

    Attributes:
        toolkit: TokenLayerToolkit

    Provides:
        -   def execute(
                    envelope: RootTokenEnvelope
            ) -> ValidationResult[CombatantTokenCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    
    def __init__(self):
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            envelope: TokenEnvelope,
    ) -> ValidationResult[CombatantTokenCarrier]:
        """
        Assure the properties can assemble a safe CombatantTokenCarrier.

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
             envelope: RootTokenEnvelope
        Returns:
            ValidationResult[CombatantTokenCarrier]
        Raises:
            CombatantTokenEnvelopeConsumerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- INITIATE_THE_VALIDATION_PROCESS ---#
        priming = self.toolkit.priming_validator.execute(
            candidate=envelope,
            target_model=TokenEnvelope,
            null_exception=TokenEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CombatantTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenEnvelopeConsumerException.MSG,
                    err_code=CombatantTokenEnvelopeConsumerException.ERR_CODE,
                    ex=priming.exception
                )
            )
        safe = cast(TokenEnvelope, priming.payload)
        # Handle the case that the envelope wrong envelope was delivered.
        if not safe.for_combatant_token_consumer:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CombatantTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenEnvelopeConsumerException.MSG,
                    err_code=CombatantTokenEnvelopeConsumerException.ERR_CODE,
                    ex=TokenValidationRouterException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenValidationRouterException.MSG,
                        err_code=TokenValidationRouterException.ERR_CODE,
                    )
                )
            )
        # --- EXTRACT_THE_BLUEPRINT_THE_VALIDATOR_NEEDS ---#
        extract = safe.prime_extract
        reference = cast(CombatantTokenCarrier, extract.reference)
        fingerprint = reference.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if fingerprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CombatantTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenEnvelopeConsumerException.MSG,
                    err_code=CombatantTokenEnvelopeConsumerException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- START_COMBATANT_TOKEN_READINESS_VALIDATION_PROCESS ---#
        
        # Handle the case that the readiness is flagged.
        readiness_validation = self._toolkit.priming_validator.execute(
            candidate=fingerprint.readiness,
            target_model=CombatantReadiness,
            null_exception=CombatantReadinessNullException(),
        )
        if readiness_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CombatantTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenEnvelopeConsumerException.MSG,
                    err_code=CombatantTokenEnvelopeConsumerException.ERR_CODE,
                    ex=readiness_validation.exception,
                )
            )
        # --- START_CAPTOR_VALIDATION_PROCESS ---#
        
        captor = fingerprint.captor
        if captor is not None:
            # Handle the case that the not-null captor is flagged
            captor_validation = self.toolkit.priming_validator.execute(
                candidate=captor,
                target_model=Token,
                null_exception=TokenNullException(),
            )
            if captor_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    CombatantTokenEnvelopeConsumerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CombatantTokenEnvelopeConsumerException.MSG,
                        err_code=CombatantTokenEnvelopeConsumerException.ERR_CODE,
                        ex=captor_validation.exception,
                    )
                )
            # Otherwise update captor_placeholder
            captor = cast(Token, captor_validation.payload)
            if safe.team == captor.team:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    CombatantTokenEnvelopeConsumerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CombatantTokenEnvelopeConsumerException.MSG,
                        err_code=CombatantTokenEnvelopeConsumerException.ERR_CODE,
                        ex=TokenConsistencyException(
                            cls_mthd=method,
                            cls_name=self.__class__.__name__,
                            msg=TokenConsistencyException.MSG,
                            err_code=TokenConsistencyException.ERR_CODE,
                        ),
                    )
                )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        readiness = cast(CombatantReadiness, readiness_validation.payload)
        
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        
        # The client wants a safe CombatantToken.
        if extract.recipient_wants_model:
            model = CombatantToken(
                id=safe.id,
                team=safe.team,
                footstep=safe.footstep,
                formation=safe.formation,
                home_square=safe.home_square,
            )
            # Update the mutatable fields.
            model.captor = captor
            model.readiness = readiness
            model.deployment = safe.deployment
            payload = CombatantTokenCarrier(model=model)
            return ValidationResult.success(payload)
        # Otherwise, the client is a TokenBuilder that needs a Blueprint.
        blueprint = CombatantTokenBlueprint(
            id=safe.id,
            team=safe.team,
            footstep=safe.footstep,
            formation=safe.formation,
            home_square=safe.home_square,
            deployment=safe.deployment,
            captor=captor,
            readiness=readiness,
        )
        blueprint.mark_as_validated()
        payload = CombatantTokenCarrier(blueprint=blueprint)
        return ValidationResult.success(payload)
    
    