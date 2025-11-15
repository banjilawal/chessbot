# src/chess/rank/validator/name/validator.py

"""
Module: chess.rank.validator.name.validator
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast, Tuple

from chess.system import IdentityService, LoggingLevelRouter, ValidationResult
from chess.rank import (
    Rank, King, Queen, Bishop, Rook, Knight, Pawn, RankSpec, RankNameException, RankNameOutOfBoundsException,
    KingNameException, QueenNameException, RookNameException, BishopNameException, KnightNameException,
    PawnNameException,
)


class RankNameValidator:
    """
    # ROLE: Validation, Data Integrity.

    # RESPONSIBILITIES:
    Verifies the candidate is consistent with the name attribute for a Rank is
        *   Not null.
        *   A valid Rank subclass.

    # PROVIDES:
    ValidationResult[Rank, int] containing either:
        - On success: (Rank, int) tuple in payload.
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
            identity_service: type[IdentityService]=IdentityService
    ) -> ValidationResult[Rank, str]:
        """
        # ACTION:
        1.  Use identity_service to verify basic name safety.
        2.  Check the candidate exists in the set of names in RankSpec.
        3.  Verify the number matches the RankSpec value for rank param.
        4.  If any check fails, return the exception inside a ValidationResult.
        3.  When all checks pass return a tuple of rank, number. inside a ValidationResult.

        # PARAMETERS:
            *   rank (Rank): an appropriate, not null subclass instance.
            *   candidate (Any): object to validate as the correct name for the rank.
            *   identity_service (type[IdentityService]): has default value, does basic name safety checks.

        # Returns:
        ValidationResult[tuple(Rank, str)] containing either:
            - On success: tuple(Rank,str) in payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NUllRankNameException
            *   RankNameBelowBoundsException
            *   RankNameAboveBoundsException
            *   KingNameException
            *   QueenNameException
            *   BishopNameException
            *   RookNameException
            *   KnightNameException
            *   PawnNameException
            *   RankNameException
        """
        method = "RankNameValidator.validate"
        
        try:
            name_validation = identity_service.validate_name(candidate)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            
            name = cast(candidate, str)
            
            if name.upper() not in ["KING", "QUEEN", "BISHOP", "ROOK", "KNIGHT", "PAWN"]:
                return ValidationResult.failure(
                    RankNameOutOfBoundsException(
                        f"{method}: {RankNameOutOfBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if isinstance(rank, King) and name.upper() != RankSpec.KING.name.upper():
                return ValidationResult.failure(
                    KingNameException(f"{method}: {KingNameException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Queen) and name.upper() != RankSpec.QUEEN.name.upper():
                return ValidationResult.failure(
                    QueenNameException(f"{method}: {QueenNameException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Bishop) and name.upper() != RankSpec.BISHOP.name.upper():
                return ValidationResult.failure(
                    BishopNameException(f"{method}: {BishopNameException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Rook) and name.upper() != RankSpec.ROOK.name.upper():
                return ValidationResult.failure(
                    RookNameException(f"{method}: {RookNameException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Knight) and name.upper() != RankSpec.KNIGHT.name.upper():
                return ValidationResult.failure(
                    KnightNameException(f"{method}: {KnightNameException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Pawn) and name.upper() != RankSpec.PAWN.name.upper():
                return ValidationResult.failure(
                    PawnNameException(f"{method}: {PawnNameException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(name)
        except Exception as ex:
            return ValidationResult.failure(
                RankNameException(
                    f"{method}: {RankNameException.DEFAULT_MESSAGE}",
                    ex
                )
            )