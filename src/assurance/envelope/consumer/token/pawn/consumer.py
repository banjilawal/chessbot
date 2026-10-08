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
from domain import (
    Bishop, Knight, Pawn, PawnToken, PawnTokenBlueprint, Persona,
    PromotionState, Queen, Rank, Rook, TokenDeployment
)
from err import (
    PawnTokenEnvelopeConsumerException, PawnTokenPromotionConsistencyException,
    PersonaNullException, PromotionStateNullException, RootTokenEnvelopeNullException,
    TokenCarrierEmptyException
)
from exchange import RankValidationRequest
from transit import (
    CombatantTokenCarrier, CombatantTokenEnvelope, PawnTokenCarrier,
    RankCarrier, RootTokenEnvelope
)
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
        
        # --- PREPROCESS_THE_ENVELOPE ---#
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
        # --- RUN_THE_COMBATANT_TOKEN_VALIDATION_PROCESS. ---#
        original = cast(RootTokenEnvelope, priming.payload)
        consumption_result = self._combatant_consumer.execute(envelope=original)
        
        # Handle the case that envelope cannot be consumed.
        if consumption_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenEnvelopeConsumerException.MSG,
                    err_code=PawnTokenEnvelopeConsumerException.ERR_CODE,
                    ex=consumption_result.exception
                )
            )
        reference = cast(CombatantTokenCarrier, consumption_result.payload)
        if not isinstance(reference, PawnTokenCarrier):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenEnvelopeConsumerException.MSG,
                    err_code=PawnTokenEnvelopeConsumerException.ERR_CODE,
                    ex=TypeError(
                        f"Expected PawnTokenCarrier received "
                        f"CombatantTokenCarrier instead."
                    )
                )
            )
        carrier = cast(PawnTokenCarrier, reference)
        blueprint = carrier.extract_blueprint()
        # Handle the case that the blueprint is null.
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
        safe = CombatantTokenEnvelope(
            id=original.id,
            team=original.team,
            footstep=original.footstep,
            formation=original.formation,
            deployment=original.deployment,
            home_square=original.home_square,
            prime_extract=original.prime_extract,
            readiness=blueprint.readiness,
            captor=blueprint.captor,
        )
        # --- START_PROMOTION_STATE_VALIDATION_PROCESS ---#
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
        # --- START_THE_PROMOTION_PERSONA_VALIDATION_PROCESS ---#
        promotion_persona_validation = self.toolkit.priming_validator.execute(
            candidate=blueprint.promotion_persona,
            target_model=Persona,
            null_exception=PersonaNullException(),
        )
        if promotion_persona_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenEnvelopeConsumerException.MSG,
                    err_code=PawnTokenEnvelopeConsumerException.ERR_CODE,
                    ex=promotion_persona_validation.exception,
                )
            )
        # --- START_THE_RANK_VALIDATION_PROCESS ---#
        rank_validation = self.toolkit.wrapper.rank.extract_model(
            request=RankValidationRequest(
                item=RankCarrier(model=blueprint.rank),
                id=IdFactory.next_id(class_name="RankValidationRequest")
            )
        )
        # Handle the case that the rank is not safe.
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
        # --- RUN_THE_PROMOTION_INCONSISTENCY_CHECK. ---#
        # Handle the case that a promotion inconsistency occurs.
        if blueprint.promotion_is_not_consistent:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PawnTokenEnvelopeConsumerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PawnTokenEnvelopeConsumerException.MSG,
                    err_code=PawnTokenEnvelopeConsumerException.ERR_CODE,
                    ex=PawnTokenPromotionConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PawnTokenPromotionConsistencyException.MSG,
                        err_code=PawnTokenPromotionConsistencyException.ERR_CODE,
                    ),
                )
            )
        # --- EXTRACT_THE_VALIDATION_PAYLOADS. ---#
        promotion_persona = cast(Persona, promotion_persona_validation.payload)
        promotion_state = cast(PromotionState, promotion_state_validation.payload)
        rank = self._make_rank(promotion_persona)
        
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#

        # The client wants a safe PawnToken.
        if safe.prime_extract.reference.has_model:
            model = PawnToken(
                id=safe.id,
                footstep=safe.footstep,
                team=safe.team,
                formation=safe.formation,
                home_square=safe.home_square,
            )
            # Update the mutatable fields.
            model.rank = rank
            model.captor = safe.captor
            model.readiness = safe.readiness
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
                captor=safe.captor,
                footstep=safe.footstep,
                readiness=safe.readiness,
                formation=safe.formation,
                deployment=safe.deployment,
                home_square=safe.home_square,
                promotion_state=promotion_state,
                promotion_persona=promotion_persona,
                rank=rank,
            )
        )
        return ValidationResult.success(carrier)
    
    @LoggingLevelRouter.monitor
    def _make_rank(self, persona: Persona) -> Rank:
        if persona == Persona.BISHOP:
            return Bishop()
        if persona == Persona.KNIGHT:
            return Knight()
        if persona == Persona.ROOK:
            return Rook()
        if persona == Persona.QUEEN:
            return Queen()
        return Pawn()