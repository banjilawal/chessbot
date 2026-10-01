# src/assurance/validator/model/encounter/king/validator.py

"""
Module: assurance.validator.payload.encounter.king.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from artifcat import ValidationResult
from assurance import CommonEncounterPropertyTable, EncounterEnemyValidator, EncounterValidatorToolkit
from domain import (
    KingReadiness, KingEncounter, KingEncounterBlueprint, KingEncounterPrimeExtract, PromotionState,
    Rank, Encounter
)
from err import (
    KingReadinessNullException, CommonEncounterPropertyTableNullException,
    KingEncounterPrimeExtractNullException, KingEncounterValidatorException,
    PromotionStateNullException
)
from exchange import RankValidationRequest, EncounterValidationRequest
from transit import KingEncounterCarrier, RankCarrier, EncounterCarrier
from util import IdFactory, LoggingLevelRouter


class KingEncounterValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a KingEncounterCarrier is safe to use.

    Attributes:
        toolkit: EncounterValidatorToolkit
        enemy_validator: EncounterEnemyValidator

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[KingEncounterCarrier]:

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
            property_table: CommonEncounterPropertyTable
    ) -> ValidationResult[KingEncounterCarrier]:
        """
        Assure the properties can assemble a safe KingEncounterCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                fields are flagged.
                    -   captor
                    -   rank
                    -   promotion_state
                    -   king_readiness
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            property_table: CommonEncounterPropertyTable
        Returns:
            ValidationResult[KingEncounterCarrier]
        Raises:
            KingEncounterValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the property table is null or the wrong type.
        table_validation = self._toolkit.priming_validator.execute(
            candidate=property_table,
            target_model=Type[CommonEncounterPropertyTable],
            null_exception=CommonEncounterPropertyTableNullException(),
        )
        if table_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingEncounterValidatorException.MSG,
                    err_code=KingEncounterValidatorException.ERR_CODE,
                    ex=table_validation.exception
                )
            )
        # Handle the case that the property table has the wrong PrimeExtract.
        extract_validation = self._toolkit.priming_validator.execute(
            candidate=property_table.prime_extract,
            target_model=Type[KingEncounterPrimeExtract],
            null_exception=KingEncounterPrimeExtractNullException(),
        )
        if extract_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingEncounterValidatorException.MSG,
                    err_code=KingEncounterValidatorException.ERR_CODE,
                    ex=extract_validation.exception
                )
            )
        # Handle the case that there is no blueprint in the carrier.
        prime_extract = cast(KingEncounterPrimeExtract, property_table.prime_extract)
        blueprint = cast(KingEncounterBlueprint, prime_extract.blueprint)
        # --- START_KING_ENCOUNTER_READINESS_VALIDATION_PROCESS ---#
        
        # Handle the case that the readiness is flagged.
        readiness_validation = self._toolkit.priming_validator.execute(
            candidate=blueprint.readiness,
            target_model=KingReadiness,
            null_exception=KingReadinessNullException(),
        )
        if readiness_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingEncounterValidatorException.MSG,
                    err_code=KingEncounterValidatorException.ERR_CODE,
                    ex=readiness_validation.exception,
                )
            )
        # --- START_PROMOTION_STATE_VALIDATION_PROCESS ---#
        
        # Handle the case that the promotion_state is flagged.
        promotion_state_validation = self._toolkit.priming_validator.execute(
            candidate=blueprint.checkmate,
            target_model=PromotionState,
            null_exception=PromotionStateNullException(),
        )
        if promotion_state_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingEncounterValidatorException.MSG,
                    err_code=KingEncounterValidatorException.ERR_CODE,
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
                KingEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingEncounterValidatorException.MSG,
                    err_code=KingEncounterValidatorException.ERR_CODE,
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
                    KingEncounterValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=KingEncounterValidatorException.MSG,
                        err_code=KingEncounterValidatorException.ERR_CODE,
                        ex=enemy_validation_result.exception,
                    )
                )
            # Otherwise update captor_placeholder
            captor_placeholder = cast(Encounter, enemy_validation_result.payload)

        # --- Extract validation payloads. ---#
        rank = cast(Rank, rank_validation.payload)
        readiness = cast(KingReadiness, readiness_validation.payload)
        promotion_state = cast(PromotionState, promotion_state_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        # The client wants a safe KingEncounter.
        if prime_extract.carrier.has_model:
            payload = KingEncounter(
                id=property_table.safe.id,
                team=property_table.safe.victim,
                formation=property_table.safe.formation,
                home_square=property_table.safe.home_square,
            )
            payload.rank = rank
            payload.readiness = readiness
            payload.captor = captor_placeholder
            payload.promotion_state = promotion_state
            payload.deployment = property_table.safe.deployment
            payload.position = property_table.safe.position
            payload.previous_position = property_table.safe.previous_position
            
            return ValidationResult.success(KingEncounterCarrier(model=payload))
        
        # Otherwise, the client is a VectorBuilder that needs a Blueprint.
        payload = KingEncounterBlueprint(
            id=property_table.safe.id,
            team=property_table.safe.victim,
            formation=property_table.safe.formation,
            home_square=property_table.safe.home_square,
            deployment=property_table.safe.deployment,
            position=property_table.safe.position,
            previous_position=property_table.safe.previous_position,
            promotion_state=promotion_state,
            captor=captor_placeholder,
            readiness=readiness,
            rank=rank,
        )
        return ValidationResult.success(KingEncounterCarrier(blueprint=payload))
    
    