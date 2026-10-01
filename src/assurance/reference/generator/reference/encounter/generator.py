# src/assurance/reference/generator/reference/encounter/generator.py

"""
Module: assurance.reference.generator.reference.encounter.generator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import (
    EncounterParticipantCertifier, EncounterParticipantChart, EncounterReferencePropertyTable,
    EncounterValidationReference, EncounterValidatorToolkit, ValidationReferenceGenerator
)
from config import NumericSetting
from domain import (
    Maneuver, Token, Encounter, EncounterBlueprint, EncounterPrimeExtract
)
from err import (
    EncounterValidationReferenceGeneratorException
)
from exchange import ManeuverValidationRequest, TokenValidationRequest
from transit import ManeuverCarrier, TokenCarrier
from util import IdFactory, LoggingLevelRouter


class EncounterValidationReferenceGenerator(ValidationReferenceGenerator[Encounter]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs validation checks on fields in Encounter superclass.

    Attributes:
        toolkit: EncounterValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[EncounterValidationReference]:

    Super Class:
        ValidationReferenceGenerator
    """
    _participant_certifier: EncounterParticipantCertifier
    
    def __init__(
            self,
            toolkit: Optional[EncounterValidatorToolkit] | None = None,
            participant_certifier: Optional[EncounterParticipantCertifier] | None = None,
    ):
        """
        Args:
            toolkit: Optional[EncounterValidatorToolkit]
            participant_certifier: Optional[EncounterPositionCertifier]
        """
        super().__init__(toolkit=toolkit or EncounterValidatorToolkit())
        self._participant_certifier = participant_certifier or EncounterParticipantCertifier()
        
    @property
    def toolkit(self) -> EncounterValidatorToolkit:
        return cast(EncounterValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[EncounterValidationReference]:
        """
        Assure a candidate's properties are reference for a Encounter

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Token, Formation, Deployment, id, or HomeSquare are flagged.
                    -   The position_table_generator fails.
            2.  Otherwise, send a EncounterValidationReference in the success result.
        Args:
            candidate: Any
        Returns:
           ValidationResult[EncounterValidationReference]
        Raises:
            EncounterValidationReferenceGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        load_result = self.toolkit.loader.execute(candidate)
        if load_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterValidationReferenceGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidationReferenceGeneratorException.MSG,
                    err_code=EncounterValidationReferenceGeneratorException.ERR_CODE,
                    ex=load_result.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(EncounterPrimeExtract, load_result.payload)
        blueprint = cast(EncounterBlueprint, prime_extract.blueprint)
        # --- START_ID_VALIDATION_PROCESS ---#
        
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self.toolkit.blueprint_id_extractor.execute(
            candidate=blueprint,
            blueprint_owner_name=blueprint.domain_class_name,
            blueprint_type=self.toolkit.types.blueprint,
            blueprint_null_exception=self.toolkit.nulls.blueprint,
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterValidationReferenceGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidationReferenceGeneratorException.MSG,
                    err_code=EncounterValidationReferenceGeneratorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # --- START_TOKEN_VALIDATION_PROCESS ---#
        
        # Handle the case that the token is flagged.
        victim_validation = self.toolkit.wrapper.token.extract_model(
            request=TokenValidationRequest(
                item=TokenCarrier(model=blueprint.victim),
                id=IdFactory.next_id(class_name="TokenValidationRequest"),
            )
        )
        if victim_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterValidationReferenceGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidationReferenceGeneratorException.MSG,
                    err_code=EncounterValidationReferenceGeneratorException.ERR_CODE,
                    ex=victim_validation.exception,
                )
            )
        # --- START_ATTACKER_MANEUVER_VALIDATION_PROCESS ---#
        
        # Handle the case that the token is flagged.
        attacker_maneuver_validation = self.toolkit.wrapper.maneuver.extract_model(
            request=ManeuverValidationRequest(
                item=ManeuverCarrier(model=blueprint.attacker_maneuver),
                id=IdFactory.next_id(class_name="TManeuverValidationRequest"),
            )
        )
        if attacker_maneuver_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterValidationReferenceGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidationReferenceGeneratorException.MSG,
                    err_code=EncounterValidationReferenceGeneratorException.ERR_CODE,
                    ex=attacker_maneuver_validation.exception,
                )
            )
        # --- START_ATTACKER_REWARD_VALIDATION_PROCESS ---#
        
        # Handle the case that the home_square gets flagged.
        attacker_reward = self.toolkit.number_validator.execute(
            candidate=blueprint.attacker_reward,
            floor=NumericSetting.floor(),
            ceiling=NumericSetting.ceiling(),
        )
        if attacker_reward.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterValidationReferenceGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidationReferenceGeneratorException.MSG,
                    err_code=EncounterValidationReferenceGeneratorException.ERR_CODE,
                    ex=attacker_reward.exception,
                )
            )
        # --- Extract from the validation payloads. ---#
        id = cast(int, id_validation.payload)
        victim = cast(Token, victim_validation.payload)
        attacker_reward = cast(int, attacker_reward.payload)
        attacker_maneuver = cast(Maneuver, attacker_maneuver_validation.payload)
        
        participant_chart_validation = self._participant_certifier.execute(
            victim=victim,
            attacker=attacker_maneuver.traveler,
        )
        # Handle the case that the victim and the attacker are the same
        if participant_chart_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterValidationReferenceGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidationReferenceGeneratorException.MSG,
                    err_code=EncounterValidationReferenceGeneratorException.ERR_CODE,
                    ex=participant_chart_validation.exception
                )
            )
        participant_chart = cast(
            EncounterParticipantChart, 
            participant_chart_validation.payload,
        )
        reference_properties = EncounterReferencePropertyTable(
            id=id,
            attacker_reward=attacker_reward,
            participant_chart=participant_chart,
            attacker_maneuver=attacker_maneuver,
        )
        
        # --- Send the work product. ---#
        validation_reference = EncounterValidationReference(
            reference_properties=reference_properties,
            prime_extract=prime_extract,
        )
        return ValidationResult.success(validation_reference)

    