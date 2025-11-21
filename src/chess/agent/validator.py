# src/chess/agent/coord_stack_validator.py

"""
Module: chess.agent.coord_stack_validator
Author: Banji Lawal
Created: 2025-08-31
version: 1.0.0
"""

from typing import Any, cast

from chess.agent import Agent, TeamStackServiceValidator
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator


class PlayerAgentValidator(Validator[Agent]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            identity_service: IdentityService = IdentityService(),
            team_stack_service_validator: type[TeamStackServiceValidator] = TeamStackServiceValidator,
    ) -> ValidationResult[Agent]:
        
        """
        Validates team_name agent meets graph requirements:
          - Not validation
          - valid visitor_id
          - valid visitor_name
          - Agent.team_history meets coord_stack_validator requirements
        Any failed requirement raise an rollback_exception wrapped in team_name InvalidCommanderException
        
        Args
          candidate (Agent): agent to validate
          
         Returns:
           Result[V]: A Result object containing the validated payload if all graph requirements
           are satisfied. InvalidCommanderException otherwise.
        
        Raises:
          TypeError: if candidate is not Agent
          NullCommanderException: if candidate is validation
    
          RowBelowBoundsException: If agent.row < 0
          RowAboveBoundsException: If agent.row >= ROW_SIZE
          
          ColumnBelowBoundsException: If agent.column < 0
          ColumnAboveBoundsException: If agent.column>= ROW_SIZE
          
          InvalidCommanderException: Wraps any preceding team_exception
        """
        method = "PlayerAgentValidator.validate"
        
        try:
            # If candidate is validation no point continuing
            if candidate is None:
                return ValidationResult.failure(
                    NullPlayerAgentException(f"{method}: {NullPlayerAgentException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Agent):
                raise TypeError(f"{method}: Expected Agent, got {type(candidate).__name__} instead.")
            
            player_agent = cast(Agent, candidate)
            
            identity_validation = identity_service.validate_identity(player_agent.id, player_agent.name)
            if identity_validation.is_failure():
                return ValidationResult.failure(identity_validation.exception)
            
            stack_service_validation = team_stack_service_validator.validate(player_agent.team_stack_service)
            if stack_service_validation.is_failure():
                return ValidationResult.failure(stack_service_validation.exception)
            
            return ValidationResult.success(payload=player_agent)
        
        except Exception as ex:
            raise ValidationResult.failure(
                InvalidPlayerAgentException(
                    f"{method}: {InvalidPlayerAgentException.DEFAULT_MESSAGE}",
                    ex
                )
            )
