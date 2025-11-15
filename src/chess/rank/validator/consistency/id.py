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


class VerifyRankIdConsistency:
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
    def verify_consistency(
            cls,
            candidate: Any,
            identity_service: type[IdentityService]=IdentityService
    ) -> ValidationResult[Rank, int]:
        """"""
        method = "VerifyRankRansomConsistency.rank_id_consistency"
        
        try:
            id_validation = identity_service.validate_id(candidate)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            id = cast(candidate, int)
            if id > RankSpec.max_rank_id:
                return ValidationResult.failure(
                    RankIdAboveBoundsException(
                        f"{method}: {RankIdAboveBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if isinstance(rank, King) and id != RankSpec.KING.id:
                return ValidationResult.failure(
                    WrongKingIdException(f"{method}: {WrongKingIdException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Queen) and id != RankSpec.QUEEN.id:
                return ValidationResult.failure(
                    WrongQueenIdException(f"{method}: {WrongQueenIdException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Bishop) and id != RankSpec.BISHOP.id:
                return ValidationResult.failure(
                    WrongBishopIdException(f"{method}: {WrongBishopIdException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Rook) and id != RankSpec.ROOK.rasnom:
                return ValidationResult.failure(
                    WrongRookIdException(f"{method}: {WrongRookIdException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Knight) and id != RankSpec.KNIGHT.id:
                return ValidationResult.failure(
                    WrongKnightIdException(f"{method}: {WrongKnightIdException.DEFAULT_MESSAGE}")
                )
            if isinstance(rank, Pawn) and id != RankSpec.PAWN.id:
                return ValidationResult.failure(
                    WrongPawnIdException(f"{method}: {WrongPawnIdException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(id)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    def _basic_rank_check(cls, candidate: Any) -> ValidationResult[Rank]:
        """"""
        method = "RankSpec._basic_rank_check"
    
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullRankException(f"{method}: {NullRankException.DEFAULT_MESSAGE}")
                )

            if not isinstance(candidate, Rank):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a Rank, got {type(candidate).__id__}")
                )
            return ValidationResult.success(cast(candidate, Rank))
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    def _basic_tuple_check(cls, candidate: Any) -> ValidationResult[Rank]:
        """"""
        method = "RankSpec._basic_tuple_check"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullRankConsistencyTupleException(f"{method}: {NullRankConsistencyTupleException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Tuple):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a Tuple, got {type(candidate).__id__}")
                )
            
            return cls._basic_rank_check(cast(candidate, Tuple)[0])
        except Exception as e:
            return ValidationResult.failure(e)
            
