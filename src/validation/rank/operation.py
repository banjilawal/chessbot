# src/operation/validation/rank/operation.py

"""
Module: operation.validation.rank.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from model import Persona, Rank
from toolkit import RankToolkit
from operation import Validator
from result import ValidationResult
from util import LoggingLevelRouter
from err import PersonaNullException, RankNullException, RankValidationException


class RankValidator(Validator[Rank]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Rank instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(candidate: Any, toolkit: RankToolkit) -> ValidationResult[Rank]:

    Super Class:
        Validator
    """
    OPERATION_NAME = "rank_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: RankToolkit | None = None,
    ) -> ValidationResult[Rank]:
        """
        Verify the object is a Rank that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult any of the cases occur:
                    -   Candidate either null or not a Rank.
                    _   Its absolute value is > BOARD_DIMENSION.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            toolkit: RankToolkit
        Returns:
            ValidationResult[Rank]
        Raises:
             RankValidationException
        """
        method = f"{cls.__name__}.validate"
        
        if toolkit is None:
            toolkit = RankToolkit()
        
        # Handle the case that, the candidate does not exist.
        validation_bootstrap_result = toolkit.validation_bootstrapper.validate(
            candidate=candidate,
            target_model=Rank,
            null_exception=RankNullException(),
        )
        if validation_bootstrap_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=RankValidationException.MSG,
                    err_code=RankValidationException.ERR_CODE,
                    ex=validation_bootstrap_result.exception,
                )
            )
        # --- Cast candidate to a Rank for additional tests. ---#
        rank = cast(Rank, candidate)
        
        # Handle the case that, the rank's id is not safe.
        id_validation_result = toolkit.identity_service.validate_id(rank.id)
        if id_validation_result.is_failure:
            # Return the exception on failure.
            return ValidationResult.failure(
                RankValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=RankValidationException.MSG,
                    err_code=RankValidationException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the rank has the wrong persona.
        rank_persona_validation_result = toolkit.validation_bootstrapper.validate(
            candidate=rank.persona,
            target_model=Persona,
            null_exception=PersonaNullException(),
        )
        if rank_persona_validation_result.is_failure:
            # Return the exception on failure.
            return ValidationResult.failure(
                RankValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=RankValidationException.MSG,
                    err_code=RankValidationException.ERR_CODE,
                    ex=rank_persona_validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(rank)
