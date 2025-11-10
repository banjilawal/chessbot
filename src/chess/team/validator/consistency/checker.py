# src/chess/team_name/validator/consistency/check.py

"""
Module: chess.team_name.validator.consistency.check
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""


from typing import Any, cast, Tuple
from chess.system import GameColor, LoggingLevelRouter, ValidationResult
from chess.team import (
    Team, NullTeamException, TeamBoundsChecker,
    AdvancingStepInconsistencyException, TeamRankRowInconsistencyException, TeamPawnRowInconsistencyException,
    TeamNameInconsistencyException, TeamLetterInconsistencyException, TeamColorInconsistencyException,
    NullTeamConsistencyTupleException
)



class TeamFieldConsistencyCheck:
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def team_advancing_step_consistency(cls, candidate: Any) -> ValidationResult[int]:
        """"""
        method = "TeamFieldConsistencyCheck.team_advancing_step_consistency"
        
        try:
            tuple_validation = cls._basic_tuple_check(candidate)
            if tuple_validation.failure():
                return ValidationResult.failure(tuple_validation.exception)
            
            pair = cast(Tuple, candidate)
            team = cast(Team, pair[0])
            
            advancing_step_bounds_check = TeamBoundsChecker.advancing_step_bounds_check(pair[1])
            if advancing_step_bounds_check.failure():
                return ValidationResult.failure(advancing_step_bounds_check.exception)
            
            advancing_step = cast(int, pair[1])
            
            if team.schema.advancing_step != advancing_step:
                return ValidationResult.failure(
                    AdvancingStepInconsistencyException(
                        f"{method}: {AdvancingStepInconsistencyException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(advancing_step)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def team_rank_row_consistency(cls, candidate: Any) -> ValidationResult[int]:
        """"""
        method = "TeamFieldConsistencyCheck.team_rank_row_consistency"
        
        try:
            tuple_validation = cls._basic_tuple_check(candidate)
            if tuple_validation.failure():
                return ValidationResult.failure(tuple_validation.exception)
            
            pair = cast(Tuple, candidate)
            team = cast(Team, pair[0])
            
            rank_row_bounds_check = TeamBoundsChecker.rank_row_bounds_check(pair[1])
            if rank_row_bounds_check.failure():
                return ValidationResult.failure(rank_row_bounds_check.exception)
            
            rank_row = cast(int, pair[1])
            
            if team.schema.rank_row != rank_row:
                return ValidationResult.failure(
                    TeamRankRowInconsistencyException(f"{method}: {TeamRankRowInconsistencyException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(rank_row)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def team_pawn_row_consistency(cls, candidate: Any) -> ValidationResult[int]:
        """"""
        method = "TeamFieldConsistencyCheck.team_pawn_row_consistency"
        
        try:
            tuple_validation = cls._basic_tuple_check(candidate)
            if tuple_validation.failure():
                return ValidationResult.failure(tuple_validation.exception)
            
            pair = cast(Tuple, candidate)
            team = cast(Team, pair[0])
            
            pawn_row_bounds_check = TeamBoundsChecker.pawn_row_bounds_check(pair[1])
            if pawn_row_bounds_check.failure():
                return ValidationResult.failure(pawn_row_bounds_check.exception)
            
            pawn_row = cast(int, pawn_row_bounds_check.payload)
            
            if team.schema.pawn_row != pawn_row:
                return ValidationResult.failure(
                    TeamPawnRowInconsistencyException(f"{method}: {TeamPawnRowInconsistencyException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(pawn_row)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    def team_name_consistency(cls, candidate: Any) -> ValidationResult[str]:
        """"""
        method = "TeamFieldConsistencyCheck.team_name_consistency"
        
        try:
            tuple_validation = cls._basic_tuple_check(candidate)
            if tuple_validation.failure():
                return ValidationResult.failure(tuple_validation.exception)
            
            pair = cast(Tuple, candidate)
            team = cast(Team, pair[0])
            
            name_bounds_check = TeamBoundsChecker.name_bounds_check(pair[1])
            if name_bounds_check.is_failure():
                return ValidationResult.failure(name_bounds_check.exception)
            name = cast(str, name_bounds_check.payload)
            
            if team.schema.name.upper() != name.upper():
                return ValidationResult.failure(
                    TeamNameInconsistencyException(f"{method}: {TeamNameInconsistencyException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(name)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    def team_letter_consistency(cls, candidate: Any) -> ValidationResult[str]:
        """"""
        method = "TeamFieldConsistencyCheck.team_letter_consistency"
        
        try:
            tuple_validation = cls._basic_tuple_check(candidate)
            if tuple_validation.is_failure():
                return ValidationResult.failure(tuple_validation.exception)
            
            pair = cast(Tuple, tuple_validation.payload)
            team = cast(Team, pair[0])
            
            letter_bounds_check = TeamBoundsChecker.letter_bounds_check(pair[1])
            if letter_bounds_check.is_failure():
                return ValidationResult.failure(letter_bounds_check.exception)
            letter = cast(str, letter_bounds_check.payload)
            
            if team.schema.letter.upper() != letter:
                return ValidationResult.failure(
                    TeamLetterInconsistencyException(f"{method}: {TeamLetterInconsistencyException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(letter)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def team_color_consistency(cls, candidate: Any) -> ValidationResult[GameColor]:
        """"""
        method = "TeamFieldConsistencyCheck.team_id_consistency"
        
        try:
            tuple_validation = cls._basic_tuple_check(candidate)
            if tuple_validation.failure():
                return ValidationResult.failure(tuple_validation.exception)
            
            pair = cast(Tuple, candidate)
            team = cast(Team, pair[0])
            
            color_bounds_check = TeamBoundsChecker.colorbounds_check(pair[1])
            if color_bounds_check.failure():
                return ValidationResult.failure(color_bounds_check.exception)
            
            team_color = cast(GameColor, pair[1])
            
            if team.schema.color != team_color:
                return ValidationResult.failure(
                    TeamColorInconsistencyException(f"{method}: {TeamColorInconsistencyException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(team_color)
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    def _basic_team_check(cls, candidate: Any) -> ValidationResult[Team]:
        """"""
        method = "TeamSpec._basic_team_check"
    
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamException(f"{method}: {NullTeamException.DEFAULT_MESSAGE}")
                )

            if not isinstance(candidate, Team):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a Team, got {type(candidate).__id__}")
                )
            return ValidationResult.success(cast(candidate, Team))
        except Exception as e:
            return ValidationResult.failure(e)
    
    @classmethod
    def _basic_tuple_check(cls, candidate: Any) -> ValidationResult[Team]:
        """"""
        method = "TeamSpec._basic_tuple_check"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamConsistencyTupleException(f"{method}: {NullTeamConsistencyTupleException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Tuple):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected a Tuple, got {type(candidate).__id__}")
                )
            
            return cls._basic_team_check(cast(Tuple)[0])
        except Exception as e:
            return ValidationResult.failure(e)
            
