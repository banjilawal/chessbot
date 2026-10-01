# src/assurance/validator/model/encounter/combatant/validator.py

"""
Module: assurance.validator.payload.encounter.combatant.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from artifcat import ValidationResult
from assurance import (
    CommonEncounterPropertyTable, EncounterEnemyValidator, EncounterValidatorToolkit
)
from domain import (
    CombatantReadiness, CombatantEncounter, CombatantEncounterBlueprint,
    CombatantEncounterPrimeExtract, Encounter
)
from err import (
    CombatantReadinessNullException, CombatantEncounterPrimeExtractNullException,
    CombatantEncounterValidatorException, CommonEncounterPropertyTableNullException
)
from exchange import EncounterValidationRequest
from transit import CombatantEncounterCarrier, EncounterCarrier
from util import IdFactory, LoggingLevelRouter


class CombatantEncounterValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a CombatantEncounterCarrier is safe to use.

    Attributes:
        toolkit: EncounterValidatorToolkit
        enemy_validator: EncounterEnemyValidator

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[CombatantEncounterCarrier]:

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
    ) -> ValidationResult[CombatantEncounterCarrier]:
        """
        Assure the properties can assemble a safe CombatantEncounterCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                fields are flagged.
                    -   captor
                    -   combatant_readiness
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            property_table: CommonEncounterPropertyTable
        Returns:
            ValidationResult[CombatantEncounterCarrier]
        Raises:
            CombatantEncounterValidatorException
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
                CombatantEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantEncounterValidatorException.MSG,
                    err_code=CombatantEncounterValidatorException.ERR_CODE,
                    ex=table_validation.exception
                )
            )
        # Handle the case that the property table has the wrong PrimeExtract.
        extract_validation = self._toolkit.priming_validator.execute(
            candidate=property_table.prime_extract,
            target_model=Type[CombatantEncounterPrimeExtract],
            null_exception=CombatantEncounterPrimeExtractNullException(),
        )
        if extract_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CombatantEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantEncounterValidatorException.MSG,
                    err_code=CombatantEncounterValidatorException.ERR_CODE,
                    ex=extract_validation.exception
                )
            )
        # Handle the case that there is no blueprint in the carrier.
        prime_extract = cast(CombatantEncounterPrimeExtract, property_table.prime_extract)
        blueprint = cast(CombatantEncounterBlueprint, prime_extract.blueprint)
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
                CombatantEncounterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantEncounterValidatorException.MSG,
                    err_code=CombatantEncounterValidatorException.ERR_CODE,
                    ex=readiness_validation.exception,
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
                    CombatantEncounterValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CombatantEncounterValidatorException.MSG,
                        err_code=CombatantEncounterValidatorException.ERR_CODE,
                        ex=enemy_validation_result.exception,
                    )
                )
            # Otherwise update captor_placeholder
            captor_placeholder = cast(Encounter, enemy_validation_result.payload)

        # --- Extract validation payloads. ---#
        readiness = cast(CombatantReadiness, readiness_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        # The client wants a safe CombatantEncounter.
        if prime_extract.carrier.has_model:
            payload = CombatantEncounter(
                id=property_table.safe.id,
                team=property_table.safe.victim,
                formation=property_table.safe.formation,
                home_square=property_table.safe.home_square,
            )
            payload.readiness = readiness
            payload.captor = captor_placeholder
            payload.deployment = property_table.safe.deployment
            payload.position = property_table.safe.position
            payload.previous_position = property_table.safe.previous_position
            
            return ValidationResult.success(CombatantEncounterCarrier(model=payload))
        
        # Otherwise, the client is a VectorBuilder that needs a Blueprint.
        payload = CombatantEncounterBlueprint(
            id=property_table.safe.id,
            team=property_table.safe.victim,
            formation=property_table.safe.formation,
            home_square=property_table.safe.home_square,
            deployment=property_table.safe.deployment,
            position=property_table.safe.position,
            previous_position=property_table.safe.previous_position,
            captor=captor_placeholder,
            readiness=readiness,
        )
        return ValidationResult.success(CombatantEncounterCarrier(blueprint=payload))
    
    