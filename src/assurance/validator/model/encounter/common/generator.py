# src/assurance/validator/model/encounter/common/validator.py

"""
Module: assurance.validator.model.common.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import EncounterProductEnvelope, EncounterValidatorToolkit
from config import NumericSetting
from domain import EncounterBlueprint, EncounterPrimeExtract, Maneuver, Token
from exchange import ManeuverValidationRequest
from transit import ManeuverCarrier, TokenCarrier
from util import IdFactory, LoggingLevelRouter


class EncounterProductEnvelopeGenerator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs validation checks on fields in Encounter superclass.

    Attributes:
        toolkit: EncounterValidatorToolkit
        position_validator: EncounterPositionValidator

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[EncounterProductEnvelope]:

    Super Class:
    """
    _toolkit: EncounterValidatorToolkit
    
    def __init__(
            self,
            toolkit: Optional[EncounterValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[EncounterValidatorToolkit]
        """
        self._toolkit = toolkit or EncounterValidatorToolkit()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[EncounterProductEnvelope]:
        """
        Assure a candidate's properties are safe for a Encounter

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Token, Formation, Deployment, id, or HomeSquare are flagged.
                    -   The position_table_generator fails.
            2.  Otherwise, send a EncounterProductEnvelope in the success result.
        Args:
            candidate: Any
        Returns:
           ValidationResult[EncounterProductEnvelope]
        Raises:
            EncounterProductEnvelopeGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        load_result = self._toolkit.loader.execute(candidate)
        if load_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterProductEnvelopeGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterProductEnvelopeGeneratorException.MSG,
                    err_code=EncounterProductEnvelopeGeneratorException.ERR_CODE,
                    ex=load_result.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(EncounterPrimeExtract, load_result.payload)
        blueprint = cast(EncounterBlueprint, prime_extract.blueprint)
        # --- START_ID_VALIDATION_PROCESS ---#
        
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self._toolkit.blueprint_id_extractor.execute(
            candidate=blueprint,
            blueprint_owner_name=blueprint.domain_class_name,
            blueprint_type=self._toolkit.types.blueprint,
            blueprint_null_exception=self._toolkit.nulls.blueprint,
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterProductEnvelopeGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterProductEnvelopeGeneratorException.MSG,
                    err_code=EncounterProductEnvelopeGeneratorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # --- START_TOKEN_VALIDATION_PROCESS ---#
        
        # Handle the case that the victim is flagged.
        victim_validation = self._toolkit.wrapper.token.extract_model(
            request=TokenValidationRequest(
                item=TokenCarrier(model=blueprint.victim),
                id=IdFactory.next_id(class_name="TokenValidationRequest"),
            )
        )
        if victim_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterProductEnvelopeGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterProductEnvelopeGeneratorException.MSG,
                    err_code=EncounterProductEnvelopeGeneratorException.ERR_CODE,
                    ex=victim_validation.exception,
                )
            )
        # --- START_HOME_SQUARE_DETECTION_PROCESS ---#
        
        # Handle the case that the home_square gets flagged.
        attacker_maneuver_validation = self._toolkit.wrapper.maneuver.extract_model(
            request=ManeuverValidationRequest(
                item=ManeuverCarrier(model=blueprint.attacker_maneuver),
                id=IdFactory.next_id(class_name="ManeuverValidationRequest"),
            )
        )
        if attacker_maneuver_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterProductEnvelopeGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterProductEnvelopeGeneratorException.MSG,
                    err_code=EncounterProductEnvelopeGeneratorException.ERR_CODE,
                    ex=attacker_maneuver_validation.exception,
                )
            )
        attacker_reward_validation = self._toolkit.number_validator.execute(
            candidate=blueprint.attacker_reward,
            floor=NumericSetting.floor(),
            ceiling=NumericSetting.ceiling(),
        )
        if attacker_reward_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterProductEnvelopeGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterProductEnvelopeGeneratorException.MSG,
                    err_code=EncounterProductEnvelopeGeneratorException.ERR_CODE,
                    ex=attacker_reward_validation.exception,
                )
            )
        # --- Extract from the validation payloads. ---#
        id = cast(int, id_validation.payload)
        victim = cast(Token, victim_validation.payload)
        attacker_reward = cast(int, attacker_reward_validation.payload)
        attacker_maneuver = cast(Maneuver, attacker_maneuver_validation.payload)

        # --- START_POSITIONS_VALIDATION_PROCESS ---#
        


        
        # --- Send the work product. ---#
        encounter_property_table = EncounterProductEnvelope(
            id=id,
            token=token,
            formation=formation,
            home_square=home_square,
            deployment=deployment,
            position_table=position_table,
        )
        return ValidationResult.success(encounter_property_table)

    