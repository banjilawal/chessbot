# src/chess/rank/validator/designation/validator.py

"""
Module: chess.rank.validator.designation.validator
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast, Tuple

from chess.system import IdentityService, LoggingLevelRouter, ValidationResult
from chess.rank import (
    Rank, King, Queen, Bishop, Rook, Knight, Pawn, RankSpec, RankLetterException, RankLetterOutOfBoundsException,
    KingLetterException, QueenLetterException, RookLetterException, BishopLetterException, KnightLetterException,
    PawnLetterException,
)


class RankLetterValidator:
    """
    # ROLE: Validation, Data Integrity.

    # RESPONSIBILITIES:
    Verifies the candidate is consistent with the designation attribute for a Rank is
        *   Not null.
        *   A valid Rank subclass.

    # PROVIDES:
    ValidationResult[Rank, int] containing either:
        - On success: (Rank, int) tuple in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    No attributes
    """
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def validate(
            cls,
            rank: Rank,
            candidate: Any,
            identity_service: type[IdentityService] = IdentityService
    ) -> ValidationResult[Rank, str]:
        """
        # ACTION:
        1.  Use identity_service to verify basic designation safety.
        2.  Check the candidate exists in the set of letters in RankSpec.
        3.  Verify the number matches the RankSpec value for rank param.
        4.  If any check fails, return the exception inside a ValidationResult.
        3.  When all checks pass return a tuple of rank, number. inside a ValidationResult.

        # PARAMETERS:
            *   rank (Rank): an appropriate, not null subclass instance.
            *   candidate (Any): object to validate as the correct designation for the rank.
            *   identity_service (type[IdentityService]): has default value, does basic designation safety checks.

        # Returns:
        ValidationResult[tuple(Rank, str)] containing either:
            - On success: tuple(Rank,str) in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NUllRankLetterException
            *   RankLetterBelowBoundsException
            *   RankLetterAboveBoundsException
            *   KingLetterException
            *   QueenLetterException
            *   BishopLetterException
            *   RookLetterException
            *   KnightLetterException
            *   PawnLetterException
            *   RankLetterException
        """
        method = "RankLetterValidator.validate"
        
        try:
            letter_validation = identity_service.validate_letter(candidate)
            if letter_validation.is_failure():
                return ValidationResult.failure(letter_validation.exception)
            
            letter = cast(candidate, str)
            
            letter = cast(str, candidate)
            
            if letter.upper() not in ["K", "Q", "B", "R", "N", "P"]:
                return ValidationResult.failure(
                    RankLetterOutOfBoundsException(
                        f"{method}: {RankLetterOutOfBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if isinstance(rank, King) and letter.upper() != RankSpec.KING.designation.upper():
                return ValidationResult.failure(
                    WrongKingLetterException(f"{method}: {WrongKingLetterException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Queen) and letter.upper() != RankSpec.QUEEN.designation.upper():
                return ValidationResult.failure(
                    WrongQueenLetterException(f"{method}: {WrongQueenLetterException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Bishop) and letter.upper() != RankSpec.BISHOP.designation.upper():
                return ValidationResult.failure(
                    WrongBishopLetterException(f"{method}: {WrongBishopLetterException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Rook) and letter.upper() != RankSpec.ROOK.designation.upper():
                return ValidationResult.failure(
                    WrongRookLetterException(f"{method}: {WrongRookLetterException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Knight) and letter.upper() != RankSpec.KNIGHT.designation.upper():
                return ValidationResult.failure(
                    WrongKnightLetterException(f"{method}: {WrongKnightLetterException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Pawn) and letter.upper() != RankSpec.PAWN.designation.upper():
                return ValidationResult.failure(
                    WrongPawnLetterException(f"{method}: {WrongPawnLetterException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(letter)
        
        except Exception as ex:
            return ValidationResult.failure(
                RankLetterInconsistencyException(
                    f"{method}: {RankLetterInconsisitencyException.DEFAULT_MESSAGE}"
                )
            )