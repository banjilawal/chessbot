# src/chess/rank_name/validator/factory.py

"""
Module: chess.rank_name.validator.factory
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""


from typing import Any, cast

from chess.system import LoggingLevelRouter, Validator, ValidationResult
from chess.rank import Rank, NullRankException, King, Queen, Rook, Bishop, Knight, Pawn,  RankFieldConsistencyCheck


class RankValidatorFactory(Validator[Rank]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Rank]:
        """"""
        method = "RankValidatorFactory.validate"
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullRankException(
                        f"{method} {NullRankException.DEFAULT_MESSAGE}"
                    )
                )
 
            if isinstance(candidate, King):
                return RankValidatorFactory.validate_king(cast(King, candidate))
            if isinstance(candidate, Queen):
                return RankValidatorFactory.validate_queen_spec(cast(Queen, candidate))
            if isinstance(candidate, Rook):
                return RankValidatorFactory.validate_rook(cast(Rook, candidate))
            if isinstance(candidate, Bishop):
                return RankValidatorFactory.validate_bishop(cast(Bishop, candidate))
            if isinstance(candidate, Knight):
                return RankValidatorFactory.validate_knight(cast(Knight, candidate))
            if isinstance(candidate, Pawn):
                return RankValidatorFactory.validate_pawn(cast(Pawn, candidate))

            return ValidationResult.failure(
                TypeError(f"{method} Expected a Rank subclass, got {type(candidate).__name__}")
            )
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_king(cls, king: King) -> ValidationResult[King]:
        try:
            id_check = RankFieldConsistencyCheck.rank_id_consistency((king, king.id))
            if id_check.is_failure():
                return ValidationResult.failure(id_check.exception)
            quota_check = RankFieldConsistencyCheck.rank_quota_consistency((king, king.quota))
            if quota_check.is_failure():
                return ValidationResult.failure(quota_check.exception)
            ransom_check = RankFieldConsistencyCheck.rank_ransom_consistency((king, king.ransom))
            if ransom_check.is_failure():
                return ValidationResult.failure(ransom_check.exception)
            name_check = RankFieldConsistencyCheck.rank_name_consistency((king, king.name))
            if name_check.is_failure():
                return ValidationResult.failure(name_check.exception)
            letter_check = RankFieldConsistencyCheck.rank_letter_consistency((king, king.letter))
            if letter_check.is_failure():
                return ValidationResult.failure(letter_check.exception)
            
            return ValidationResult.success(king)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_queen(cls, queen: Queen) -> ValidationResult[Queen]:
        try:
            id_check = RankFieldConsistencyCheck.rank_id_consistency((queen, queen.id))
            if id_check.is_failure():
                return ValidationResult.failure(id_check.exception)
            quota_check = RankFieldConsistencyCheck.rank_quota_consistency((queen, queen.quota))
            if quota_check.is_failure():
                return ValidationResult.failure(quota_check.exception)
            ransom_check = RankFieldConsistencyCheck.rank_ransom_consistency((queen, queen.ransom))
            if ransom_check.is_failure():
                return ValidationResult.failure(ransom_check.exception)
            name_check = RankFieldConsistencyCheck.rank_name_consistency((queen, queen.name))
            if name_check.is_failure():
                return ValidationResult.failure(name_check.exception)
            letter_check = RankFieldConsistencyCheck.rank_letter_consistency((queen, queen.letter))
            if letter_check.is_failure():
                return ValidationResult.failure(letter_check.exception)
            
            return ValidationResult.success(queen)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_rook(cls, rook: Rook) -> ValidationResult[Rook]:
        try:
            id_check = RankFieldConsistencyCheck.rank_id_consistency((rook, rook.id))
            if id_check.is_failure():
                return ValidationResult.failure(id_check.exception)
            quota_check = RankFieldConsistencyCheck.rank_quota_consistency((rook, rook.quota))
            if quota_check.is_failure():
                return ValidationResult.failure(quota_check.exception)
            ransom_check = RankFieldConsistencyCheck.rank_ransom_consistency((rook, rook.ransom))
            if ransom_check.is_failure():
                return ValidationResult.failure(ransom_check.exception)
            name_check = RankFieldConsistencyCheck.rank_name_consistency((rook, rook.name))
            if name_check.is_failure():
                return ValidationResult.failure(name_check.exception)
            letter_check = RankFieldConsistencyCheck.rank_letter_consistency((rook, rook.letter))
            if letter_check.is_failure():
                return ValidationResult.failure(letter_check.exception)
            
            return ValidationResult.success(rook)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_bishop(cls, bishop: Bishop) -> ValidationResult[Bishop]:
        try:
            id_check = RankFieldConsistencyCheck.rank_id_consistency((bishop, bishop.id))
            if id_check.is_failure():
                return ValidationResult.failure(id_check.exception)
            quota_check = RankFieldConsistencyCheck.rank_quota_consistency((bishop, bishop.quota))
            if quota_check.is_failure():
                return ValidationResult.failure(quota_check.exception)
            ransom_check = RankFieldConsistencyCheck.rank_ransom_consistency((bishop, bishop.ransom))
            if ransom_check.is_failure():
                return ValidationResult.failure(ransom_check.exception)
            name_check = RankFieldConsistencyCheck.rank_name_consistency((bishop, bishop.name))
            if name_check.is_failure():
                return ValidationResult.failure(name_check.exception)
            letter_check = RankFieldConsistencyCheck.rank_letter_consistency((bishop, bishop.letter))
            if letter_check.is_failure():
                return ValidationResult.failure(letter_check.exception)
            
            return ValidationResult.success(bishop)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_knight(cls, knight: Knight) -> ValidationResult[Knight]:
        try:
            id_check = RankFieldConsistencyCheck.rank_id_consistency((knight, knight.id))
            if id_check.is_failure():
                return ValidationResult.failure(id_check.exception)
            quota_check = RankFieldConsistencyCheck.rank_quota_consistency((knight, knight.quota))
            if quota_check.is_failure():
                return ValidationResult.failure(quota_check.exception)
            ransom_check = RankFieldConsistencyCheck.rank_ransom_consistency((knight, knight.ransom))
            if ransom_check.is_failure():
                return ValidationResult.failure(ransom_check.exception)
            name_check = RankFieldConsistencyCheck.rank_name_consistency((knight, knight.name))
            if name_check.is_failure():
                return ValidationResult.failure(name_check.exception)
            letter_check = RankFieldConsistencyCheck.rank_letter_consistency((knight, knight.letter))
            if letter_check.is_failure():
                return ValidationResult.failure(letter_check.exception)
            
            return ValidationResult.success(knight)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_pawn(cls, pawn: Pawn) -> ValidationResult[Pawn]:
        try:
            id_check = RankFieldConsistencyCheck.rank_id_consistency((pawn, pawn.id))
            if id_check.is_failure():
                return ValidationResult.failure(id_check.exception)
            quota_check = RankFieldConsistencyCheck.rank_quota_consistency((pawn, pawn.quota))
            if quota_check.is_failure():
                return ValidationResult.failure(quota_check.exception)
            ransom_check = RankFieldConsistencyCheck.rank_ransom_consistency((pawn, pawn.ransom))
            if ransom_check.is_failure():
                return ValidationResult.failure(ransom_check.exception)
            name_check = RankFieldConsistencyCheck.rank_name_consistency((pawn, pawn.name))
            if name_check.is_failure():
                return ValidationResult.failure(name_check.exception)
            letter_check = RankFieldConsistencyCheck.rank_letter_consistency((pawn, pawn.letter))
            if letter_check.is_failure():
                return ValidationResult.failure(letter_check.exception)
            
            return ValidationResult.success(pawn)
        except Exception as e:
            return ValidationResult.failure(e)