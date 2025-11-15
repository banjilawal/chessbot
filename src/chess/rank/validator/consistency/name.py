# src/chess/rank/validator/consistency/check.py

"""
Module: chess.rank.validator.consistency.check
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast, Tuple
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult
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


class VerifyRankLetterConsistency:
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
    def verify_consistency(
            cls,
            rank: Rank,
            candidate: Any,
            identity_service: type[IdentityService]=IdentityService
    ) -> ValidationResult[Rank, str]:
        """"""
        method = "VerifyRankRansomConsistency.rank_name_consistency"
        
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
                    WrongKingNameException(f"{method}: {WrongKingNameException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Queen) and name.upper() != RankSpec.QUEEN.name.upper():
                return ValidationResult.failure(
                    WrongQueenNameException(f"{method}: {WrongQueenNameException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Bishop) and name.upper() != RankSpec.BISHOP.name.upper():
                return ValidationResult.failure(
                    WrongBishopNameException(f"{method}: {WrongBishopNameException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Rook) and name.upper() != RankSpec.ROOK.name.upper():
                return ValidationResult.failure(
                    WrongRookNameException(f"{method}: {WrongRookNameException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Knight) and name.upper() != RankSpec.KNIGHT.name.upper():
                return ValidationResult.failure(
                    WrongKnightNameException(f"{method}: {WrongKnightNameException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Pawn) and name.upper() != RankSpec.PAWN.name.upper():
                return ValidationResult.failure(
                    WrongPawnNameException(f"{method}: {WrongPawnNameException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(name)
        except Exception as ex:
            return ValidationResult.failure(
                RankNameInconsistencyException(
                    f"{method}: {RankNameInconsistencyException.DEFAULT_MESSAGE}",
                    e
                )
            )
