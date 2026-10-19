# src/assurance/envelope/consumer/rank/rook/consumer.py

"""
Module: assurance.envelope.consumer.rank.rook.consumer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ValidationResult
from assurance import RankEnvelopeConsumer
from domain import Rook, RookBlueprint, Persona
from err import (
    RookEnvelopeConsumerException, RookPersonaConsistencyException, PersonaNullException,
    RankCarrierEmptyException, RankValidationRouterException, RootRankEnvelopeNullException
)
from transit import RookCarrier, RootRankEnvelope

from util import LoggingLevelRouter


class RookEnvelopeConsumer(RankEnvelopeConsumer[Rook]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure a Rook covered by a RootRankEnvelope is safe.

    Attributes:
        toolkit: RankValidatorToolkit

    Provides:
        -   def execute(
                    envelope: RootRankEnvelope
            ) -> ValidationResult[RookCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    
    def __init__(self):
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            envelope: RootRankEnvelope
    ) -> ValidationResult[RookCarrier]:
        """
        Assure the properties can assemble a safe RookCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the
                following occur.
                    -   The consumer cannot be primed.
                    -   The envelope is not meant for the consumer. 
                    -   the victim is a Rook.
                    -   The location is not consistent.
            2.  Otherwise, Send a Carrier with the correct type of payload in
                the success result.
        Args:
             envelope: RootRankEnvelope
        Returns:
            ValidationResult[RookCarrier]
        Raises:
            RookEnvelopeConsumerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- INITIATE_THE_VALIDATION_PROCESS ---#
        priming = self.toolkit.priming_validator.execute(
            candidate=envelope,
            target_model=RootRankEnvelope,
            null_exception=RootRankEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RookEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RookEnvelopeConsumerException.MSG,
                    err_code=RookEnvelopeConsumerException.ERR_CODE,
                    ex=priming.exception
                )
            )
        safe = cast(RootRankEnvelope, priming.payload)
        # Handle the case that the envelope wrong envelope was delivered.
        if not safe.for_rook_consumer:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RookEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RookEnvelopeConsumerException.MSG,
                    err_code=RookEnvelopeConsumerException.ERR_CODE,
                    ex=RankValidationRouterException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RankValidationRouterException.MSG,
                        err_code=RankValidationRouterException.ERR_CODE,
                    )
                )
            )
        # --- EXTRACT_THE_BLUEPRINT_THE_VALIDATOR_NEEDS ---#
        reference = cast(RookCarrier, safe.prime_extract.reference)
        blueprint = reference.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RookEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RookEnvelopeConsumerException.MSG,
                    err_code=RookEnvelopeConsumerException.ERR_CODE,
                    ex=RankCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RankCarrierEmptyException.MSG,
                        err_code=RankCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- START_ROOK_PERSONA_VALIDATION_PROCESS ---#
        persona_validation = self._toolkit.priming_validator.execute(
            candidate=blueprint.persona,
            target_model=Persona,
            null_exception=PersonaNullException(),
        )
        # Handle the case that the persona is flagged.
        if persona_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RookEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RookEnvelopeConsumerException.MSG,
                    err_code=RookEnvelopeConsumerException.ERR_CODE,
                    ex=persona_validation.exception,
                )
            )
        # --- Extract validation payloads. ---#
        persona = cast(Persona, persona_validation.payload)
        if persona != Persona.ROOK:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RookEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RookEnvelopeConsumerException.MSG,
                    err_code=RookEnvelopeConsumerException.ERR_CODE,
                    ex=RookPersonaConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RookPersonaConsistencyException.MSG,
                        err_code=RookPersonaConsistencyException.ERR_CODE,
                    ),
                )
            )
        
        # --- Forward the appropriate work product to the caller. ---#
        # The client wants a safe Rook.
        if safe.prime_extract.reference.has_model:
            model = Rook(persona=persona)
            carrier = RookCarrier(model=model)
            return ValidationResult.success(carrier)        
        # Otherwise, the client is a VectorBuilder that needs a Blueprint.
        carrier = RookCarrier(blueprint=RookBlueprint(persona=persona))
        return ValidationResult.success(carrier)
    
    