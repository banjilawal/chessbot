# src/chess/rank/validator/ransom/validator.py

"""
Module: chess.rank.validator.ransom.validator
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast, Tuple

from chess.system import LoggingLevelRouter, ValidationResult, Validator
from chess.rank import (
    Rank, King, Queen, Bishop, Rook, Knight, Pawn, RankSpec, RankRansomException, NullRankRansomException,
    RankRansomAboveBoundsException, RankRansomBelowBoundsException, KingRansomException, QueenRansomException,
    RookRansomException, BishopRansomException, KnightRansomException, PawnRansomException,
)


class RankRansomValidator(Validator[Rank, int]):
    """
    # ROLE: Validation, Data Integrity.

    # RESPONSIBILITIES:
    Verifies the candidate is consistent with the ransom attribute for a Rank is
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
    @LoggingLevelRouter.monitor
    def validate(cls, rank: Rank, candidate: Any) -> ValidationResult[Rank, int]:
        """
        # ACTION:
        1.  If the candidate is not null and an INT convert to a number.
        2.  Check if the number is between 0 and Queen.ransom.
        3.  Verify the number matches the RankSpec value for rank param.
        4.  If any check fails, return the exception inside a ValidationResult.
        3.  When all checks pass return a tuple of rank, number. inside a ValidationResult.

        # PARAMETERS:
            *   rank (Rank): an appropriate, not null subclass instance.
            *   candidate (Any): object to validate as the correct ransom for the rank.

        # Returns:
        ValidationResult[tuple(Rank, int)] containing either:
            - On success: Vector in payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NUllRankRansomException
            *   RankRansomBelowBoundsException
            *   RankRansomAboveBoundsException
            *   KingRansomException
            *   QueenRansomException
            *   BishopRansomException
            *   RookRansomException
            *   KnightRansomException
            *   PawnRansomException
            *   RankRansomException
        """
        method = "RankRansomValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullRankRansomException(
                        f"{method}: {NullRankRansomException.DEFAULT_MESSAGE}"
                    )
                )
                
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: Expected an integer, got {type(candidate).__id__} instead."
                    )
                )
                
            ransom = cast(candidate, int)
            if ransom < 0:
                return ValidationResult.failure(
                    RankRansomBelowBoundsException(
                        f"{method}: {RankRansomBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
                
            if ransom > RankSpec.QUEEN.ransom:
                return ValidationResult.failure(
                    RankRansomAboveBoundsException(
                        f"{method}: {RankRansomAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )

                
            if isinstance(rank, King) and ransom != RankSpec.KING.ransom:
                return ValidationResult.failure(
                    KingRansomException(f"{method}: {KingRansomException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Queen) and ransom != RankSpec.QUEEN.ransom:
                return ValidationResult.failure(
                    QueenRansomException(f"{method}: {QueenRansomException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Bishop) and ransom != RankSpec.BISHOP.ransom:
                return ValidationResult.failure(
                    BishopRansomException(f"{method}: {BishopRansomException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Rook) and ransom != RankSpec.ROOK.rasnom:
                return ValidationResult.failure(
                    RookRansomException(f"{method}: {RookRansomException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Knight) and ransom != RankSpec.KNIGHT.ransom:
                return ValidationResult.failure(
                    KnightRansomException(f"{method}: {KnightRansomException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Pawn) and ransom != RankSpec.PAWN.ransom:
                return ValidationResult.failure(
                    PawnRansomException(f"{method}: {PawnRansomException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(rank, ransom)
        
        except Exception as ex:
            return ValidationResult.failure(
                RankRansomException(
                    f"{method}: {RankRansomException.DEFAULT_MESSAGE}",
                    ex
                )
            )