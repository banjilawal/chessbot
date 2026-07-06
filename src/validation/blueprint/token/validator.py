# src/validation/blueprint/token/validator.py

"""
Module: validation.blueprint.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from blueprint import TokenBlueprint
from schema import Formation
from context import TokenHomeContext
from err import FormationNullException, TokenBlueprintValidatorException
from model import HomeSquare
from result import ValidationResult
from toolkit import TokenToolkit

from util import LoggingLevelRouter
from validation import Validator


class TokenBlueprintValidator(Validator[TokenBlueprint]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a TokenBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    toolkit: TokenBlueprintToolkit,
            ) -> ValidationResult:

    Super Class:
        BlueprintValidator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            toolkit: TokenToolkit | None = None
    ) -> ValidationResult[TokenBlueprint]:
        """
        Verify a TokenBlueprint and fill before its used.

        Action:
            1.  Send an exception chain in the ValidationResult if any following occurs:
                    -   A blueprint attribute gets flagged by a validator.
                    -   The opening square is not found.
                    -   The Rank is not built successfully.
                    -   Any blueprint values have already been used in the team.
            2.  Otherwise ,create a new Blueprint including the Rank and OpeningSquare.
            2.  Send the success result.
        Args:
            candidate: Any
            toolkit: TokenToolkit
        Returns:
            ValidationResult[Blueprint]
        Raises:
            PrimingTokenAssemblyException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TokenToolkit()
        
        # Handle the case that, the validator is not primed.
        validator_priming_result = toolkit.priming_validator.execute(
            candidate=candidate,
            target_=toolkit.blueprint_model,
            null_exception=toolkit.blueprint_null_execption,
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        # --- Cast the candidate into a TokenBlueprint for additional tests. ---#
        blueprint = cast(toolkit.blueprint_model, candidate)
        
        # Handle the case that, any id in the blueprint is flagged.
        id_validation_result = toolkit.blueprint_id_validator.execute(
            candidate=blueprint.id,
            identity_service=toolkit.identity_service,
        )
        if id_validation_result.is_failure:
        # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the team does not pass a validation check.
        team_validation = toolkit.team_validator.validate(
            candidate=blueprint.team
        )
        if team_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # Handle the case that, the formation does not pass a validation check.
        formation_validation = toolkit.priming_validator.execute(
            candidate=blueprint.formation,
            target_model=Type[Formation],
            null_exception=FormationNullException(),
        )
        if formation_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # Handle the case that, the home_square gets flagged.
        home_detection_result = toolkit.home_detector.execute(
            context=TokenHomeContext(
                board=blueprint.team.board,
                square_name=blueprint.formation.home_square_name,
            ),
        )
        if home_detection_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=home_detection_result.exception,
                )
            )
        # Handle the case that, the rank is not safe to use.
        rank_validation_result = toolkit.blueprint_rank_processor.execute(
            blueprint=blueprint,
            toolkit=toolkit,
        )
        if rank_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=rank_validation_result.exception,
                )
            )
        # --- Completed validations successfully. Extract the payloads to build a new blueprint. ---#
        rank = rank_validation_result.payload
        id = cast(int, id_validation_result.payload)
        home_square = cast(HomeSquare, home_detection_result.payload)
        
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            TokenBlueprint(
                id=id,
                rank=rank,
                team=blueprint.team,
                formation=blueprint.formation,
                home_square=home_square,
            )
        )