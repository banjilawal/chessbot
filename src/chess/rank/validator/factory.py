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
    Rank, King, Queen, Rook, Bishop, Knight, Pawn, RankIdValidator, RankLetterValidator, RankNameValidator,
    RankQuotaValidator, RankRansomValidator, NullRankException, InvalidRankException
)


class RankValidatorFactory(Validator[Rank]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            rank_id_validator: type[RankIdValidator]=RankIdValidator,
            rank_name_validator: type[RankNameValidator]=RankNameValidator,
            rank_letter_validator: type[RankLetterValidator]=RankLetterValidator,
            rank_quota_validator: type[RankQuotaValidator]=RankQuotaValidator,
            rank_ransom_validator: type[RankRansomValidator]=RankRansomValidator
    ) -> ValidationResult[Rank]:
        """"""
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
                        f"{method}: Expected a Rank got {type(candidate).__name__} instead."
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
                
            id_validation = rank_id_validator.validate(rank=rank, candidate=rank.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            name_validation = rank_name_validator.validate(rank=rank, candidate=rank.name)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            
            letter_validation = rank_letter_validator.validate(rank=rank, candidate=rank.letter)
            if letter_validation.is_failure():
                return ValidationResult.failure(letter_validation.exception)
            
            ransom_validation = rank_ransom_validator.validate(rank=rank, candidate=rank.ransom)
            if ransom_validation.is_failure():
                return ValidationResult.failure(ransom_validation.exception)
            
            quota_validation = rank_quota_validator.validate(rank=rank, candidate=rank.ransom)
            if quota_validation.is_failure():
                return ValidationResult.failure(quota_validation.exception)
            
        except Exception as ex:
            return ValidationResult.failure(
                InvalidRankException(
                    f"{method}: {InvalidRankException.DEFAULT_MESSAGE}",
                    ex
                )
            )