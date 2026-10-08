# src/assurance/envelope/consumer/token/king/consumer.py

"""
Module: assurance.envelope.consumer.token.king.consumer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ValidationResult
from assurance import TokenEnvelopeConsumer
from domain import (
    KingReadiness, KingToken, KingTokenBlueprint,
    Token, TokenDeployment
)
from err import (
    KingReadinessNullException, KingTokenEnvelopeConsumerException,
    RootTokenEnvelopeNullException, TokenCarrierEmptyException,
    TokenConsistencyException, TokenEnvelopeRouterException, TokenNullException
)
from transit import KingTokenCarrier, RootTokenEnvelope
from util import LoggingLevelRouter


class KingTokenEnvelopeConsumer(
    TokenEnvelopeConsumer[KingToken]
):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure a KingToken covered by a RootTokenEnvelope is safe.

    Attributes:
        toolkit: TokenValidatorToolkit

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
            envelope: RootTokenEnvelope
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
            target_model=RootTokenEnvelope,
            null_exception=RootTokenEnvelopeNullException(),
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
        safe = cast(RootTokenEnvelope, priming.payload)
        # Handle the case that the envelope wrong envelope was delivered.
        if not safe.for_king_token_consumer:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenEnvelopeConsumerException.MSG,
                    err_code=KingTokenEnvelopeConsumerException.ERR_CODE,
                    ex=TokenEnvelopeRouterException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenEnvelopeRouterException.MSG,
                        err_code=TokenEnvelopeRouterException.ERR_CODE,
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
        # --- START_KING_TOKEN_READINESS_VALIDATION_PROCESS ---#
        # Handle the case that the readiness is flagged.
        readiness_validation = self._toolkit.priming_validator.execute(
            candidate=blueprint.readiness,
            target_model=KingReadiness,
            null_exception=KingReadinessNullException(),
        )
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
        # --- START_THE_THREAT_LEVEL_VALIDATION_PROCESS ---#
        # Handle the case that the readiness is flagged.
        threat_level_validation = self._toolkit.priming_validator.execute(
            candidate=blueprint.threat_level,
            target_model=KingReadiness,
            null_exception=ThreatLevelNullException(),
        )
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
        # --- START_THE_ALERT_VALIDATION_PROCESS ---#
        alert_validation =
        captor = blueprint.captor
        if blueprint.captor is not None:
            # Handle the case that the not-null captor is flagged
            captor_validation = self.toolkit.priming_validator.execute(
                candidate=captor,
                target_model=Token,
                null_exception=TokenNullException(),
            )
            if captor_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    KingTokenEnvelopeConsumerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=KingTokenEnvelopeConsumerException.MSG,
                        err_code=KingTokenEnvelopeConsumerException.ERR_CODE,
                        ex=captor_validation.exception,
                    )
                )
            # Otherwise update captor_placeholder
            captor = cast(Token, captor_validation.payload)
            if safe.team == captor.team:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    KingTokenEnvelopeConsumerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=KingTokenEnvelopeConsumerException.MSG,
                        err_code=KingTokenEnvelopeConsumerException.ERR_CODE,
                        ex=TokenConsistencyException(
                            cls_mthd=method,
                            cls_name=self.__class__.__name__,
                            msg=TokenConsistencyException.MSG,
                            err_code=TokenConsistencyException.ERR_CODE,
                        ),
                    )
                )

        # --- Extract validation payloads. ---#
        readiness = cast(KingReadiness, readiness_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        # The client wants a safe KingToken.
        if safe.prime_extract.reference.has_model:
            model = KingToken(
                id=safe.id,
                team=safe.team,
                footstep=safe.footstep,
                formation=safe.formation,
                home_square=safe.home_square,
            )
            model.captor = captor
            model.readiness = readiness
            if safe.deployment == TokenDeployment.DEPLOYED_TO_HOME_SQUARE:
                model.mark_as_deployed()
            carrier = KingTokenCarrier(model=model)
            return ValidationResult.success(carrier)        
        # Otherwise, the client is a VectorBuilder that needs a Blueprint.
        carrier = KingTokenCarrier(
            blueprint=KingTokenBlueprint(
                id=safe.id,
                team=safe.team,
                footstep=safe.footstep,
                formation=safe.formation,
                home_square=safe.home_square,
                deployment=safe.deployment,
                captor=captor,
                readiness=readiness,
            )
        )
        return ValidationResult.success(carrier)
    
    