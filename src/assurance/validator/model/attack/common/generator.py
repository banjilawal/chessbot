# src/assurance/validator/model/attack/common/validator.py

"""
Module: assurance.validator.model.common.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import AttackValidatorToolkit, CommonAttackPropertyTable, SafeSuperAttackPropertyTable
from domain import AttackBlueprint, AttackPrimeExtract, Maneuver, Token
from exchange import ManeuverValidationRequest, TokenValidationRequest
from transit import ManeuverCarrier, TokenCarrier
from util import IdFactory, LoggingLevelRouter


class CommonAttackPropertyTableGenerator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs validation checks on fields in Attack superclass.

    Attributes:
        toolkit: AttackValidatorToolkit
        position_validator: AttackPositionValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[CommonAttackPropertyTable]:

    Super Class:
    """
    _toolkit: AttackValidatorToolkit
    
    def __init__(
            self,
            toolkit: Optional[AttackValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[AttackValidatorToolkit]
        """
        self._toolkit = toolkit or AttackValidatorToolkit()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[CommonAttackPropertyTable]:
        """
        Assure a candidate's properties are safe for a Attack

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Maneuver, Formation, Deployment, id, or HomeSquare are flagged.
                    -   The position_table_generator fails.
            2.  Otherwise, send a CommonAttackPropertyTable in the success result.
        Args:
            candidate: Any
        Returns:
           ValidationResult[CommonAttackPropertyTable]
        Raises:
            CommonAttackPropertyTableGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        load_result = self._toolkit.loader.execute(candidate)
        if load_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonAttackPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonAttackPropertyTableGeneratorException.MSG,
                    err_code=CommonAttackPropertyTableGeneratorException.ERR_CODE,
                    ex=load_result.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(AttackPrimeExtract, load_result.payload)
        attack_blueprint = cast(AttackBlueprint, prime_extract.blueprint)
        # --- START_ID_VALIDATION_PROCESS ---#
        
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self._toolkit.blueprint_id_extractor.execute(
            candidate=attack_blueprint,
            blueprint_owner_name=attack_blueprint.domain_class_name,
            blueprint_type=self._toolkit.types.blueprint,
            blueprint_null_exception=self._toolkit.nulls.blueprint,
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonAttackPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonAttackPropertyTableGeneratorException.MSG,
                    err_code=CommonAttackPropertyTableGeneratorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # --- START_VICTIM_VALIDATION_PROCESS ---#
        victim_validation = self._toolkit.wrapper.token.extract_model(
            request=TokenValidationRequest(
                item=TokenCarrier(model=attack_blueprint.victim),
                id=IdFactory.next_id(class_name="TokenValidationRequest"),
            )
        )
        attacker_validation = self._toolkit.wrapper.token.extract_model(
            request=TokenValidationRequest(
                item=TokenCarrier(model=attack_blueprint.attacker),
                id=IdFactory.next_id(class_name="TokenValidationRequest"),
            )
        )
        # --- START_MANEUVER_VALIDATION_PROCESS ---#
        
        # Handle the case that the maneuver is flagged.
        maneuver_validation = self._toolkit.wrapper.maneuver.extract_model(
            request=ManeuverValidationRequest(
                item=ManeuverCarrier(model=attack_blueprint.attacker_maneuver),
                id=IdFactory.next_id(class_name="ManeuverValidationRequest"),
            )
        )
        if maneuver_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonAttackPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonAttackPropertyTableGeneratorException.MSG,
                    err_code=CommonAttackPropertyTableGeneratorException.ERR_CODE,
                    ex=maneuver_validation.exception,
                )
            )
        # --- Extract from the validation payloads. ---#
        id = cast(int, id_validation.payload)
        victim = cast(Token, victim_validation.payload)
        attacker = cast(Token, attacker_validation.payload)
        maneuver = cast(Maneuver, maneuver_validation.payload)
        
        if victim == attacker:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonAttackPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonAttackPropertyTableGeneratorException.MSG,
                    err_code=CommonAttackPropertyTableGeneratorException.ERR_CODE,
                    ex=maneuver_validation.exception,
                )
            )
        safe_property_table = SafeSuperAttackPropertyTable(
            id=id,
            victim=victim,
            attacker=attacker,
            maneuver=maneuver,
        )
        
        # --- Send the work product. ---#
        attack_property_table = CommonAttackPropertyTable(
            id=id,
            maneuver=maneuver,
            formation=formation,
            home_square=home_square,
            deployment=deployment,
            position_table=position_table,
        )
        return ValidationResult.success(attack_property_table)

    