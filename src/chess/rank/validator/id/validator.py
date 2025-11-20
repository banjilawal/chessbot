# src/chess/rank/validator/id/validator.py

"""
Module: chess.rank.validator.id.validator
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast, Tuple

from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.rank import (
    Rank, King, Queen, Bishop, Rook, Knight, Pawn, RankSpec, RankIdException, RankIdAboveBoundsException,
    KingIdException, QueenIdException, RookIdException, BishopIdException, KnightIdException, PawnIdException,
)


class RankIdValidator(Validator[Rank, int]):
    """
    # ROLE: Validation, Data Integrity.

    # RESPONSIBILITIES:
    Verifies the candidate is consistent with the id attribute for a Rank is
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
    ) -> ValidationResult[Rank, int]:
        """
        # ACTION:
        1.  Use identity_service to verify basic id safety.
        2.  Check the candidate exists in the set of ids in RankSpec.
        3.  Verify the number matches the RankSpec value for rank param.
        4.  If any check fails, return the exception inside a ValidationResult.
        3.  When all checks pass return a tuple of rank, number. inside a ValidationResult.

        # PARAMETERS:
            *   rank (Rank): an appropriate, not null subclass instance.
            *   candidate (Any): object to validate as the correct id for the rank.
            *   identity_service (type[IdentityService]): has default value, does basic id safety checks.

        # Returns:
        ValidationResult[tuple(Rank, int)] containing either:
            - On success: tuple(Rank,int) in the payload.
            - On failure: Exception.

        # RAISES:
            *   KingIdException
            *   QueenIdException
            *   BishopIdException
            *   RookIdException
            *   KnightIdException
            *   PawnIdException
            *   RankIdException
        """
        method = "RankIdValidator.validate"
        
        try:
            id_validation = cls.validate_rank_id_bounds(candidate)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            id = cast(candidate, int)
            
            if isinstance(rank, King) and id != RankSpec.KING.id:
                return ValidationResult.failure(
                    KingIdException(f"{method}: "
                                    f"{KingIdException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Queen) and id != RankSpec.QUEEN.id:
                return ValidationResult.failure(
                    QueenIdException(f"{method}: "
                                     f"{QueenIdException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Bishop) and id != RankSpec.BISHOP.id:
                return ValidationResult.failure(
                    BishopIdException(f"{method}: "
                                      f"{BishopIdException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Rook) and id != RankSpec.ROOK.id:
                return ValidationResult.failure(
                    RookIdException(f"{method}: "
                                    f"{RookIdException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Knight) and id != RankSpec.KNIGHT.id:
                return ValidationResult.failure(
                    KnightIdException(f"{method}: "
                                      f"{KnightIdException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Pawn) and id != RankSpec.PAWN.id:
                return ValidationResult.failure(
                    PawnIdException(f"{method}: "
                                    f"{PawnIdException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(rank, id)
        
        except Exception as ex:
            return ValidationResult.failure(
                RankIdException(
                    ex=ex,
                    message=f"{method}:"
                            f" {RankIdException.DEFAULT_MESSAGE}",
                )
            )


    @classmethod
    @LoggingLevelRouter.monitor()
    def validate_rank_id_bounds(
            cls,
            candidate: any,
            identity_service: IdentityService = IdentityService()
    ) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Use identity_service to verify basic id safety.
        2.  Check the candidate exists in the set of ids in RankSpec.
        4.  If any check fails, return the exception inside a ValidationResult.
        3.  When all checks pass return the id inside a ValidationResult.

        # PARAMETERS:
            *   candidate (Any)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[int] containing either:
            - On success: int in the payload.
            - On failure: Exception.

        # RAISES:
            *   RankIdAboveBoundsException
            *   RankIdException
        """
        method = "RankIdValidator.validate_rank_id_bounds"
        
        try:
            id_validation = identity_service.validate_id(candidate)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            id = cast(int, candidate)
            
            if id > RankSpec.max_rank_id:
                return ValidationResult.failure(
                    RankIdAboveBoundsException(
                        f"{method}: "
                        f"{RankIdAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            return ValidationResult.success(id)
        except Exception as ex:
            return ValidationResult.failure(
                RankIdException(
                    ex=ex,
                    message=f"{method}:"
                            f" {RankIdException.DEFAULT_MESSAGE}",
                )
            )