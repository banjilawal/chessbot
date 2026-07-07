# src/validator/team/validator.py

"""
Module: validator.team.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from controller import WorkerRegistryController
from model import Schema, Team
from toolkit import TeamToolkit
from operation import Validator
from result import ValidationResult
from util import LoggingLevelRouter
from err import SchemaNullException, TeamNullException, TeamValidationException


class TeamValidator(Validator[Team]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Team instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(candidate: Any, toolkit: TeamToolkit) -> ValidationResult[Team]:

    Super Class:
        Validator
    """
    OPERATION_NAME = "text_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: TeamToolkit | None = None,
    ) -> ValidationResult[Team]:
        """
        Verify the object is a Team that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult any of the cases occur:
                    -   Candidate is null
                    -   It's not a number.
                    _   A Team check fails
                    -   A Rank check fails
                    -   Identity check fails
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            toolkit: TeamToolkit
        Returns:
            ValidationResult[Team]
        Raises:
             TeamValidationException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TeamToolkit()
        
        # Handle the case that, the validator is not primed.
        validator_priming_result = toolkit.priming_validator.run(
            candidate=candidate,
            context_model=Team,
            null_exception=TeamNullException(),
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TeamValidationException.MSG,
                    err_code=TeamValidationException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        # --- Cast the candidate into a Team for additional tests ---#
        team = cast(Team, candidate)
        
        # Handle the case that, team.id does not pass a validation check.
        id_validation_result = toolkit.identity_service.validate_id(candidate=team.id)
        if id_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TeamValidationException.MSG,
                    err_code=TeamValidationException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, team.schema does not pass a validation check.
        schema_validation_result = toolkit.priming_validator.run(
            candidate=candidate,
            context_model=Schema,
            null_exception=SchemaNullException(),
        )
        if schema_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TeamValidationException.MSG,
                    err_code=TeamValidationException.ERR_CODE,
                    ex=schema_validation_result.exception,
                )
            )
        # Handle the case that, team.owner does not pass a validation check.
        owner_validation_result = toolkit.owner_validator.build(team.owner)
        if owner_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TeamValidationException.MSG,
                    err_code=TeamValidationException.ERR_CODE,
                    ex=owner_validation_result.exception,
                )
            )
        # Handle the case that, team.board does not pass a validation check.
        board_validation_result = toolkit.board_validator.validate(team.board)
        if board_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TeamValidationException.MSG,
                    err_code=TeamValidationException.ERR_CODE,
                    ex=board_validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(team)
    
# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register_worker(worker=TeamValidator)
 