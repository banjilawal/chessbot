# src/assurance/envelope/consumer/token/consumer.py

"""
Module: assurance.envelope.consumer.token.consumer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ValidationResult
from assurance import TokenEnvelopeConsumer
from domain import (
    CombatantReadiness, CombatantToken, CombatantTokenBlueprint,
    Token, TokenDeployment
)
from err import (
    CombatantReadinessNullException, CombatantTokenEnvelopeConsumerException,
    RootTokenEnvelopeNullException, TokenCarrierEmptyException,
    TokenConsistencyException, TokenEnvelopeRouterException, TokenNullException
)
from transit import CombatantTokenCarrier, RootTokenEnvelope
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
        toolkit: TokenValidatorToolkit

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
            envelope: RootTokenEnvelope
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
        
        # Handle the case that the property table is null or the wrong type.
        priming = self._toolkit.priming_validator.execute(
            candidate=envelope,
            target_model=RootTokenEnvelope,
            null_exception=RootTokenEnvelopeNullException(),
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
        safe = cast(RootTokenEnvelope, priming.payload)
        
        if not safe.for_combatant_token_consumer:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CombatantTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenEnvelopeConsumerException.MSG,
                    err_code=CombatantTokenEnvelopeConsumerException.ERR_CODE,
                    ex=TokenEnvelopeRouterException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenEnvelopeRouterException.MSG,
                        err_code=TokenEnvelopeRouterException.ERR_CODE,
                    )
                )
            )
        reference = cast(CombatantTokenCarrier, safe.prime_extract.reference)
        blueprint = reference.extract_blueprint()
        
        if blueprint is None:
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
            candidate=blueprint.readiness,
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

        # --- Extract validation payloads. ---#
        readiness = cast(CombatantReadiness, readiness_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        # The client wants a safe CombatantToken.
        if safe.prime_extract.reference.has_model:
            model = CombatantToken(
                id=safe.id,
                team=safe.team,
                walk=safe.walk,
                formation=safe.formation,
                home_square=safe.home_square,
            )
            model.captor = captor
            model.readiness = readiness
            if safe.deployment == TokenDeployment.DEPLOYED_TO_HOME_SQUARE:
                model.mark_as_deployed()
            carrier = CombatantTokenCarrier(model=model)
            return ValidationResult.success(carrier)        
        # Otherwise, the client is a VectorBuilder that needs a Blueprint.
        carrier = CombatantTokenCarrier(
            blueprint=CombatantTokenBlueprint(
                id=safe.id,
                team=safe.team,
                walk=safe.walk,
                formation=safe.formation,
                home_square=safe.home_square,
                deployment=safe.deployment,
                captor=captor,
                readiness=readiness,
            )
        )
        return ValidationResult.success(carrier)
    
    