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
    Rank, RankSpec, King, Queen, Bishop, Rook, Knight, Pawn, RankBoundsChecker,

    WrongKingRansomException, WrongQueenRansomException, WrongRookRansomException, WrongBishopRansomException,
    WrongKnightRansomException, WrongPawnRansomException,
    
    WrongKingQuotaException, WrongQueenQuotaException, WrongRookQuotaException, WrongBishopQuotaException,
    WrongKnightQuotaException, WrongPawnQuotaException,
    
    WrongKingNameException, WrongQueenNameException, WrongRookNameException, WrongBishopNameException,
    WrongKnightNameException, WrongPawnNameException,

    WrongKingLetterException, WrongQueenLetterException, WrongRookLetterException, WrongBishopLetterException,
    WrongKnightLetterException, WrongPawnLetterException,
    
    WrongKingIdException, WrongQueenIdException, WrongRookIdException, WrongBishopIdException, WrongKnightIdException,
    WrongPawnIdException
)


class RankFieldConsistencyCheck:
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def rank_ransom_consistency(cls, candidate: Any) -> ValidationResult[int]:
        """"""
        method = "RankFieldConsistencyCheck.rank_ransom_consistency"
        
        try:
            tuple_validation = cls._basic_tuple_check(candidate)
            if tuple_validation.failure():
                return ValidationResult.failure(tuple_validation.exception)
            
            pair = cast(Tuple, candidate)
            rank = cast(Rank, pair[0])
            
            ransom_bounds_check = RankBoundsChecker.ransom_bounds_check(pair[1])
            if ransom_bounds_check.failure():
                return ValidationResult.failure(ransom_bounds_check.exception)
            
            ransom = cast(int, pair[1])
            
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
            
            return ValidationResult.success(ransom)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def rank_quota_consistency(cls, candidate: Any) -> ValidationResult[int]:
        """"""
        method = "RankFieldConsistencyCheck.rank_quota_consistency"
        
        try:
            tuple_validation = cls._basic_tuple_check(candidate)
            if tuple_validation.failure():
                return ValidationResult.failure(tuple_validation.exception)
            
            pair = cast(Tuple, candidate)
            rank = cast(Rank, pair[0])
            
            quota_bounds_check = RankBoundsChecker.quota_bounds_check(pair[1])
            if quota_bounds_check.failure():
                return ValidationResult.failure(quota_bounds_check.exception)
            
            quota = cast(int, quota_bounds_check.payload)
            
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
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    def rank_name_consistency(cls, candidate: Any) -> ValidationResult[str]:
        """"""
        method = "RankFieldConsistencyCheck.rank_name_consistency"
        
        try:
            tuple_validation = cls._basic_tuple_check(candidate)
            if tuple_validation.failure():
                return ValidationResult.failure(tuple_validation.exception)
            
            pair = cast(Tuple, candidate)
            rank = cast(Rank, pair[0])
            
            name_bounds_check = RankBoundsChecker.name_bounds_check(pair[1])
            if name_bounds_check.is_failure():
                return ValidationResult.failure(name_bounds_check.exception)
            name = cast(str, name_bounds_check.payload)
            
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
                    WrongRookNamexception(f"{method}: {WrongRookNamexception.DEFAULT_MESSAGE}")
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
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    def rank_letter_consistency(cls, candidate: Any) -> ValidationResult[str]:
        """"""
        method = "RankFieldConsistencyCheck.rank_letter_consistency"
        
        try:
            tuple_validation = cls._basic_tuple_check(candidate)
            if tuple_validation.is_failure():
                return ValidationResult.failure(tuple_validation.exception)
            
            pair = cast(tuple_validation.payload, Tuple)
            rank = cast(Rank, pair[0])
            
            letter_bounds_check = RankBoundsChecker.letter_bounds_check(pair[1])
            if letter_bounds_check.is_failure():
                return ValidationResult.failure(letter_bounds_check.exception)
            letter = cast(str, letter_bounds_check.payload)
            
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
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def rank_id_consistency(cls, candidate: Any) -> ValidationResult[int]:
        """"""
        method = "RankFieldConsistencyCheck.rank_id_consistency"
        
        try:
            tuple_validation = cls._basic_tuple_check(candidate)
            if tuple_validation.failure():
                return ValidationResult.failure(tuple_validation.exception)
            
            pair = cast(Tuple, candidate)
            rank = cast(Rank, pair[0])
            
            id_bounds_check = RankBoundsChecker.id_bounds_check(pair[1])
            if id_bounds_check.failure():
                return ValidationResult.failure(id_bounds_check.exception)
            
            id = cast(int, pair[1])
            
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
                    NullTupleException(f"{method}: {NullTupleException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Tuple):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a Tuple, got {type(candidate).__id__}")
                )
            
            return RankFieldValidator._basic_rank_check(cast(candidate, Tuple)[0])
        except Exception as e:
            return ValidationResult.failure(e)
            
