# src/assurance/envelope/consumer/token/consumer.py

"""
Module: assurance.envelope.consumer.token.consumer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import CombatantTokenEnvelopeConsumer, TokenEnvelopeConsumer
from domain import PawnToken, PawnTokenBlueprint, PromotionState, Rank, TokenDeployment
from err import (
    PawnTokenEnvelopeConsumerException, PromotionStateNullException, RootTokenEnvelopeNullException,
    TokenCarrierEmptyException
)
from exchange import RankValidationRequest
from transit import CombatantTokenCarrier, PawnTokenCarrier, RankCarrier, RootTokenEnvelope
from util import IdFactory, LoggingLevelRouter


class PawnTokenEnvelopeConsumer(
    TokenEnvelopeConsumer[PawnToken]
):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Assure a PawnToken covered by a RootTokenEnvelope is safe.

    Attributes:
        toolkit: TokenValidatorToolkit
        combatant_consumer: CombatantTokenEnvelopeConsumer

    Provides:
        -   def execute(
                    envelope: RootTokenEnvelope
            ) -> ValidationResult[PawnTokenCarrier]

    Super Class:
        RootEnvelopeConsumer
    """
    
    _combatant_consumer: CombatantTokenEnvelopeConsumer
    
    def __init__(
            self,
            combatant_consumer: Optional[CombatantTokenEnvelopeConsumer] | None = None
    ):
        """
        Args:
            combatant_consumer: Optional[CombatantTokenEnvelopeConsumer]
        """
        super().__init__()
        self._combatant_consumer = combatant_consumer or CombatantTokenEnvelopeConsumer()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            envelope: RootTokenEnvelope
    ) -> ValidationResult[PawnTokenCarrier]:
        """
        Assure the properties can assemble a safe PawnTokenCarrier.

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
            ValidationResult[PawnTokenCarrier]
        Raises:
            PawnTokenEnvelopeConsumerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        priming = self._toolkit.priming_validator.execute(
            candidate=envelope,
            target_model=RootTokenEnvelope,
            null_exception=RootTokenEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenEnvelopeConsumerException.MSG,
                    err_code=PawnTokenEnvelopeConsumerException.ERR_CODE,
                    ex=priming.exception
                )
            )
        safe = cast(RootTokenEnvelope, priming.payload)
        
        result = self._combatant_consumer.execute(envelope=safe)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenEnvelopeConsumerException.MSG,
                    err_code=PawnTokenEnvelopeConsumerException.ERR_CODE,
                    ex=result.exception
                )
            )
        reference = cast(CombatantTokenCarrier, result.payload)
        if not isinstance(reference, PawnTokenCarrier):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenEnvelopeConsumerException.MSG,
                    err_code=PawnTokenEnvelopeConsumerException.ERR_CODE,
                    ex=TypeError(
                        f"Expected PawnTokenCarrier received CombatantTokenCarrier instead."
                    )
                )
            )
        carrier = cast(PawnTokenCarrier, reference)
        blueprint = carrier.extract_blueprint()
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenEnvelopeConsumerException.MSG,
                    err_code=PawnTokenEnvelopeConsumerException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    )
                )
            )
        promotion_state_validation = self.toolkit.priming_validator.execute(
            candidate=blueprint.promotion_state,
            target_model=PromotionState,
            null_exception=PromotionStateNullException(),
        )
        if promotion_state_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenEnvelopeConsumerException.MSG,
                    err_code=PawnTokenEnvelopeConsumerException.ERR_CODE,
                    ex=promotion_state_validation.exception,
                )
            )
        rank_validation = self.toolkit.wrapper.rank.extract_model(
            request=RankValidationRequest(
                item=RankCarrier(model=blueprint.rank),
                id=IdFactory.next_id(class_name="RankValidationRequest")
            )
        )
        if rank_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenEnvelopeConsumerException.MSG,
                    err_code=PawnTokenEnvelopeConsumerException.ERR_CODE,
                    ex=rank_validation.exception,
                )
            )
        
        rank = cast(Rank, rank_validation.payload)
        promotion_state = cast(PromotionState, promotion_state_validation.payload)
        # --- Forward the appropriate work product to the caller. ---#
        # The client wants a safe PawnToken.
        if safe.prime_extract.reference.has_model:
            model = PawnToken(
                id=safe.id,
                walk=safe.walk,
                team=safe.team,
                formation=safe.formation,
                home_square=safe.home_square,
            )
            model.captor = blueprint.captor
            model.readiness = blueprint.readiness
            model.rank = rank
            model.promotion_state = promotion_state
            if safe.deployment == TokenDeployment.DEPLOYED_TO_HOME_SQUARE:
                model.mark_as_deployed()
            carrier = PawnTokenCarrier(model=model)
            return ValidationResult.success(carrier)        
        # Otherwise, the client is a VectorBuilder that needs a Blueprint.
        carrier = PawnTokenCarrier(
            blueprint=PawnTokenBlueprint(
                id=safe.id,
                team=safe.team,
                walk=safe.walk,
                rank=rank,
                promotion_state=promotion_state,
                formation=safe.formation,
                home_square=safe.home_square,
                deployment=safe.deployment,
                captor=blueprint.captor,
                readiness=blueprint.readiness,
            )
        )
        return ValidationResult.success(carrier)
    
    