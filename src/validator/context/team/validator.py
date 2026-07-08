# src/validator/context/team/validator.py

"""
Module: validator.context.team.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from model import Schema, TeamContext
from result import ValidationResult
from toolkit import TeamContextToolkit
from util import LoggingLevelRouter
from err import SchemaNullException, TeamContextValidatorException, TeamContextValidationRouteException
from validator import ContextValidator


class TeamContextValidator(ContextValidator[Team]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a TeamContext instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    toolkit: TeamContextToolkit,
            ) -> ValidationResult[Team]:

    Super Class:
        ContextValidator
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            toolkit: TeamContextToolkit | None = None,
    ) -> ValidationResult[Team]:
        """
        Certify a candidate is a TeamContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Validation is not primed.
                    -   The enabled attribute fails a safety check.
                    -   There is no validation path for the attribute.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
            toolkit: TeamContextToolkit,
        Returns:
            ValidationResult[Team]
        Raises:
            TeamContextValidatorException
            TeamContextValidationRouteException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TeamContextToolkit()
        
        # Handle the case that, the validator is not primed.
        priming_result = toolkit.context_priming_validator.build(
            candidate=candidate,
            context_model=toolkit.context_model_type,
            context_null_exception=toolkit.null_context_exception,
            validator_bootstrapper=toolkit.team_toolkit.priming_validator
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamContextValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TeamContextValidatorException.MSG,
                    err_code=TeamContextValidatorException.ERR_CODE,
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
                    TeamContextValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TeamContextValidatorException.MSG,
                        err_code=TeamContextValidatorException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-owner target.
        if context.owner is not None:
            validation_result = toolkit.team_toolkit.player_validator.execute(
                candidate=context.owner
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamContextValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TeamContextValidatorException.MSG,
                        err_code=TeamContextValidatorException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-board target.
        if context.board is not None:
            validation_result = toolkit.team_toolkit.board_validator.execute(
                candidate=context.board
            )
            if validation_result.is_failure:
                if validation_result.is_failure:
                    # Send the exception chain on failure.
                    return ValidationResult.failure(
                        TeamContextValidatorException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=TeamContextValidatorException.MSG,
                            err_code=TeamContextValidatorException.ERR_CODE,
                            ex=validation_result.exception
                        )
                    )
                # On validation success forward the work product to the caller.
                return ValidationResult.success(context)
        
        # Certification for the search-by-color target.
        if context.schema is not None:
            validation_result = toolkit.team_toolkit.priming_validator.execute(
                candidate=context.schema,
                model_type=Schema,
                null_exception=SchemaNullException()
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamContextValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TeamContextValidatorException.MSG,
                        err_code=TeamContextValidatorException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Return the exception chain if there is no validation route for the context.
        return ValidationResult.failure(
            TeamContextValidatorException(
                cls_mthd=method,
                cls_name=cls.__name__,
                msg=TeamContextValidatorException.MSG,
                err_code=TeamContextValidatorException.ERR_CODE,
                ex=TeamContextValidationRouteException(
                    msg=TeamContextValidationRouteException.MSG,
                    err_code=TeamContextValidationRouteException.ERR_CODE,
                )
            )
        )
