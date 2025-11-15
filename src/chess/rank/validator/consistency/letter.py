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
    def verify_consistency(cls, rank: Rank, candidate: Any) -> ValidationResult[Rank, str]:
        """"""
        method = "VerifyRankRansomConsistency.rank_letter_consistency"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullRankLetterException(
                        f"{method}: {NullRankLetterException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, str):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: Expected a str, got {type(candidate).__id__}"
                    )
                )
            
            letter = cast(str, candidate)
            
            if letter.upper() not in ["K", "Q", "B", "R", "N", "P"]:
                return ValidationResult.failure(
                    RankLetterOutOfBoundsException(
                        f"{method}: {RankLetterOutOfBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if isinstance(rank, King) and letter.upper() != RankSpec.KING.letter.upper():
                return ValidationResult.failure(
                    WrongKingLetterException(f"{method}: {WrongKingLetterException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Queen) and letter.upper() != RankSpec.QUEEN.letter.upper():
                return ValidationResult.failure(
                    WrongQueenLetterException(f"{method}: {WrongQueenLetterException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Bishop) and letter.upper() != RankSpec.BISHOP.letter.upper():
                return ValidationResult.failure(
                    WrongBishopLetterException(f"{method}: {WrongBishopLetterException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Rook) and letter.upper() != RankSpec.ROOK.letter.upper():
                return ValidationResult.failure(
                    WrongRookLetterException(f"{method}: {WrongRookLetterException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Knight) and letter.upper() != RankSpec.KNIGHT.letter.upper():
                return ValidationResult.failure(
                    WrongKnightLetterException(f"{method}: {WrongKnightLetterException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(rank, Pawn) and letter.upper() != RankSpec.PAWN.letter.upper():
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