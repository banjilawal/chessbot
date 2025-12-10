# src/chess/rank/validator/factory.py

"""
Module: chess.rank.validator.factory
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast

from chess.rank import (
    Bishop, BishopValidator, InvalidRankException, King, KingValidator, Knight, KnightValidator,
    NullRankException, Pawn, PawnValidator, Queen, QueenValidator, Rank, RankSpecValidator, Rook, RookValidator
)
from chess.system import LoggingLevelRouter, Validator, ValidationResult


class RankValidatorFactory(Validator[Rank]):
    """
    # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Verifies a candidate is a Rank instance that meets integrity requirements, before
        the candidate is used.

    # PROVIDES:
    ValidationResult[Rank] containing either:
        - On success: Rank in the payload.
        - On failure: Exception.

    # ATTRIBUTES:

    # CONSTRUCTOR:
    Default Constructor

    # CLASS METHODS:
        def validate(
                candidate: Any, rook_validator: RookValidator, king_validator: KingValidator,
                pawn_validator: PawnValidator, queen_validator: QueenValidator,
                knight_validator: KnightValidator, bishop_validator: BishopValidator,
        ) -> ValidationResult[Rank]: ValidationResult[(Team, Game)]:

    # INSTANCE METHODS:
        *   rank_spec_validator: RankSpecValidator
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
        1.  Check if the candidate is null. If so return an exception in a ValidationResult.
        2.  If the candidate is not a Rank instance send an exception in a ValidationResult.
        3.  Find the candidate's matching concrete rank and hand off its validation to the
            subclass validator.

        # PARAMETERS:
            *   candidate (Any)
            *   rook_validator (RookValidator)
            *   king_validator (KingValidator)
            *   pawn_validator (PawnValidator)
            *   queen_validator (QueenValidator)
            *   knight_validator (KnightValidator)
            *   bishop_validator (BishopValidator)
            
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
            # Make sure its not null first.
            if candidate is None:
                return ValidationResult.failure(
                    NullRankException(f"{method} {NullRankException.DEFAULT_MESSAGE}")
                )
            # Verify candidate is a Rank instance. Cast to a Rank if so.
            if not isinstance(candidate, Rank):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a Rank got {type(candidate).__name__} instead.")
                )
            rank = cast(Rank, candidate)
            # Pick which validator to run.
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
            
        # If the candidate is not any of the concrete Ranks control passes to the except block.
        # The unhandled exception is wrapped inside an InvalidRankException which is sent inside
        # a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidRankException(ex=ex, message=f"{method}: {InvalidRankException.DEFAULT_MESSAGE}")
            )