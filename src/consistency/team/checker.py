# src/consistency/team/consistency.py

"""
Module: consistency.team.checker
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from controller import WorkerRegistryController
from model import Team
from toolkit import TeamToolkit
from result import ValidationResult
from util import LoggingLevelRouter
from err import SchemaNullException, TeamNullException, TeamConsistencyCheckerException
from consistency import  ConsistencyChecker


class TeamConsistencyChecker(ConsistencyChecker[Team]):
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
        Consistency
    """
    OPERATION_NAME = "text_consistency"
    
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
             TeamConsistencyCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TeamToolkit()
        
        # Handle the case that, the consistency is not primed.
        consistency_priming_result = toolkit.priming_consistency.execute(
            candidate=candidate,
            target_model=Team,
            model_null_exception=TeamNullException(),
        )
        if consistency_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamConsistencyCheckerException.MSG,
                    err_code=TeamConsistencyCheckerException.ERR_CODE,
                    ex=consistency_priming_result.exception,
                )
            )
        # --- Cast the candidate into a Team for additional tests ---#
        team = cast(Team, candidate)
        
        # Handle the case that, team.id does not pass a validation check.
        id_validation_result = toolkit.identity_service.validate_id(candidate=team.id)
        if id_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamConsistencyCheckerException.MSG,
                    err_code=TeamConsistencyCheckerException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, team.schema does not pass a validation check.
        schema_validation_result = toolkit.priming_consistency.execute(
            candidate=candidate,
            target_model=Schema,
            model_null_exception=SchemaNullException(),
        )
        if schema_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamConsistencyCheckerException.MSG,
                    err_code=TeamConsistencyCheckerException.ERR_CODE,
                    ex=schema_validation_result.exception,
                )
            )
        # Handle the case that, team.owner does not pass a validation check.
        owner_validation_result = toolkit.owner_consistency.execute(team.owner)
        if owner_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamConsistencyCheckerException.MSG,
                    err_code=TeamConsistencyCheckerException.ERR_CODE,
                    ex=owner_validation_result.exception,
                )
            )
        # Handle the case that, team.board does not pass a validation check.
        board_consistency_result = toolkit.board_consistency.execute(team.board)
        if board_consistency_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamConsistencyCheckerException.MSG,
                    err_code=TeamConsistencyCheckerException.ERR_CODE,
                    ex=board_consistency_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(team)
    
# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register_worker(worker=TeamConsistency)
 