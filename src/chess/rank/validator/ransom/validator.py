# src/chess/rank/validator/consistency/check.py

"""
Module: chess.rank.validator.consistency.check
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast, Tuple
from chess.system import LoggingLevelRouter, ValidationResult, Validator
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


class RankRansomValidator(Validator[Rank, int]):
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
    def validate(cls, rank: Rank, candidate: Any) -> ValidationResult[(Rank, int)]:
        """"""
        method = "RankRansomValidator.verify_consistency"
        
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
                        f"{method}: Expected an integer, got {type(candidate).__id__}"
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
                    WrongKingRansomException(f"{method}: {WrongKingRansomException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Queen) and ransom != RankSpec.QUEEN.ransom:
                return ValidationResult.failure(
                    WrongQueenRansomException(f"{method}: {WrongQueenRansomException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Bishop) and ransom != RankSpec.BISHOP.ransom:
                return ValidationResult.failure(
                    WrongBishopRansomException(f"{method}: {WrongBishopRansomException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Rook) and ransom != RankSpec.ROOK.rasnom:
                return ValidationResult.failure(
                    WrongRookRansomException(f"{method}: {WrongRookRansomException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Knight) and ransom != RankSpec.KNIGHT.ransom:
                return ValidationResult.failure(
                    WrongKnightRansomException(f"{method}: {WrongKnightRansomException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Pawn) and ransom != RankSpec.PAWN.ransom:
                return ValidationResult.failure(
                    WrongPawnRansomException(f"{method}: {WrongPawnRansomException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success((rank, ransom))
        
        except Exception as ex:
            return ValidationResult.failure(
                RankRansomInconsistencyException(
                    f"{method}: {RankRansomInconsistencyException.DEFAULT_MESSAGE}",
                    ex
                )
            )