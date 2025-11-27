# src/chess/agent/validator/validator.py

"""
Module: chess.agent.validator.validator
Author: Banji Lawal
Created: 2025-08-31
version: 1.0.0
"""

from typing import Any, cast

from chess.engine.service import EngineService
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.agent import (
    Agent, AgentVariety, AgentVarietyNullException, InvalidAgentException, MachineAgent, NullAgentException,
)



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
                    TypeError(f"{method}: Expected Agent, {type(candidate).__name__} instead.")
                )
            
            agent = cast(Agent, candidate)
            
            identity_validation = identity_service.validate_identity(agent.id, agent.name)
            if identity_validation.is_failure():
                return ValidationResult.failure(identity_validation.exception)
            
            if isinstance(agent, MachineAgent):
                return cls._certify_machine_engine(machine=agent, engine_candidate=agent.engine_service)
            
            return ValidationResult.success(agent)
        except Exception as ex:
            return ValidationResult.failure(
                InvalidAgentException(ex=ex, message=f"{method}: {InvalidAgentException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def certify_variety(cls, candidate: Any) -> ValidationResult[AgentVariety]:
        method = "AgentValidator.certify_variety"
        try:
            if candidate is None:
                return ValidationResult.failure(
                    AgentVarietyNullException(f"{method}: {AgentVarietyNullException.DEFAULT_MESSAGE}")
                )

            if candidate not in [AgentVariety.HUMAN_AGENT, AgentVariety.MACHINE_AGENT]:
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected AgentVariety,  {type(candidate).__name__} instead.")
                )
            
            return ValidationResult.success(cast(AgentVariety, candidate))
        except Exception as ex:
            return ValidationResult.failure(
                InvalidAgentException(ex=ex, message=f"{method}: {InvalidAgentException.DEFAULT_MESSAGE}")
            )
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def certify_machine_engine(
            cls,
            machine: MachineAgent,
            engine_candidate: Any,
            engine_service: EngineService = EngineService(),
    ) -> ValidationResult[Agent]:
        method = "AgentValidator.certify_machine_engine"
        try:
            engine_validation = engine_service.validate_engine(engine_candidate)
            if engine_validation.is_failure():
            
        except Exception as ex:
        return ValidationResult.failure(
            InvalidAgentException(ex=ex, message=f"{method}: {InvalidAgentException.DEFAULT_MESSAGE}")
        )
    
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