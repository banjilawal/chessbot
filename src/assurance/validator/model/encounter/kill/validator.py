# src/assurance/validator/model/encounter/kill/validator.py

"""
Module: assurance.validator.payload.encounter.kill.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from artifcat import ValidationResult
from assurance import EncounterProductEnvelope, EncounterEnemyValidator, EncounterValidatorToolkit
from domain import (
    CombatantReadiness, KillEncounter, KillEncounterBlueprint, KillEncounterPrimeExtract, PromotionState,
    Rank, Encounter
)
from err import (
    CombatantReadinessNullException, EncounterProductEnvelopeNullException,
    KillEncounterPrimeExtractNullException, KillEncounterValidatorException,
    PromotionStateNullException
)
from exchange import RankValidationRequest, EncounterValidationRequest
from transit import KillEncounterCarrier, RankCarrier, EncounterCarrier
from util import IdFactory, LoggingLevelRouter


class KillEncounterValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a KillEncounterCarrier is safe to use.

    Attributes:
        toolkit: EncounterValidatorToolkit
        enemy_validator: EncounterEnemyValidator

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[KillEncounterCarrier]:

    Super Class:
    """
    _toolkit: EncounterValidatorToolkit
    _enemy_validator: EncounterEnemyValidator
    
    def __init__(
            self,
            toolkit: Optional[EncounterValidatorToolkit] | None = None,
            enemy_validator: Optional[EncounterEnemyValidator] | None = None,
    ):
        """
        Args:
            toolkit: Optional[EncounterValidatorToolkit]
            enemy_validator: Optional[EncounterEnemyValidator]
        """
        self._toolkit = toolkit or EncounterValidatorToolkit()
        self._enemy_validator = enemy_validator or EncounterEnemyValidator()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            reference: EncounterProductEnvelope
    ) -> ValidationResult[KillEncounterCarrier]:
        """
        Assure the properties can assemble a safe KillEncounterCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                fields are flagged.
                    -   captor
                    -   rank
                    -   promotion_state
                    -   combatant_readiness
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            reference: EncounterProductEnvelope
        Returns:
            ValidationResult[KillEncounterCarrier]
        Raises:
            KillEncounterValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the property table is null or the wrong type.
        priming = self._toolkit.priming_validator.execute(
            candidate=reference,
            target_model=Type[EncounterProductEnvelope],
            null_exception=EncounterProductEnvelopeNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterValidatorException.MSG,
                    err_code=KillEncounterValidatorException.ERR_CODE,
                    ex=priming.exception
                )
            )
        # Handle the case that the property table has the wrong PrimeExtract.
        extract_validation = self._toolkit.priming_validator.execute(
            candidate=reference.prime_extract,
            target_model=Type[KillEncounterPrimeExtract],
            null_exception=KillEncounterPrimeExtractNullException(),
        )
        if extract_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterValidatorException.MSG,
                    err_code=KillEncounterValidatorException.ERR_CODE,
                    ex=extract_validation.exception
                )
            )
        # Handle the case that there is no blueprint in the carrier.
        prime_extract = cast(KillEncounterPrimeExtract, reference.prime_extract)
        blueprint = cast(KillEncounterBlueprint, prime_extract.blueprint)
        # --- START_COMBATANT_ENCOUNTER_READINESS_VALIDATION_PROCESS ---#
        
        # Handle the case that the readiness is flagged.
        readiness_validation = self._toolkit.priming_validator.execute(
            candidate=blueprint.readiness,
            target_model=CombatantReadiness,
            null_exception=CombatantReadinessNullException(),
        )
        if readiness_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterValidatorException.MSG,
                    err_code=KillEncounterValidatorException.ERR_CODE,
                    ex=readiness_validation.exception,
                )
            )
        # --- START_PROMOTION_STATE_VALIDATION_PROCESS ---#
        
        # Handle the case that the promotion_state is flagged.
        promotion_state_validation = self._toolkit.priming_validator.execute(
            candidate=blueprint.promotion_state,
            target_model=PromotionState,
            null_exception=PromotionStateNullException(),
        )
        if promotion_state_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterValidatorException.MSG,
                    err_code=KillEncounterValidatorException.ERR_CODE,
                    ex=promotion_state_validation.exception,
                )
            )
        # --- START_RANK_VALIDATION_PROCESS ---#
        
        # Handle the case that the rank is flagged.
        rank_validation = self._toolkit.wrapper.rank.extract_model(
            request=RankValidationRequest(
                item=RankCarrier(model=blueprint.rank),
                id=IdFactory.next_id(class_name="RankValidationRequest"),
            )
        )
        if rank_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KillEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterValidatorException.MSG,
                    err_code=KillEncounterValidatorException.ERR_CODE,
                    ex=rank_validation.exception,
                )
            )
        # --- START_CAPTOR_VALIDATION_PROCESS ---#
        
        captor_placeholder = blueprint.captor
        if blueprint.captor is not None:
            # Handle the case that the not-null captor is flagged
            enemy_validation_result = self._enemy_validator.execute(
                request=EncounterValidationRequest(
                    item=EncounterCarrier(model=blueprint.captor),
                    id=IdFactory.next_id(class_name="EncounterValidationRequest"),
                )
            )
            if enemy_validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    KillEncounterValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=KillEncounterValidatorException.MSG,
                        err_code=KillEncounterValidatorException.ERR_CODE,
                        ex=enemy_validation_result.exception,
                    )
                )
            # Otherwise update captor_placeholder
            captor_placeholder = cast(Encounter, enemy_validation_result.payload)

        # --- Extract validation payloads. ---#
        rank = cast(Rank, rank_validation.payload)
        readiness = cast(CombatantReadiness, readiness_validation.payload)
        promotion_state = cast(PromotionState, promotion_state_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        # The client wants a safe KillEncounter.
        if prime_extract.carrier.has_model:
            payload = KillEncounter(
                id=reference.safe.id,
                team=reference.safe.victim,
                formation=reference.safe.formation,
                home_square=reference.safe.home_square,
            )
            payload.rank = rank
            payload.readiness = readiness
            payload.captor = captor_placeholder
            payload.promotion_state = promotion_state
            payload.deployment = reference.safe.deployment
            payload.position = reference.safe.position
            payload.previous_position = reference.safe.previous_position
            
            return ValidationResult.success(KillEncounterCarrier(model=payload))
        
        # Otherwise, the client is a VectorBuilder that needs a Blueprint.
        payload = KillEncounterBlueprint(
            id=reference.safe.id,
            team=reference.safe.victim,
            formation=reference.safe.formation,
            home_square=reference.safe.home_square,
            deployment=reference.safe.deployment,
            position=reference.safe.position,
            previous_position=reference.safe.previous_position,
            promotion_state=promotion_state,
            captor=captor_placeholder,
            readiness=readiness,
            rank=rank,
        )
        return ValidationResult.success(KillEncounterCarrier(blueprint=payload))
    
    