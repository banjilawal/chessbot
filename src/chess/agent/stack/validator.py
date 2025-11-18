# src/chess/agent/stack/validator.py

"""
Module: chess.agent.stack.validator
Author: Banji Lawal
Created: 2025-08-25
version: 1.0.0
"""

from typing import Any, cast

from chess.agent import (
    TeamStack, CorruptedTeamStackException, InconsistentCurrentTeamException,
    InvalidTeamStackException, NullTeamStackException, TeamStackSizeConflictException
)
from chess.system import LoggingLevelRouter, Validator, ValidationResult


class TeamStackValidator(Validator[TeamStack]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[TeamStack]:
        
        method = "TeamStackValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamStackException(f"{method} {NullTeamStackException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, TeamStack):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected TeamStack, got {type(candidate).__name__} instead.")
                )
            
            team_stack = cast(TeamStack, candidate)
            
            if team_stack.size() > 0 and team_stack.is_empty():
                return ValidationResult.failure(
                    TeamStackSizeConflictException(
                        f"{method}: {TeamStackSizeConflictException.DEFAULT_MESSAGE}"
                    )
                )
            
            if team_stack.is_empty() and team_stack.current_team is not None:
                return ValidationResult.failure(
                    InconsistentCurrentTeamException(
                        f"{method}: {InconsistentCurrentTeamException.DEFAULT_MESSAGE}"
                    )
                )
            
            if team_stack.current_team is None and not team_stack.is_empty():
                return ValidationResult.failure(
                    InconsistentCurrentTeamException(
                        f"{method}: {InconsistentCurrentTeamException.DEFAULT_MESSAGE}"
                    )
                )
            
            if team_stack.items is None:
                return ValidationResult.failure(
                    CorruptedTeamStackException(
                        f"{method} {CorruptedTeamStackException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(payload=team_stack)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamStackException(
                    f"{method}: {InvalidTeamStackException.DEFAULT_MESSAGE}",
                    ex
                )
            )