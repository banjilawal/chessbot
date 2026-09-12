# src/assurance/validator/model/player/human/validator.py

"""
Module: assurance.validator.model.player.human.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import PlayerValidatorToolkit
from domain import (
    Formation, HumanReadiness, HumanPlayer, HomeSquare, HumanPlayerBlueprint, Team, TeamValidationRequest, PlayerDeployment,
    PlayerReadiness
)
from err import (
    FormationNullException, HumanPlayerValidatorException, NullException, TeamCarrierEmptyException,
    PlayerCarrierEmptyException
)
from transit import HumanPlayerCarrier, TeamCarrier
from util import IdFactory, LoggingLevelRouter


class HumanPlayerValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a PlayerCarrier and its contents instance is safe before use.

    Attributes:
        toolkit: PlayerValidationToolkit

    Provides:
        -   def execute(validated_carrier: HumanPlayerCarrier) -> ValidationResult[HumanPlayerCarrier]

    Super Class:
    """
    _toolkit: PlayerValidatorToolkit
    
    def __init__(
            self,
            toolkit: Optional[PlayerValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[PlayerValidationToolkit]
        """
        self._toolkit=toolkit or PlayerValidatorToolkit()
    
    @LoggingLevelRouter.monitor
    def execute(self, validated_carrier: HumanPlayerCarrier) -> ValidationResult[HumanPlayerCarrier]:
        """
        Send a validated HumanPlayer or Blueprint which inside the validated
        HumanPlayerCarrier.

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
            validated_carrier: HumanPlayerCarrier
        Returns:
            ValidationResult[HumanPlayerCarrier]
        Raises:
            HumanPlayerValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that there is no blueprint in the carrier.
        blueprint = validated_carrier.extract_blueprint()
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HumanPlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanPlayerValidatorException.MSG,
                    err_code=HumanPlayerValidatorException.ERR_CODE,
                    ex=PlayerCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerCarrierEmptyException.MSG,
                        err_code=PlayerCarrierEmptyException.ERR_CODE,
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
                HumanPlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanPlayerValidatorException.MSG,
                    err_code=HumanPlayerValidatorException.ERR_CODE,
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
                HumanPlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanPlayerValidatorException.MSG,
                    err_code=HumanPlayerValidatorException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # Handle the case that the team_carrier does not contain a model.
        team_carrier = cast(TeamCarrier, team_validation.payload)
        if not team_carrier.is_carrying_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HumanPlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanPlayerValidatorException.MSG,
                    err_code=HumanPlayerValidatorException.ERR_CODE,
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
                HumanPlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanPlayerValidatorException.MSG,
                    err_code=HumanPlayerValidatorException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # Handle the case that the readiness does not pass a validation check.
        readiness_validation = self._toolkit.helper.priming_validator.execute(
            candidate=blueprint.readiness,
            target_model=HumanReadiness,
            null_exception=NullException(),
        )
        if readiness_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HumanPlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanPlayerValidatorException.MSG,
                    err_code=HumanPlayerValidatorException.ERR_CODE,
                    ex=readiness_validation.exception,
                )
            )
        # Handle the case that the deployment does not pass a validation check.
        deployment_validation = self._toolkit.helper.priming_validator.execute(
            candidate=blueprint.deployment,
            target_model=PlayerReadiness,
            null_exception=NullException(),
        )
        if deployment_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                HumanPlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanPlayerValidatorException.MSG,
                    err_code=HumanPlayerValidatorException.ERR_CODE,
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
                HumanPlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HumanPlayerValidatorException.MSG,
                    err_code=HumanPlayerValidatorException.ERR_CODE,
                    ex=home_detection.exception,
                )
            )
        # --- Extract validation payloads. ---#
        id = cast(int, id_validation.payload)
        team = cast(Team, team_carrier.entity)
        home_square = cast(HomeSquare, home_detection.payload)
        formation = cast(Formation, formation_validation.payload)
        readiness = cast(HumanReadiness, readiness_validation.payload)
        deployment = cast(PlayerDeployment, deployment_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        
        # The model case.
        if validated_carrier.is_carrying_model:
            model = HumanPlayer(
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
            
            return ValidationResult.success(HumanPlayerCarrier(model=model))
        # Else the blueprint case
        return ValidationResult.success(
            HumanPlayerCarrier(
                blueprint=HumanPlayerBlueprint(
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
    )
    
    