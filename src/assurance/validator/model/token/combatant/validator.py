# src/assurance/validator/model/token/combatant/validator.py

"""
Module: assurance.validator.model.token.combatant.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import TokenValidatorToolkit
from domain import (
    Formation, CombatantReadiness, CombatantToken, HomeSquare, CombatantBlueprint, Team, TeamValidationRequest, TokenDeployment,
    TokenReadiness
)
from err import (
    FormationNullException, CombatantTokenValidatorException, NullException, TeamCarrierEmptyException,
    TokenCarrierEmptyException
)
from transit import CombatantCarrier, TeamCarrier
from util import IdFactory, LoggingLevelRouter


class CombatantTokenValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TokenCarrier and its contents instance is safe before use.

    Attributes:
        toolkit: TokenValidationToolkit

    Provides:
        -   def execute(validated_carrier: CombatantCarrier) -> ValidationResult[CombatantCarrier]

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
    def execute(self, validated_carrier: CombatantCarrier) -> ValidationResult[CombatantCarrier]:
        """
        Send a validated CombatantToken or Blueprint which inside the validated
        CombatantCarrier.

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
            validated_carrier: CombatantCarrier
        Returns:
            ValidationResult[CombatantCarrier]
        Raises:
            CombatantTokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that there is no blueprint in the carrier.
        blueprint = validated_carrier.extract_blueprint()
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CombatantTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenValidatorException.MSG,
                    err_code=CombatantTokenValidatorException.ERR_CODE,
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
                CombatantTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenValidatorException.MSG,
                    err_code=CombatantTokenValidatorException.ERR_CODE,
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
                CombatantTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenValidatorException.MSG,
                    err_code=CombatantTokenValidatorException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # Handle the case that the team_carrier does not contain a model.
        team_carrier = cast(TeamCarrier, team_validation.payload)
        if not team_carrier.is_carrying_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CombatantTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenValidatorException.MSG,
                    err_code=CombatantTokenValidatorException.ERR_CODE,
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
                CombatantTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenValidatorException.MSG,
                    err_code=CombatantTokenValidatorException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # Handle the case that the readiness does not pass a validation check.
        readiness_validation = self._toolkit.helper.priming_validator.execute(
            candidate=blueprint.readiness,
            target_model=CombatantReadiness,
            null_exception=NullException(),
        )
        if readiness_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CombatantTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenValidatorException.MSG,
                    err_code=CombatantTokenValidatorException.ERR_CODE,
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
                CombatantTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenValidatorException.MSG,
                    err_code=CombatantTokenValidatorException.ERR_CODE,
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
                CombatantTokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CombatantTokenValidatorException.MSG,
                    err_code=CombatantTokenValidatorException.ERR_CODE,
                    ex=home_detection.exception,
                )
            )
        # --- Extract validation payloads. ---#
        id = cast(int, id_validation.payload)
        team = cast(Team, team_carrier.entity)
        home_square = cast(HomeSquare, home_detection.payload)
        formation = cast(Formation, formation_validation.payload)
        readiness = cast(CombatantReadiness, readiness_validation.payload)
        deployment = cast(TokenDeployment, deployment_validation.payload)
        
        # --- Forward the appropriate work product to the caller. ---#
        
        # The model case.
        if validated_carrier.is_carrying_model:
            model = CombatantToken(
                id=id,
                team=team,
                home_square=home_square,
                formation=formation,
            )
            model.readiness = readiness
            model.deployment = deployment
            model.captor = blueprint.captor
            model.position = blueprint.position
            model.previous_position = model.previous_position
            
            return ValidationResult.success(CombatantCarrier(model=model))
        # Else the blueprint case
        return ValidationResult.success(
            CombatantCarrier(
                blueprint=CombatantBlueprint(
                    id=id,
                    team=team,
                    formation=formation,
                    readiness=readiness,
                    deployment=deployment,
                    home_square=home_square,
                    captor=blueprint.captor,
                    position=blueprint.position,
                    previous_position=blueprint.previous_position,
            )
        )
    )
    
    