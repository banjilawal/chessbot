# src/assurance/validator/model/token/king/validator.py

"""
Module: assurance.validator.model.token.king.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import TokenValidatorToolkit
from domain import (
    Formation, KingToken, HomeSquare, KingTokenBlueprint, Team, TeamValidationRequest, TokenDeployment, TokenReadiness
)
from err import (
    FormationNullException, KingTokenValidatorException, NullException, TeamCarrierEmptyException,
    TokenCarrierEmptyException
)
from transit import KingTokenCarrier, TeamCarrier
from util import IdFactory, LoggingLevelRouter


class KingTokenValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TokenCarrier and its contents instance is safe before use.

    Attributes:
        toolkit: TokenValidationToolkit

    Provides:
        -   def execute(validated_carrier: KingTokenCarrier) -> ValidationResult[KingTokenCarrier]

    Super Class:
    """
    _toolkit: TokenValidatorToolkit
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidationToolkit]
        """
        self._toolkit=toolkit or TokenValidatorToolkit()
    
    @LoggingLevelRouter.monitor
    def execute(self, validated_carrier: KingTokenCarrier) -> ValidationResult[KingTokenCarrier]:
        """
        Send a validated KingToken or Blueprint which inside the validated
        KingTokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The carrier is empty.
                    - The id check fails.
                    - The team check fails.
                    - The formation is null or the wrong type.
                    - The readiness is null or the wrong type.
                    - the deployment is null or the wrong type.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            validated_carrier: KingTokenCarrier
        Returns:
            ValidationResult[KingTokenCarrier]
        Raises:
            KingTokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that there is no blueprint in the carrier.
        blueprint = validated_carrier.extract_blueprint()
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenValidatorException.MSG,
                    err_code=KingTokenValidatorException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self._toolkit.helper.blueprint_id_extractor.execute(
            candidate=blueprint,
            blueprint_owner_name=blueprint.domain_class_name,
            blueprint_type=self._toolkit.metadata.types.blueprint,
            blueprint_null_exception=self._toolkit.metadata.nulls.blueprint,
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenValidatorException.MSG,
                    err_code=KingTokenValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # Handle the case that the team does not pass a validation check.
        team_validation = self._toolkit.helper.team_validator.execute(
            request=TeamValidationRequest(
                id=IdFactory.next_id(class_name="TeamValidationRequest"),
                item=TeamCarrier(model=blueprint.team),
            )
        )
        if team_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenValidatorException.MSG,
                    err_code=KingTokenValidatorException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # Handle the case that the team_carrier does not contain a model.
        team_carrier = cast(TeamCarrier, team_validation.payload)
        if not team_carrier.is_carrying_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenValidatorException.MSG,
                    err_code=KingTokenValidatorException.ERR_CODE,
                    ex=TeamCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamCarrierEmptyException.MSG,
                        err_code=TeamCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the formation does not pass a validation check.
        formation_validation = self._toolkit.helper.priming_validator.execute(
            candidate=blueprint.formation,
            target_model=Formation,
            null_exception=FormationNullException(),
        )
        if formation_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenValidatorException.MSG,
                    err_code=KingTokenValidatorException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # Handle the case that the readiness does not pass a validation check.
        readiness_validation = self._toolkit.helper.priming_validator.execute(
            candidate=blueprint.readiness,
            target_model=TokenReadiness,
            null_exception=NullException(),
        )
        if readiness_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenValidatorException.MSG,
                    err_code=KingTokenValidatorException.ERR_CODE,
                    ex=readiness_validation.exception,
                )
            )
        # Handle the case that the deployment does not pass a validation check.
        deployment_validation = self._toolkit.helper.priming_validator.execute(
            candidate=blueprint.deployment,
            target_model=TokenReadiness,
            null_exception=NullException(),
        )
        if deployment_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenValidatorException.MSG,
                    err_code=KingTokenValidatorException.ERR_CODE,
                    ex=deployment_validation.exception,
                )
            )
        # Handle the case that the home_square gets flagged.
        home_detection = self._toolkit.helper.home_extractor.execute(
            blueprint=blueprint,
        )
        if home_detection.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                KingTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KingTokenValidatorException.MSG,
                    err_code=KingTokenValidatorException.ERR_CODE,
                    ex=home_detection.exception,
                )
            )
        # --- Extract and cast payloads of the validation results. ---#
        id = cast(int, id_validation.payload)
        team = cast(Team, team_carrier.entity)
        formation = cast(Formation, formation_validation.payload)
        home_square = cast(HomeSquare, home_detection.payload)
        readiness = cast(TokenReadiness, readiness_validation.payload)
        deployment = cast(TokenDeployment, deployment_validation.payload)
        
        # --- Extract the blueprint to verify the attributes. ---#
   
        if validated_carrier.is_carrying_model:
            model = KingToken(
                id=id,
                team=team,
                home_square=home_square,
                formation=formation,
            )
            model.readiness = readiness
            model.deployment = deployment
            model.position = blueprint.position
            model.checkmate = blueprint.checkmate
            model.check_warning = blueprint.check_warning
            model.previous_position = model.previous_position
            
            return ValidationResult.success(
                KingTokenCarrier(model=model)
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            KingTokenCarrier(blueprint=KingTokenBlueprint(
                id=id,
                team=team,
                formation=formation,
                readiness=readiness,
                deployment=deployment,
                home_square=home_square,
                position=blueprint.position,
                checkmate=blueprint.checkmate,
                check_warning=blueprint.check_warning,
                previous_position=blueprint.previous_position,
            )
        )
    
    