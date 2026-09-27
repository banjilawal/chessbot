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
from assurance import (
    CommonAttackPropertyTable, AttackPositionTable, AttackPositionTableGenerator, 
    AttackValidatorToolkit
)
from domain import (
    Formation, HomeSquare, Team, AttackBlueprint, AttackDeployment, 
    AttackPrimeExtract
)
from err import (
    CommonAttackPropertyTableGeneratorException, FormationNullException,
    AttackDeploymentNullException
)
from exchange import TeamValidationRequest
from transit import TeamCarrier
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
    _position_table_generator: AttackPositionTableGenerator
    
    def __init__(
            self,
            toolkit: Optional[AttackValidatorToolkit] | None = None,
            position_validator: Optional[AttackPositionTableGenerator] | None = None,
    ):
        """
        Args:
            toolkit: Optional[AttackValidatorToolkit]
            position_validator: Optional[AttackPositionValidator]
        """
        self._toolkit = toolkit or AttackValidatorToolkit()
        self._position_table_generator = position_validator or AttackPositionTableGenerator()
    
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
                    -   Team, Formation, Deployment, id, or HomeSquare are flagged.
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
        # --- START_FORMATION_VALIDATION_PROCESS ---#
        
        # Handle the case that the formation is flagged.
        formation_validation = self._toolkit.priming_validator.execute(
            candidate=attack_blueprint.formation,
            target_model=Formation,
            null_exception=FormationNullException(),
        )
        if formation_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonAttackPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonAttackPropertyTableGeneratorException.MSG,
                    err_code=CommonAttackPropertyTableGeneratorException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # --- START_DEPLOYEMENT_STATE_VALIDATION_PROCESS ---#
        
        # Handle the case that the deployment is flagged.
        deployment_validation = self._toolkit.priming_validator.execute(
            candidate=attack_blueprint.deployment,
            target_model=AttackDeployment,
            null_exception=AttackDeploymentNullException(),
        )
        if deployment_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonAttackPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonAttackPropertyTableGeneratorException.MSG,
                    err_code=CommonAttackPropertyTableGeneratorException.ERR_CODE,
                    ex=deployment_validation.exception,
                )
            )
        # --- START_TEAM_VALIDATION_PROCESS ---#
        
        # Handle the case that the team is flagged.
        team_validation = self._toolkit.wrapper.team.extract_model(
            request=TeamValidationRequest(
                item=TeamCarrier(model=attack_blueprint.team),
                id=IdFactory.next_id(class_name="TeamValidationRequest"),
            )
        )
        if team_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonAttackPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonAttackPropertyTableGeneratorException.MSG,
                    err_code=CommonAttackPropertyTableGeneratorException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # --- START_HOME_SQUARE_DETECTION_PROCESS ---#
        
        # Handle the case that the home_square gets flagged.
        home_detection = self._toolkit.home_square_extractor.execute(
            blueprint=attack_blueprint,
        )
        if home_detection.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonAttackPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonAttackPropertyTableGeneratorException.MSG,
                    err_code=CommonAttackPropertyTableGeneratorException.ERR_CODE,
                    ex=home_detection.exception,
                )
            )
        # --- START_POSITIONS_VALIDATION_PROCESS ---#
        
        # Handle the case that the current_position is flagged.
        generation_result = self._position_table_generator.execute(
            blueprint=attack_blueprint
        )
        if generation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonAttackPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonAttackPropertyTableGeneratorException.MSG,
                    err_code=CommonAttackPropertyTableGeneratorException.ERR_CODE,
                    ex=generation_result.exception,
                )
            )
        # --- Extract from the validation payloads. ---#
        id = cast(int, id_validation.payload)
        team = cast(Team, team_validation.payload)
        home_square = cast(HomeSquare, home_detection.payload)
        formation = cast(Formation, formation_validation.payload)
        deployment = cast(AttackDeployment, deployment_validation.payload)
        position_table = cast(AttackPositionTable, generation_result.payload)
        
        # --- Send the work product. ---#
        attack_property_table = CommonAttackPropertyTable(
            id=id,
            team=team,
            formation=formation,
            home_square=home_square,
            deployment=deployment,
            position_table=position_table,
        )
        return ValidationResult.success(attack_property_table)

    