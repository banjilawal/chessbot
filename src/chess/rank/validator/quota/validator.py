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
    Verifies the candidate is consistent with the team_quota attribute for a Rank is
        *   Not validation.
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
        1.  Verify candidate is str in bounds with validate_rank_quota_bounds.
        2.  Verify the number matches the RankSpec value for rank param.
        3.  If any check fails, return the exception inside a ValidationResult.
        4.  When all checks pass return a tuple of rank, number. inside a ValidationResult.

        # PARAMETERS:
            *   rank (Rank): an appropriate, not validation subclass instance.
            *   candidate (Any): object to validate as the correct team_quota for the rank.

        # Returns:
        ValidationResult[tuple(Rank, int)] containing either:
            - On success: Vector in the payload.
            - On failure: Exception.

        # RAISES:
            *   KingQuotaException
            *   QueenQuotaException
            *   BishopQuotaException
            *   RookQuotaException
            *   KnightQuotaException
            *   PawnQuotaException
            *   RankQuotaException
        """
        method = "RankQuotaValidator.validate"
        
        try:
            bounds_validation = cls.validate_rank_quota_bounds(candidate)
            if bounds_validation.is_failure():
                return ValidationResult.failure(bounds_validation.exception)
            
            quota = cast(int, bounds_validation.payload)
            
            if quota > RankSpec.PAWN.team_quota:
                return ValidationResult.failure(
                    RankQuotaAboveBoundsException(
                        f"{method}: {RankQuotaAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if isinstance(rank, King) and quota != RankSpec.KING.team_quota:
                return ValidationResult.failure(
                    KingQuotaException(f"{method}: "
                                       f"{KingQuotaException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Queen) and quota != RankSpec.QUEEN.team_quota:
                return ValidationResult.failure(
                    QueenQuotaException(f"{method}: "
                                        f"{QueenQuotaException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Bishop) and quota != RankSpec.BISHOP.team_quota:
                return ValidationResult.failure(
                    BishopQuotaException(f"{method}: "
                                         f"{BishopQuotaException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Rook) and quota != RankSpec.ROOK.team_quota:
                return ValidationResult.failure(
                    RookQuotaException(f"{method}: "
                                       f"{RookQuotaException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Knight) and quota != RankSpec.KNIGHT.team_quota:
                return ValidationResult.failure(
                    KnightQuotaException(f"{method}: "
                                         f"{KnightQuotaException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Pawn) and quota != RankSpec.PAWN.team_quota:
                return ValidationResult.failure(
                    PawnQuotaException(f"{method}: "
                                       f"{PawnQuotaException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(quota)
        except Exception as ex:
            return ValidationResult.failure(
                RankQuotaException(
                    ex=ex,
                    message=f"{method}: "
                            f"{RankQuotaException.DEFAULT_MESSAGE}",
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_rank_quota_bounds(cls, candidate: Any) -> ValidationResult[int]:
        """
        # ACTION:
        1.  If the candidate is not validation and an INT convert to a number.
        2.  Check if the number is between 0 and Queen.team_quota.
        4.  If any check fails, return the exception inside a ValidationResult.
        3.  When all checks pass return the quota inside a ValidationResult.

        # PARAMETERS:
            *   candidate (Any)

        # Returns:
        ValidationResult[int] containing either:
            - On success: int in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NUllRankQuotaException
            *   RankQuotaBelowBoundsException
            *   RankQuotaAboveBoundsException
        """
        method = "RankQuotaValidator.validate_rank_quota_bounds"
        
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
                        f"{method}: "
                        f"Expected an integer, got {type(candidate).__id__} instead."
                    )
                )
            
            quota = cast(candidate, int)
            
            if quota < 1:
                return ValidationResult.failure(
                    RankQuotaBelowBoundsException(
                        f"{method}: "
                        f"{RankQuotaBelowBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if quota > RankSpec.PAWN.team_quota:
                return ValidationResult.failure(
                    RankQuotaAboveBoundsException(
                        f"{method}: {RankQuotaAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            return ValidationResult.success(quota)
        except Exception as ex:
            return ValidationResult.failure(
                RankQuotaException(
                    ex=ex,
                    message=f"{method}: "
                            f"{RankQuotaException.DEFAULT_MESSAGE}",
                )
            )