# src/validation/context/team/operation.py

"""
Module: validation.context.team.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import SchemaNullException, TeamContextValidationException
from model import Schema, TeamContext
from result import ValidationResult
from toolkit.build.context.team.builder import TeamContextToolkit
from util import LoggingLevelRouter
from validation import Validator


class TeamContextValidator(Validator[TeamContext]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a TeamContext instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception returned to the caller.

    Super Class:
        *   Validator

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: TeamContextToolkit | None = None,
    ) -> ValidationResult[TeamContext]:
        """
        # ACTION:
            1.  If the rank fails existence or type tests send the exception in the ValidationResult.
                Else, cast to TeamContext instance context.
            2.  If one-and-only-one context attribute is not null return an exception in the ValidationResult.
            3.  If there is no certification route for the attribute return an exception in the ValidationResult.
            4.  If the certification route exists use the appropriate service or validation to send either an exception
                chain the ValidationResult or the context.
        # PARAMETERS:
            *   rank (Any)
            *   color_validator (ColorValidator)
            *   player_service (PlayerService)
            *   board_service (BoardService)
            *   identity_service (IdentityService)
        # RETURNS:
            *   ValidationResult[TeamContext] containing either:
                    - On failure: Exception.
                    - On success: TeamContext in the payload.
        Raises:
            *   TypeError
            *   NullTeamContextException
            *   ZeroTeamContextFlagsException
            *   BoardTeamContextFlagsException
            *   TeamContextValidationException
            *   TeamContextValidationRouteException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TeamContextToolkit()
        
        # handle the case that, priming the validator fails.
        priming_result = toolkit.context_validation_primer.validate(
            candidate=candidate,
            context_model=toolkit.context_model_type,
            null_exception=toolkit.null_context_exception,
            validator_bootstrapper=toolkit.token_toolkit.validation_bootstrap
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TeamContextValidationException.MSG,
                    err_code=TeamContextValidationException.ERR_CODE,
                    ex=priming_result.exception
                )
            )
        # --- Cast the candidate into TeamContext for routing attribute testing ---#
        context = cast(TeamContext, candidate)
        
        # Certification for the search-by-id target.
        if context.id is not None:
            validation_result = toolkit.team_toolkit.identity_service.validate_id(
                candidate=context.id
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TeamContextValidationException.MSG,
                        err_code=TeamContextValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-owner target.
        if context.owner is not None:
            validation_result = toolkit.team_toolkit.player_service.validator.validate(
                candidate=context.owner
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TeamContextValidationException.MSG,
                        err_code=TeamContextValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-board target.
        if context.board is not None:
            validation_result = toolkit.team_toolkit.board_validator.validate(
                candidate=context.board
            )
            if validation_result.is_failure:
                if validation_result.is_failure:
                    # Send the exception chain on failure.
                    return ValidationResult.failure(
                        TeamContextValidationException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=TeamContextValidationException.MSG,
                            err_code=TeamContextValidationException.ERR_CODE,
                            ex=validation_result.exception
                        )
                    )
                # On validation success forward the work product to the caller.
                return ValidationResult.success(context)
        
        # Certification for the search-by-color target.
        if context.schema is not None:
            validation_result = toolkit.token_toolkit.validation_bootstrap.validate(
                candidate=context.schema,
                model_type=Schema,
                null_exception=SchemaNullException()
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TeamContextValidationException.MSG,
                        err_code=TeamContextValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Return the exception chain if there is no validation route for the context.
        return ValidationResult.failure(
            TeamContextValidationException(
                msg=f"{method}: {TeamContextValidationException.ERR_CODE}",
                ex=TeamContextValidationRouteException(
                    f"{method}: {TeamContextValidationRouteException.MSG}"
                )
            )
        )