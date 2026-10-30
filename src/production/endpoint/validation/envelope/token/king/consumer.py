# src/production/endpoint/envelope/token/king/consumer.py

"""
Module: production.endpoint.envelope.token.king.consumer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ValidationResult
from assurance import TokenEnvelopeConsumer
from domain import (
    Alert, KingReadiness, KingToken, KingTokenBlueprint, Square, ThreatLevel
)
from err import (
    KingReadinessNullException, KingTokenEnvelopeConsumerException,
    TokenEnvelopeNullException, ThreatLevelNullException, TokenCarrierEmptyException,
    TokenValidationRouterException
)
from exchange import AlertValidationRequest, SquareValidationRequest
from transit import AlertCarrier, KingTokenCarrier, TokenEnvelope, SquareCarrier
from util import IdFactory, LoggingLevelRouter


class KingTokenEnvelopeConsumer(
    TokenEnvelopeConsumer[KingToken]
):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure a KingToken covered by a RootTokenEnvelope is safe.

    Attributes:
        toolkit: TokenLayerToolkit

    Provides:
        -   def execute(
                    envelope: RootTokenEnvelope
            ) -> ValidationResult[KingTokenCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    
    def __init__(self):
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            envelope: TokenEnvelope
    ) -> ValidationResult[KingTokenCarrier]:
        """
        Assure the properties can assemble a safe KingTokenCarrier.

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
            ValidationResult[KingTokenCarrier]
        Raises:
            KingTokenEnvelopeConsumerException
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
                KingTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenEnvelopeConsumerException.MSG,
                    err_code=KingTokenEnvelopeConsumerException.ERR_CODE,
                    ex=priming.exception
                )
            )
        safe = cast(TokenEnvelope, priming.payload)
        # Handle the case that the envelope wrong envelope was delivered.
        if not safe.for_king_token_consumer:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenEnvelopeConsumerException.MSG,
                    err_code=KingTokenEnvelopeConsumerException.ERR_CODE,
                    ex=TokenValidationRouterException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenValidationRouterException.MSG,
                        err_code=TokenValidationRouterException.ERR_CODE,
                    )
                )
            )
        # --- EXTRACT_THE_BLUEPRINT_THE_VALIDATOR_NEEDS ---#
        reference = cast(KingTokenCarrier, safe.prime_extract.reference)
        blueprint = reference.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenEnvelopeConsumerException.MSG,
                    err_code=KingTokenEnvelopeConsumerException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- START_THE_THREAT_LEVEL_VALIDATION_PROCESS ---#
        threat_level_validation = self._toolkit.priming_validator.execute(
            candidate=blueprint.threat_level,
            target_model=ThreatLevel,
            null_exception=ThreatLevelNullException(),
        )
        # Handle the case that the threat_level is flagged.
        if threat_level_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenEnvelopeConsumerException.MSG,
                    err_code=KingTokenEnvelopeConsumerException.ERR_CODE,
                    ex=threat_level_validation.exception,
                )
            )
        # --- START_KING_TOKEN_READINESS_VALIDATION_PROCESS ---#
        readiness_validation = self._toolkit.priming_validator.execute(
            candidate=blueprint.readiness,
            target_model=KingReadiness,
            null_exception=KingReadinessNullException(),
        )
        # Handle the case that the readiness is flagged.
        if readiness_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenEnvelopeConsumerException.MSG,
                    err_code=KingTokenEnvelopeConsumerException.ERR_CODE,
                    ex=readiness_validation.exception,
                )
            )
        # --- START_THE_ALERT_VALIDATION_PROCESS ---#
        alert_validation = self.toolkit.dependency.alert.extract_model(
            request=AlertValidationRequest(
                item=AlertCarrier(model=blueprint.alert),
                id=IdFactory.next_id(class_name="AlertValidationRequest")
            )
        )
        # Handle the case that the readiness is flagged.
        if alert_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenEnvelopeConsumerException.MSG,
                    err_code=KingTokenEnvelopeConsumerException.ERR_CODE,
                    ex=alert_validation.exception,
                )
            )
        # --- START_THE_POTENTAIL_DESTINATION_VALIDATION_PROCESS ---#
        potential_destination = blueprint.potential_destination
        if potential_destination is not None:
            potential_destination_validation = self.toolkit.dependency.square.extract_model(
                request=SquareValidationRequest(
                    item=SquareCarrier(model=blueprint.potential_destination),
                    id=IdFactory.next_id(class_name="SquareValidationRequest")
                )
            )
            # Handle the case that the readiness is flagged.
            if potential_destination_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    KingTokenEnvelopeConsumerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=KingTokenEnvelopeConsumerException.MSG,
                        err_code=KingTokenEnvelopeConsumerException.ERR_CODE,
                        ex=potential_destination_validation.exception,
                    )
                )
            potential_destination = cast(Square, potential_destination_validation.payload)
        # --- Extract validation payloads. ---#
        alert = cast(Alert, alert_validation.payload)
        readiness = cast(KingReadiness, readiness_validation.payload)
        threat_level = cast(ThreatLevel, threat_level_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        # The client wants a safe KingToken.
        if safe.prime_extract.reference.has_model:
            model = KingToken(
                id=safe.id,
                team=safe.team,
                footstep=safe.footstep,
                formation=safe.formation,
                home_square=safe.home_square,
                alert=alert,
            )
            model.readiness = readiness
            model.threat_level = threat_level
            model.deployment = safe.deployment
            model.potential_destination = potential_destination
            carrier = KingTokenCarrier(model=model)
            return ValidationResult.success(carrier)        
        # Otherwise, the client is a TokenBuilder that needs a Blueprint.
        carrier = KingTokenCarrier(
            blueprint=KingTokenBlueprint(
                id=safe.id,
                team=safe.team,
                footstep=safe.footstep,
                formation=safe.formation,
                home_square=safe.home_square,
                deployment=safe.deployment,
                potential_destination=potential_destination,
                threat_level=threat_level,
                readiness=readiness,
                alert=alert,
            )
        )
        return ValidationResult.success(carrier)
    
    