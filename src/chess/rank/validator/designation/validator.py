# src/chess/rank/validator/designation/validator.py

"""
Module: chess.rank.validator.designation.validator
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast, Tuple

from chess.system import IdentityService, LoggingLevelRouter, NullStringException, ValidationResult
from chess.rank import (
    NullRankDesignationException, Rank, King, Queen, Bishop, RankDesignationException, RankIdException, Rook, Knight,
    Pawn, RankSpec,
    RankDesignationException,
    RankDesignationBoundsException,
    KingDesignationException, QueenDesignationException, RookDesignationException, BishopDesignationException, KnightDesignationException,
    PawnDesignationException,
)


class RankDesignationValidator:
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
    ) -> ValidationResult[Rank, str]:
        """
        # ACTION:
        1.  Use validate_rank_designation_bounds to verify the candidate is a string. within
            RankSpec designations.
        3.  Verify the designation matches a Rank's designation attribute.
        4.  If any check fails, return the exception inside a ValidationResult.
        3.  When all checks pass return a tuple of rank, designation. inside a ValidationResult.

        # PARAMETERS:
            *   rank (Rank): an appropriate, not null subclass instance.
            *   candidate (Any): object to validate as the correct designation for the rank.

        # Returns:
        ValidationResult[tuple(Rank, str)] containing either:
            - On success: tuple(Rank,str) in the payload.
            - On failure: Exception.

        # RAISES:

            *   KingDesignationException
            *   QueenDesignationException
            *   BishopDesignationException
            *   RookDesignationException
            *   KnightDesignationException
            *   PawnDesignationException
            *   RankDesignationException
        """
        method = "RankDesignationValidator.validate"
        
        try:
            designation_validation = cls.validate_rank_designation_bounds(candidate)
            if designation_validation.is_failure():
                return ValidationResult.failure(designation_validation.exception)
            
            designation = cast(str, designation_validation.payload)
            
            if isinstance(rank, King) and designation.upper() != RankSpec.KING.designation.upper():
                return ValidationResult.failure(
                    KingDesignationException(f"{method}: {KingDesignationException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Queen) and designation.upper() != RankSpec.QUEEN.designation.upper():
                return ValidationResult.failure(
                    QueenDesignationException(f"{method}: {QueenDesignationException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Bishop) and designation.upper() != RankSpec.BISHOP.designation.upper():
                return ValidationResult.failure(
                    BishopDesignationException(f"{method}: {BishopDesignationException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Rook) and designation.upper() != RankSpec.ROOK.designation.upper():
                return ValidationResult.failure(
                    RookDesignationException(f"{method}: {RookDesignationException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Knight) and designation.upper() != RankSpec.KNIGHT.designation.upper():
                return ValidationResult.failure(
                    KnightDesignationException(f"{method}: {KnightDesignationException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Pawn) and designation.upper() != RankSpec.PAWN.designation.upper():
                return ValidationResult.failure(
                    PawnDesignationException(f"{method}: {PawnDesignationException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(designation)
        
        except Exception as ex:
            return ValidationResult.failure(
                RankDesignationException(
                    ex=ex,
                    message=f"{method}: "
                            f"{RankDesignationException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def validate_rank_designation_bounds(
            cls,
            candidate: any
    ) -> ValidationResult[str]:
        """
        # ACTION:
        1.  Verify the candidate is not null.
        2.  Verify the candidate is a string.
        2.  Check the candidate exists in the set of in RankSpec designations.
        4.  If any check fails, return the exception inside a ValidationResult.
        3.  When all checks pass return the designation inside a ValidationResult.

        # PARAMETERS:
            *   candidate (Any)

        # Returns:
        ValidationResult[str] containing either:
            - On success: str in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NUllRankDesignationException
            *   RankDesignationBoundsException
        """
        method = "RankDesignationValidator.validate_rank_designation_bounds"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullRankDesignationException(f"{method}: "
                                        f"{NullRankDesignationException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, str):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Expected a str, got {type(candidate).__id__} instead."
                    )
                )
            
            designation = cast(str, candidate)
            
            if designation.upper() not in ["K", "Q", "B", "R", "N", "P"]:
                return ValidationResult.failure(
                    RankDesignationBoundsException(
                        f"{method}: "
                        f"{RankDesignationBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            return ValidationResult.success(designation.upper)
        
        except Exception as ex:
            return ValidationResult.failure(
                RankIdException(
                    ex=ex,
                    message=f"{method}:"
                            f" {RankDesignationException.DEFAULT_MESSAGE}",
                )
            )