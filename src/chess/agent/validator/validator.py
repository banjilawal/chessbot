# src/chess/agent/validator/validator.py

"""
Module: chess.agent.validator.validator
Author: Banji Lawal
Created: 2025-08-31
version: 1.0.0
"""

from typing import Any, cast

from chess.agent import (
    Agent, AgentVariety, InvalidAgentException, NullAgentException, NullAgentTypeException,
    TeamStackServiceValidator
)
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator


class AgentValidator(Validator[Agent]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            identity_service: IdentityService = IdentityService(),
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
        method = "AgentValidator.validate"
        
        try:
            # If candidate is validation no point continuing
            if candidate is None:
                return ValidationResult.failure(
                    NullAgentException(f"{method}: {NullAgentException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Agent):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: Expected Agent, "
                        f"got {type(candidate).__name__} instead."
                    )
                )
            
            agent = cast(Agent, candidate)
            
            identity_validation = identity_service.validate_identity(agent.id, agent.name)
            if identity_validation.is_failure():
                return ValidationResult.failure(identity_validation.exception)
            
            return ValidationResult.success(agent)
        except Exception as ex:
            raise ValidationResult.failure(
                InvalidAgentException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{InvalidAgentException.DEFAULT_MESSAGE}"
                    )
                )
            )
    #
    # @classmethod
    # @LoggingLevelRouter.monitor
    # def certify_agent_variety(cls, candidate: Any) -> ValidationResult[AgentVariety]:
    #     """"""
    #     method = "AgentValidator.validate_agent_category"
    #     try:
    #         if candidate is None:
    #             return ValidationResult.failure(
    #                 NullAgentTypeException(
    #                     f"{method}: {NullAgentTypeException.DEFAULT_MESSAGE}"
    #                 )
    #             )
    #
    #         if not isinstance(candidate, AgentCategory):
    #             return ValidationResult.failure(
    #                 TypeError(
    #                     f"{method}: Expected AgentCategory, "
    #                     f"got {type(candidate).__name__} instead."
    #                 )
    #             )
    #
    #         return ValidationResult.success(cast(AgentType, candidate))
    #
    #     except Exception as ex:
    #         return ValidationResult.failure(
    #             InvalidAgentException(
    #                 ex=ex,
    #                 message=(
    #                     f"{method}: "
    #                     f"{InvalidAgentException.DEFAULT_MESSAGE}"
    #                 )
    #             )
    #         )