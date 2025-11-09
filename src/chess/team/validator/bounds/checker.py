# src/chess/team/validator/bounds/checker.py

"""
Module: chess.team.validator.bounds.checker
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast

from chess.scalar import Scalar, ScalarValidator
from chess.system import (
    LoggingLevelRouter, GameColor, NullGameColorException, ROW_SIZE, ValidationResult, NameValidator
)

from chess.team import (
    TeamSchema, AdvancingStepBoundsException, TeamColorBoundsException, NullTeamLetterException,
    TeamLetterBoundsException, TeamNameBoundsException, RankRowNullException, RankRowBelowBoundsException,
    RankRowAboveBoundsException, PawnRowNullException, PawnRowBelowBoundsException, PawnRowAboveBoundsException,
)


class TeamBoundsChecker:
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def letter_bounds_check(cls, candidate: Any) -> ValidationResult[str]:
        """"""
        method = "TeamBoundsChecker.letter_bounds_check"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamLetterException(f"{method}: {NullTeamLetterException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, str):
                return ValidationResult.failure(
                    TypeError(f"{method}:  Expected a str, got {type(candidate).__id__}")
                )
            letter = cast(str, candidate)
            
            if letter.upper() not in ["W", "B"]:
                return ValidationResult.failure(
                    TeamLetterBoundsException(f"{method}: {TeamLetterBoundsException.DEFAULT_MESSAGE}")
                )
            return ValidationResult.success(letter)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def name_bounds_check(cls, candidate: Any) -> ValidationResult[str]:
        """"""
        method = "TeamBoundsChecker.name_bounds_check"
        
        try:
            name_validation = NameValidator.validate(candidate)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            
            name = cast(str, candidate)
            
            if name.upper() not in ["WHITE", "BLACK"]:
                return ValidationResult.failure(
                    TeamNameBoundsException(f"{method}: {TeamNameBoundsException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(name)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def rank_row_bounds_check(cls, candidate: Any) -> ValidationResult[int]:
        """"""
        method = "TeamBoundsChecker.rank_row_bounds_check"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    RankRowNullException(f"{method}: {RankRowNullException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected an integer, got {type(candidate).__id__}")
                )
            
            rank_row = cast(int, candidate)
            if rank_row < 0:
                return ValidationResult.failure(
                    RankRowBelowBoundsException(f"{method}: {RankRowBelowBoundsException.DEFAULT_MESSAGE}")
                )
            
            if rank_row >= ROW_SIZE:
                return ValidationResult.failure(
                    RankRowAboveBoundsException(f"{method}: {RankRowAboveBoundsException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(rank_row)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def pawn_row_bounds_check(cls, candidate: Any) -> ValidationResult[int]:
        """"""
        method = "TeamBoundsChecker.pawn_row_bounds_check"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    PawnRowNullException(f"{method}: {PawnRowNullException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected an integer, got {type(candidate).__id__}")
                )
            
            pawn_row = cast(int, candidate)
            if pawn_row < 0:
                return ValidationResult.failure(
                    PawnRowBelowBoundsException(f"{method}: {PawnRowBelowBoundsException.DEFAULT_MESSAGE}")
                )
            
            if pawn_row >= ROW_SIZE:
                return ValidationResult.failure(
                    PawnRowAboveBoundsException(f"{method}: {PawnRowAboveBoundsException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(pawn_row)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def advancing_step_bounds_check(cls, candidate: Any) -> ValidationResult[int]:
        """"""
        method = "TeamBoundsChecker.advancing_step_bounds_check"
        
        try:
            scalar_validation = ScalarValidator.validate(candidate)
            if scalar_validation.is_failure():
                return ValidationResult.failure(scalar_validation.exception)
            
            scalar = cast(Scalar, candidate)
            
            if scalar not in [TeamSchema.WHITE.advancing_step, TeamSchema.BLACK.advancing_step]:
                return ValidationResult.failure(
                    AdvancingStepBoundsException(f"{method}: {AdvancingStepBoundsException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(scalar)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def color_bounds_check(cls, candidate: Any) -> ValidationResult[int]:
        """"""
        method = "TeamBoundsChecker.color_bounds_check"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullGameColorException(f"{method}: {NullGameColorException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, GameColor):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a GameColor, got {type(candidate).__id__}")
                )
            game_color = cast(GameColor, candidate)
            if game_color not in [TeamSchema.WHITE.color, TeamSchema.BLACK.color]:
                return ValidationResult.failure(
                    TeamColorBoundsException(f"{method}: {TeamColorBoundsException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(game_color)
        except Exception as e:
            return ValidationResult.failure(e)