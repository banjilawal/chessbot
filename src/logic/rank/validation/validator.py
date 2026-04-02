# src/logic/rank/validation/validator.py

"""
Module: logic.rank.validation.validator
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from __future__ import annotations
from typing import cast, Any

from logic.system import LoggingLevelRouter, ValidationResult, Validator
from logic.rank import (
    NullRankException, Rank, RankIntegrityWorkers, RankPersonaValidator, RankValidationException
)



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
        -   def validate(
                    rank: Any,
                    workers: RankIntegrityWorkers,
                    persona_validator: RankPersonaValidator
            ) -> ValidationResult[Rank]:

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            workers: RankIntegrityWorkers = RankIntegrityWorkers(),
            persona_validator: RankPersonaValidator = RankPersonaValidator(),
    ) -> ValidationResult[Rank]:
        """
        Verify the rank is a Rank that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult
                    -   the rank does not exist.
                    -   the rank is not a Rank.
                    -   Any integrity worker raises a failed test.
                    -   persona_validator returns an exception.
            2.  Otherwise, after the rank is cast to a Rank, send the success result.
        Args:
            candidate: Any
            workers: RankIntegrityWorkers
            persona_validator: RankPersonaValidator
        Returns:
            ValidationResult[Rank]
        Raises:
            TypeError
            NullRankException
            RankValidationException
        """
        method = f"{cls.__name__}.validate"
        
        # Handle the case that, the rank does not exist.
        if candidate is None:
            # Return the exception on failure.
            return ValidationResult.failure(
                RankValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=RankValidationException.OP,
                    msg=RankValidationException.MSG,
                    err_code=RankValidationException.ERR_CODE,
                    rslt_type=RankValidationException.RSLT_TYPE,
                    ex=NullRankException(
                        msg=NullRankException.MSG,
                        err_code=NullRankException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the rank is the wrong type.
        if not isinstance(candidate, Rank):
            # Return the exception on failure.
            return ValidationResult.failure(
                RankValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=RankValidationException.OP,
                    msg=RankValidationException.MSG,
                    err_code=RankValidationException.ERR_CODE,
                    rslt_type=RankValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected a Rank, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast rank to a Rank for additional tests ---#
        rank = cast(Rank, candidate)
        
        # Handle the case that, the rank's id is not safe.
        id_validation_result = workers.identity_service.validate_id(rank.id)
        if id_validation_result.is_failure:
            # Return the exception on failure.
            return ValidationResult.failure(
                RankValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=RankValidationException.OP,
                    msg=RankValidationException.MSG,
                    err_code=RankValidationException.ERR_CODE,
                    rslt_type=RankValidationException.RSLT_TYPE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the rank has the wrong persona.
        rank_persona_validation = persona_validator.validate(
            rank=rank,
            persona_service=workers.persona_service
        )
        if rank_persona_validation.is_failure:
            # Return the exception on failure.
            return ValidationResult.failure(
                RankValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=RankValidationException.OP,
                    msg=RankValidationException.MSG,
                    err_code=RankValidationException.ERR_CODE,
                    rslt_type=RankValidationException.RSLT_TYPE,
                    ex=rank_persona_validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(rank)
