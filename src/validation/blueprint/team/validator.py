# src/validation/blueprint/team/validator.py

"""
Module: validation.blueprint.team.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from model import Schema, TeamBlueprint
from result import ValidationResult
from toolkit import TeamBlueprintToolkit
from util import LoggingLevelRouter
from err import SchemaNullException, TeamBlueprintValidationException, TeamBlueprintValidationRouteException
from validation import BlueprintValidator


class TeamBlueprintValidator(BlueprintValidator[Team]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a TeamBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    toolkit: TeamBlueprintToolkit,
            ) -> ValidationResult[Team]:

    Super Class:
        BlueprintValidator
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            toolkit: TeamBlueprintToolkit | None = None,
    ) -> ValidationResult[Team]:
        """
        Certify a candidate is a TeamBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Validation is not primed.
                    -   The enabled attribute fails a safety check.
                    -   There is no validation path for the attribute.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
            toolkit: TeamBlueprintToolkit,
        Returns:
            ValidationResult[Team]
        Raises:
            TeamBlueprintValidationException
            TeamBlueprintValidationRouteException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TeamBlueprintToolkit()
        
        # Handle the case that, the validator is not primed.
        priming_result = toolkit.blueprint_priming_validator.build(
            candidate=candidate,
            blueprint_model=toolkit.blueprint_model_type,
            blueprint_null_exception=toolkit.null_blueprint_exception,
            validator_bootstrapper=toolkit.team_toolkit.priming_validator
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBlueprintValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TeamBlueprintValidationException.MSG,
                    err_code=TeamBlueprintValidationException.ERR_CODE,
                    ex=priming_result.exception
                )
            )
        # --- Cast the candidate into TeamBlueprint for routing attribute testing ---#
        blueprint = cast(TeamBlueprint, candidate)
        
        # Certification for the search-by-id target.
        if blueprint.id is not None:
            validation_result = toolkit.team_toolkit.identity_service.validate_id(
                candidate=blueprint.id
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamBlueprintValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TeamBlueprintValidationException.MSG,
                        err_code=TeamBlueprintValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(blueprint)
        
        # Certification for the search-by-owner target.
        if blueprint.owner is not None:
            validation_result = toolkit.team_toolkit.player_validator.execute(
                candidate=blueprint.owner
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamBlueprintValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TeamBlueprintValidationException.MSG,
                        err_code=TeamBlueprintValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(blueprint)
        
        # Certification for the search-by-board target.
        if blueprint.board is not None:
            validation_result = toolkit.team_toolkit.board_validator.execute(
                candidate=blueprint.board
            )
            if validation_result.is_failure:
                if validation_result.is_failure:
                    # Send the exception chain on failure.
                    return ValidationResult.failure(
                        TeamBlueprintValidationException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=TeamBlueprintValidationException.MSG,
                            err_code=TeamBlueprintValidationException.ERR_CODE,
                            ex=validation_result.exception
                        )
                    )
                # On validation success forward the work product to the caller.
                return ValidationResult.success(blueprint)
        
        # Certification for the search-by-color target.
        if blueprint.schema is not None:
            validation_result = toolkit.team_toolkit.priming_validator.execute(
                candidate=blueprint.schema,
                model_type=Schema,
                null_exception=SchemaNullException()
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamBlueprintValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TeamBlueprintValidationException.MSG,
                        err_code=TeamBlueprintValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(blueprint)
        
        # Return the exception chain if there is no validation route for the blueprint.
        return ValidationResult.failure(
            TeamBlueprintValidationException(
                cls_mthd=method,
                cls_name=cls.__name__,
                msg=TeamBlueprintValidationException.MSG,
                err_code=TeamBlueprintValidationException.ERR_CODE,
                ex=TeamBlueprintValidationRouteException(
                    msg=TeamBlueprintValidationRouteException.MSG,
                    err_code=TeamBlueprintValidationRouteException.ERR_CODE,
                )
            )
        )
