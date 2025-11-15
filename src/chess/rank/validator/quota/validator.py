# src/chess/rank/validator/consistency/check.py

"""
Module: chess.rank.validator.consistency.check
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast, Tuple
from chess.system import LoggingLevelRouter, ValidationResult
from chess.rank import (
    NullRankException, Rank, RankSpec, King, Queen, Bishop, Rook, Knight, Pawn, RankBoundsChecker,
    
    WrongKingRansomException, WrongQueenRansomException, WrongRookRansomException, WrongBishopRansomException,
    WrongKnightRansomException, WrongPawnRansomException,
    
    WrongKingQuotaException, WrongQueenQuotaException, WrongRookQuotaException, WrongBishopQuotaException,
    WrongKnightQuotaException, WrongPawnQuotaException,
    
    WrongKingNameException, WrongQueenNameException, WrongRookNameException, WrongBishopNameException,
    WrongKnightNameException, WrongPawnNameException,
    
    WrongKingLetterException, WrongQueenLetterException, WrongRookLetterException, WrongBishopLetterException,
    WrongKnightLetterException, WrongPawnLetterException,
    
    WrongKingIdException, WrongQueenIdException, WrongRookIdException, WrongBishopIdException, WrongKnightIdException,
    WrongPawnIdException,
    NullRankConsistencyTupleException
)


class RankQuotaValidator:
    """
    # ROLE: Validator, Consistency Management

    # RESPONSIBILITIES:
    1.  Tests
    2.  Provides reference to a Piece.

    # PROVIDES:
    Square

    # ATTRIBUTES:
        *   _id (int): unique identifier
        *   _name (str): letter-number combination. Only unique in the Board
        *   _coord (Coord): row-column array indices in Board array.
        *   _occupant (Optional[Piece]): Piece object that might be occupying the Square.
    """
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_consistency(cls, rank: Rank, candidate: Any) -> ValidationResult[Rank, int]:
        """"""
        method = "RankRansomValidator.rank_quota_consistency"
        
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
            
            if quota > RankSpec.PAWN.ransom:
                return ValidationResult.failure(
                    RankQuotaAboveBoundsException(
                        f"{method}: {RankQuotaAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if isinstance(rank, King) and quota != RankSpec.KING.quota:
                return ValidationResult.failure(
                    WrongKingQuotaException(f"{method}: {WrongKingQuotaException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Queen) and quota != RankSpec.QUEEN.quota:
                return ValidationResult.failure(
                    WrongQueenQuotaException(f"{method}: {WrongQueenQuotaException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Bishop) and quota != RankSpec.BISHOP.quota:
                return ValidationResult.failure(
                    WrongBishopQuotaException(f"{method}: {WrongBishopQuotaException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Rook) and quota != RankSpec.ROOK.quota:
                return ValidationResult.failure(
                    WrongRookQuotaException(f"{method}: {WrongRookQuotaException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Knight) and quota != RankSpec.KNIGHT.quota:
                return ValidationResult.failure(
                    WrongKnightQuotaException(f"{method}: {WrongKnightQuotaException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Pawn) and quota != RankSpec.PAWN.quota:
                return ValidationResult.failure(
                    WrongPawnQuotaException(f"{method}: {WrongPawnQuotaException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(quota)
        except Exception as ex:
            return ValidationResult.failure(
                RankQuotaInconsistencyException(
                    f"{method}: {RankQuotaInconsistencyException.DEFAULT_MESSAGE}",
                    ex
                )
            )