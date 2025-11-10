# src/chess/rank_name/validator/bounds/__init__.py

"""
Module: chess.rank_name.validator.bounds.checker
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast

from chess.system import ValidationResult, NameValidator, IdValidator, LoggingLevelRouter
from chess.rank import (
    RankSpec, NullRankLetterException, RankLetterOutOfBoundsException, RankNameOutOfBoundsException,
    NullRankRansomException, RankRansomBelowBoundsException, RankRansomAboveBoundsException,
    NullRankQuotaException, RankQuotaBelowBoundsException, RankQuotaAboveBoundsException,
    RankIdAboveBoundsException
)



class RankBoundsChecker:
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def letter_bounds_check(cls, candidate: Any) -> ValidationResult[str]:
        """"""
        method = "RankBoundsChecker.letter_bounds_check"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullRankLetterException(f"{method}: {NullRankLetterException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, str):
                return ValidationResult.failure(
                    TypeError(f"{method}:  Expected a str, got {type(candidate).__id__}")
                )
            letter = cast(str, candidate)
            
            if letter.upper() not in ["K", "Q", "B", "R", "N", "P"]:
                return ValidationResult.failure(
                    RankLetterOutOfBoundsException(f"{method}: {RankLetterOutOfBoundsException.DEFAULT_MESSAGE}")
                )
            return ValidationResult.success(letter)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def name_bounds_check(cls, candidate: Any) -> ValidationResult[str]:
        """"""
        method = "RankBoundsChecker.name_bounds_check"
        
        try:
            name_validation = NameValidator.validate(candidate)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            
            name = cast(candidate, str)
            
            if name.upper() not in ["KING", "QUEEN", "BISHOP", "ROOK", "KNIGHT", "PAWN"]:
                return ValidationResult.failure(
                    RankNameOutOfBoundsException(f"{method}: {RankNameOutOfBoundsException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(name)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def ransom_bounds_check(cls, candidate: Any) -> ValidationResult[int]:
        """"""
        method = "RankBoundsChecker.ransom_bounds_check"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullRankRansomException(f"{method}: {NullRankRansomException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected an integer, got {type(candidate).__id__}")
                )
            
            number = cast(candidate, int)
            if number < 0:
                return ValidationResult.failure(
                    RankRansomBelowBoundsException(f"{method}: {RankRansomBelowBoundsException.DEFAULT_MESSAGE}")
                )
            
            if number > RankSpec.QUEEN.ransom:
                return ValidationResult.failure(
                    RankRansomAboveBoundsException(f"{method}: {RankRansomAboveBoundsException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(number)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def quota_bounds_check(cls, candidate: Any) -> ValidationResult[int]:
        """"""
        method = "RankBoundsChecker.quota_bounds_check"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullRankQuotaException(f"{method}: {NullRankQuotaException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected an integer, got {type(candidate).__id__}")
                )
            
            quota= cast(candidate, int)
            if quota < 1:
                return ValidationResult.failure(
                    RankQuotaBelowBoundsException(f"{method}: {RankQuotaBelowBoundsException.DEFAULT_MESSAGE}")
                )
            
            if quota > RankSpec.PAWN.ransom:
                return ValidationResult.failure(
                    RankQuotaAboveBoundsException(f"{method}: {RankQuotaAboveBoundsException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(quota)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def id_bounds_check(cls, candidate: Any) -> ValidationResult[int]:
        """"""
        method = "RankBoundsChecker.id_bounds_check"
        
        try:
            id_validation = IdValidator.validate(candidate)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            id = cast(candidate, int)
            if id > RankSpec.max_rank_id:
                return ValidationResult.failure(
                    RankIdAboveBoundsException(f"{method}: {RankIdAboveBoundsException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(id)
        except Exception as e:
            return ValidationResult.failure(e)