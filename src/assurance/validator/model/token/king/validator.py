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
from domain import KingTokenBlueprint, KingToken, HomeSquare, Rank
from transit import KingTokenCarrier
from util import LoggingLevelRouter


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
    def execute(self, carrier: KingTokenCarrier) -> ValidationResult[KingTokenCarrier]:
        """
        Send a validated KingToken or Blueprint which inside the validated
        KingTokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The candidate is not a TokenCarrier or its null.
                    - The candidate is an empty TokenCarrier.
                    - Any Token attribute is flagged.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            carrier: KingTokenCarrier
        Returns:
            ValidationResult[KingTokenCarrier]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that there is no blueprint.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that any id in the blueprint is flagged.
        id_test = self.toolkit.helper.blueprint_id_extractor.execute(
            candidate=blueprint,
            blueprint_owner_name=blueprint.domain_class_name,
            blueprint_type=self.toolkit.metadata.types.blueprint,
            blueprint_null_exception=self.toolkit.metadata.nulls.blueprint,
        )
        if id_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=id_test.exception,
                )
            )
        # Handle the case that the team does not pass a validation check.
        team_test = self.toolkit.helper.team_validator.execute(
            request=TeamValidationRequest(
                id=IdFactory.next_id(class_name="TeamValidationRequest"),
                item=TeamCarrier(model=blueprint.team),
            )
        )
        if team_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=team_test.exception,
                )
            )
        team_carrier = cast(TeamCarrier, team_test.payload)
        
        # Handle the case that the formation does not pass a validation check.
        formation_test = self.toolkit.helper.priming_validator.execute(
            candidate=blueprint.formation,
            target_model=Formation,
            null_exception=FormationNullException(),
        )
        if formation_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=formation_test.exception,
                )
            )
        # Handle the case that the home_square gets flagged.
        home_detection = self.toolkit.helper.home_extractor.execute(
            blueprint=blueprint,
        )
        if home_detection.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=home_detection.exception,
                )
            )
        
        # --- Extract and cast payloads of the validation results. ---#
        id = cast(int, id_test.payload)
        team = cast(Team, team_carrier.entity)
        formation = cast(Formation, formation_test.payload)
        home_square = cast(HomeSquare, home_detection.payload)
        # --- Extract the blueprint to verify the attributes. ---#
        blueprint = cast(KingTokenBlueprint, validated_carrier.extract_blueprint())

        if validated_carrier.is_carrying_model:
            model = KingToken(
                id=id,
                team=blueprint.team,
                home_square=home_square,
                formation=blueprint.formation,
            )
            model.position = blueprint.position
            model.checkmate = blueprint.checkmate
            model.readiness = blueprint.readiness
            model.deployment = blueprint.deployment
            model.check_warning = blueprint.check_warning
            model.previous_position = model.previous_position
            
            return ValidationResult.success(
                KingTokenCarrier(model=model)
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            KingTokenCarrier(blueprint=blueprint)
        )
    
    