# src/assurance/validator/model/token/common/validator.py

"""
Module: assurance.validator.model.common.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, cast

from artifcat import ValidationResult
from assurance import CommonTokenPropertyTable, TokenPositionTable, TokenPositionTableGenerator, TokenValidatorToolkit
from domain import (
    Coord, Formation, HomeSquare, Team, TokenBlueprint, TokenDeployment,
    TokenPrimeExtract
)
from err import (
    CommonTokenPropertyTableGeneratorException, FormationNullException,
    TokenDeploymentNullException
)
from exchange import TeamValidationRequest
from transit import TeamCarrier
from util import IdFactory, LoggingLevelRouter


class CommonTokenPropertyTableGenerator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Runs validation checks on fields in Token superclass.

    Attributes:
        toolkit: TokenValidatorToolkit
        position_validator: TokenPositionValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[CommonTokenPropertyTable]:

    Super Class:
    """
    _toolkit: TokenValidatorToolkit
    _position_table_generator: TokenPositionTableGenerator
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
            position_validator: Optional[TokenPositionTableGenerator] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidatorToolkit]
            position_validator: Optional[TokenPositionValidator]
        """
        self._toolkit = toolkit or TokenValidatorToolkit()
        self._position_table_generator = position_validator or TokenPositionTableGenerator()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[CommonTokenPropertyTable]:
        """
        Assure a candidate is a safe TokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   Team, Formation, Deployment, id, or HomeSquare are flagged.
                    -   The validation_router does not return a product
            2.  Otherwise, send a TokenCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TokenCarrier]
        Raises:
            CommonTokenPropertyValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        load_result = self._toolkit.loader.execute(candidate)
        if load_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonTokenPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonTokenPropertyTableGeneratorException.MSG,
                    err_code=CommonTokenPropertyTableGeneratorException.ERR_CODE,
                    ex=load_result.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(TokenPrimeExtract, load_result.payload)
        token_blueprint = cast(TokenBlueprint, prime_extract.blueprint)
        # --- START_ID_VALIDATION_PROCESS ---#
        
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self._toolkit.blueprint_id_extractor.execute(
            candidate=token_blueprint,
            blueprint_owner_name=token_blueprint.domain_class_name,
            blueprint_type=self._toolkit.types.blueprint,
            blueprint_null_exception=self._toolkit.nulls.blueprint,
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonTokenPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonTokenPropertyTableGeneratorException.MSG,
                    err_code=CommonTokenPropertyTableGeneratorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # --- START_FORMATION_VALIDATION_PROCESS ---#
        
        # Handle the case that the formation is flagged.
        formation_validation = self._toolkit.priming_validator.execute(
            candidate=token_blueprint.formation,
            target_model=Formation,
            null_exception=FormationNullException(),
        )
        if formation_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonTokenPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonTokenPropertyTableGeneratorException.MSG,
                    err_code=CommonTokenPropertyTableGeneratorException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # --- START_DEPLOYEMENT_STATE_VALIDATION_PROCESS ---#
        
        # Handle the case that the deployment is flagged.
        deployment_validation = self._toolkit.priming_validator.execute(
            candidate=token_blueprint.deployment,
            target_model=TokenDeployment,
            null_exception=TokenDeploymentNullException(),
        )
        if deployment_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonTokenPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonTokenPropertyTableGeneratorException.MSG,
                    err_code=CommonTokenPropertyTableGeneratorException.ERR_CODE,
                    ex=deployment_validation.exception,
                )
            )
        # --- START_TEAM_VALIDATION_PROCESS ---#
        
        # Handle the case that the team is flagged.
        team_validation = self._toolkit.wrapper.team.extract_model(
            request=TeamValidationRequest(
                item=TeamCarrier(model=token_blueprint.team),
                id=IdFactory.next_id(class_name="TeamValidationRequest"),
            )
        )
        if team_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonTokenPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonTokenPropertyTableGeneratorException.MSG,
                    err_code=CommonTokenPropertyTableGeneratorException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # --- START_HOME_SQUARE_DETECTION_PROCESS ---#
        
        # Handle the case that the home_square gets flagged.
        home_detection = self._toolkit.home_square_extractor.execute(
            blueprint=token_blueprint,
        )
        if home_detection.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonTokenPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonTokenPropertyTableGeneratorException.MSG,
                    err_code=CommonTokenPropertyTableGeneratorException.ERR_CODE,
                    ex=home_detection.exception,
                )
            )
        # --- START_POSITIONS_VALIDATION_PROCESS ---#
        
        # Handle the case that the current_position is flagged.
        generation_result = self._position_table_generator.execute(
            blueprint=token_blueprint
        )
        if generation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CommonTokenPropertyTableGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CommonTokenPropertyTableGeneratorException.MSG,
                    err_code=CommonTokenPropertyTableGeneratorException.ERR_CODE,
                    ex=generation_result.exception,
                )
            )
        # --- Extract from the validation payloads. ---#
        id = cast(int, id_validation.payload)
        team = cast(Team, team_validation.payload)
        home_square = cast(HomeSquare, home_detection.payload)
        formation = cast(Formation, formation_validation.payload)
        deployment = cast(TokenDeployment, deployment_validation.payload)
        position_table = cast(TokenPositionTable, generation_result.payload)
        
        # --- Send the work product. ---#
        token_property_table = CommonTokenPropertyTable(
            id=id,
            team=team,
            formation=formation,
            home_square=home_square,
            deployment=deployment,
            position_table=position_table,
        )
        return ValidationResult.success(token_property_table)

    