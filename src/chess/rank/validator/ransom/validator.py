# src/chess/rank/validator/ransom/validator.py

"""
Module: chess.rank.validator.ransom.validator
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast, Tuple

from chess.rank.validator.ransom.exception import InvalidRankRansomException, RankRansomException
from chess.system import LoggingLevelRouter, ValidationResult, Validator
from chess.rank import (
    Rank, King, Queen, Bishop, Rook, Knight, Pawn, RankSpec, RankRansomException, NullRankRansomException,
    RankRansomAboveBoundsException, RankRansomBelowBoundsException, KingRansomException, QueenRansomException,
    RookRansomException, BishopRansomException, KnightRansomException, PawnRansomException,
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
    def validate(cls, candidate: Any, rank: Rank) -> ValidationResult[Rank, int]:
        """"""
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