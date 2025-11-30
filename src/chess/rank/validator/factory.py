# src/chess/rank/validator/factory.py

"""
Module: chess.rank.validator.factory
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast

from chess.rank import (
    Bishop, BishopValidator, InvalidRankException, King, KingValidator, Knight, KnightValidator, NullRankException,
    Pawn, PawnValidator,
    Queen,
    QueenValidator,
    Rank,
    Rook, RookValidator
)
from chess.system import LoggingLevelRouter, Validator, ValidationResult


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
            rook_validator: RookValidator = RookValidator(),
            king_validator: KingValidator = KingValidator(),
            pawn_validator: PawnValidator = PawnValidator(),
            queen_validator: QueenValidator = QueenValidator(),
            knight_validator: KnightValidator = KnightValidator(),
            bishop_validator: BishopValidator = BishopValidator(),
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
                    NullRankException(f"{method} {NullRankException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Rank):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a Rank got {type(candidate).__name__} instead.")
                )
            rank = cast(Rank, candidate)
            
            if isinstance(candidate, King):
                return king_validator.validate(rank)
            if isinstance(candidate, Queen):
                return queen_validator.validate(rank)
            if isinstance(candidate, Rook):
                return rook_validator.validate(rank)
            if isinstance(candidate, Bishop):
                return bishop_validator.validate(rank)
            if isinstance(candidate, Knight):
                return knight_validator.validate(rank)
            if isinstance(candidate, Pawn):
                return pawn_validator.validate(rank)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidRankException(ex=ex, message=f"{method}: {InvalidRankException.DEFAULT_MESSAGE}")
            )