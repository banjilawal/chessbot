# src/chess/rank/validator/factory.py

"""
Module: chess.rank.validator.factory
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast

from chess.system import LoggingLevelRouter, Validator, ValidationResult
from chess.rank import (
    Rank, King, Queen, Rook, Bishop, Knight, Pawn, RankIdValidator, RankNameValidator, RankQuotaValidator,
    RankRansomValidator, NullRankException, InvalidRankException, RankDesignationValidator
)


class RankValidatorFactory(Validator[Rank]):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    Verifies a candidate is an instance of Rank, that meets integrity requirements, before the candidate is used.

    # PROVIDES:
    ValidationResult[Rank] containing either:
        - On success: Rank in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    No attributes
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            id_validator: type[RankIdValidator] = RankIdValidator,
            name_validator: type[RankNameValidator] = RankNameValidator,
            quota_validator: type[RankQuotaValidator] = RankQuotaValidator,
            ransom_validator: type[RankRansomValidator] = RankRansomValidator,
            designation_validator: type[RankDesignationValidator] = RankDesignationValidator,
    ) -> ValidationResult[Rank]:
        """
        # ACTION:
        1.  Check candidate is not validation.
        2.  Check if candidate is a Rank.
        3.  Cast to candidate to its subclass.
        4.  Validate
                *   id      ->  with id_validator
                *   name    ->  with name_validator
                *   designation  ->  with designation_validator
                *   team_quota   ->  with quota_validator
                *   ransom  ->  with ransom_validator
        5.  If any check fails, return the exception inside a ValidationResult.
        6.  When all checks pass return the Rank instance inside a ValidationResult.

        # PARAMETERS:
            *   candidate (Any): Object to validate.
            *   id_validator (type[RankIdValidator]=RankIdValidator)
            *   name_validator (type[RankNameValidator]=RankNameValidator)
            *   designation_validator (type[RankLetterValidator]=RankLetterValidator)
            *   quota_validator (type[RankQuotaValidator]=RankQuotaValidator)
            *   ransom_validator (type[RankRansomValidator]=RankRansomValidator)

        # Returns:
        ValidationResult[Rank] containing either:
            - On success: Rank in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NullRankException
            *   InvalidRankException
        """
        method = "RankValidatorFactory.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullRankException(
                        f"{method} {NullRankException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, Rank):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Expected a Rank got {type(candidate).__name__} instead."
                    )
                )
            
            rank = cast(Rank, candidate)
            
            if isinstance(candidate, King):
                rank = cast(King, candidate)
            if isinstance(candidate, Queen):
                rank = cast(Queen, candidate)
            if isinstance(candidate, Rook):
                rank = cast(Rook, candidate)
            if isinstance(candidate, Bishop):
                rank = cast(Bishop, candidate)
            if isinstance(candidate, Knight):
                rank = cast(Knight, candidate)
            if isinstance(candidate, Pawn):
                rank = cast(Pawn, candidate)
            
            id_validation = id_validator.validate(rank=rank, candidate=rank.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            name_validation = name_validator.validate(rank=rank, candidate=rank.name)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            
            designation_validation = designation_validator.validate(rank=rank, candidate=rank.designation)
            if designation_validation.is_failure():
                return ValidationResult.failure(designation_validation.exception)
            
            ransom_validation = ransom_validator.validate(rank=rank, candidate=rank.ransom)
            if ransom_validation.is_failure():
                return ValidationResult.failure(ransom_validation.exception)
            
            quota_validation = quota_validator.validate(rank=rank, candidate=rank.ransom)
            if quota_validation.is_failure():
                return ValidationResult.failure(quota_validation.exception)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidRankException(
                    ex=ex,
                    message=f"{method}: "
                            f"{InvalidRankException.DEFAULT_MESSAGE}",
                )
            )
