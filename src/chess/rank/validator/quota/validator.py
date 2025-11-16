# src/chess/rank/validator/quota/validator.py

"""
Module: chess.rank.validator.quota.validator
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast, Tuple

from chess.system import LoggingLevelRouter, ValidationResult, Validator
from chess.rank import (
    Rank, King, Queen, Bishop, Rook, Knight, Pawn, RankSpec, RankQuotaException, NullRankQuotaException,
    RankQuotaAboveBoundsException, RankQuotaBelowBoundsException, KingQuotaException, QueenQuotaException,
    RookQuotaException, BishopQuotaException, KnightQuotaException, PawnQuotaException,
)


class RankQuotaValidator(Validator[Rank, int]):
    """
    # ROLE: Validation, Data Integrity.

    # RESPONSIBILITIES:
    Verifies the candidate is consistent with the quota attribute for a Rank is
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
    @LoggingLevelRouter.monitor
    def validate(cls, rank: Rank, candidate: Any) -> ValidationResult[Rank, int]:
        """
        # ACTION:
        1.  If the candidate is not null and an INT convert to a number.
        2.  Check if the number is between 0 and Queen.quota.
        3.  Verify the number matches the RankSpec value for rank param.
        4.  If any check fails, return the exception inside a ValidationResult.
        3.  When all checks pass return a tuple of rank, number. inside a ValidationResult.

        # PARAMETERS:
            *   rank (Rank): an appropriate, not null subclass instance.
            *   candidate (Any): object to validate as the correct quota for the rank.

        # Returns:
        ValidationResult[tuple(Rank, int)] containing either:
            - On success: Vector in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NUllRankQuotaException
            *   RankQuotaBelowBoundsException
            *   RankQuotaAboveBoundsException
            *   KingQuotaException
            *   QueenQuotaException
            *   BishopQuotaException
            *   RookQuotaException
            *   KnightQuotaException
            *   PawnQuotaException
            *   RankQuotaException
        """
        method = "RankQuotaValidator.rank_quota_consistency"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullRankQuotaException(
                        f"{method}: {NullRankQuotaException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: Expected an integer, got {type(candidate).__id__}"
                    )
                )
            
            quota = cast(candidate, int)
            if quota < 1:
                return ValidationResult.failure(
                    RankQuotaBelowBoundsException(
                        f"{method}: {RankQuotaBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if quota > RankSpec.PAWN.quota:
                return ValidationResult.failure(
                    RankQuotaAboveBoundsException(
                        f"{method}: {RankQuotaAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if isinstance(rank, King) and quota != RankSpec.KING.quota:
                return ValidationResult.failure(
                    KingQuotaException(f"{method}: {KingQuotaException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Queen) and quota != RankSpec.QUEEN.quota:
                return ValidationResult.failure(
                    QueenQuotaException(f"{method}: {QueenQuotaException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Bishop) and quota != RankSpec.BISHOP.quota:
                return ValidationResult.failure(
                    BishopQuotaException(f"{method}: {BishopQuotaException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Rook) and quota != RankSpec.ROOK.quota:
                return ValidationResult.failure(
                    RookQuotaException(f"{method}: {RookQuotaException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Knight) and quota != RankSpec.KNIGHT.quota:
                return ValidationResult.failure(
                    KnightQuotaException(f"{method}: {KnightQuotaException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Pawn) and quota != RankSpec.PAWN.quota:
                return ValidationResult.failure(
                    PawnQuotaException(f"{method}: {PawnQuotaException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(quota)
        except Exception as ex:
            return ValidationResult.failure(
                RankQuotaException(
                    f"{method}: {RankQuotaException.DEFAULT_MESSAGE}",
                    ex
                )
            )