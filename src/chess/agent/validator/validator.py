# src/chess/agent/validator/validator.py

"""
Module: chess.agent.validator.validator
Author: Banji Lawal
Created: 2025-08-31
version: 1.0.0
"""

from typing import Any, cast

from chess.engine.service import EngineService
from chess.system import IdentityService, LoggingLevelRouter, ServiceValidator, ValidationResult, Validator
from chess.agent import (
    Agent, AgentVariety, AgentVarietyNullException, HumanAgent, InvalidAgentException, InvalidAgentVarietyException,
    InvalidMachineAgentException, MachineAgent, NullAgentException,
)
from chess.team import UniqueTeamDataService


class AgentValidator(Validator[Agent]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security., Data Integrity Guarantor.

    # RESPONSIBILITIES:
    Verifies a candidate is an instance of Agent that is safe to use.

    # PARENT
        *   Validator

    # PROVIDES:
    ValidationResult[Agent] containing either:
        - On success: Agent in the payload.
        - On failure: Exception.

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            idservice: IdentityService = IdentityService(),
            service_validator: ServiceValidator = ServiceValidator(),
    ) -> ValidationResult[Agent]:
        """
        # ACTION:
        1.  Verify the candidate is not null.
        2.  Verify the candidate is an Agent. If so cast it to an Agent instance.
        3.  Use the identity service to verify the agent's name and id.
        4.  If the agent is a MachineAgent, confirm agent.engine_service is not null and
            is an EngineService instance.
        5.  Confirm agent.team_assignments is not null and is an UniqueTeamDataService instance.
        6.  Confirm agent.games is not null and is an UniqueGameDataService instance.
        7.  If any check fails, return the exception inside a ValidationResult.
        8.  When all checks return the successfully validated Agent instance inside a ValidationResult.
        
        # PARAMETERS:
            *   candidate (Any)
            *   identity_service (IdentityService)
            *   service_validator (ServiceValidator)

        # Returns:
        ValidationResult[Agent] containing either:
            - On success: Agent in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NullAgentException
            *   InvalidAgentException
        """
        method = "AgentValidator.validate"
        try:
            # If candidate is validation no point continuing
            if candidate is None:
                return ValidationResult.failure(
                    NullAgentException(f"{method}: {NullAgentException.DEFAULT_MESSAGE}")
                )
            # Handle the case, the candidate is not an Agent object.
            if not isinstance(candidate, Agent):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Agent, {type(candidate).__name__} instead.")
                )
            # Cast to an Agent for additional processing.
            agent = cast(Agent, candidate)
            
            # Verify the id and name are safe.
            identity_validation = idservice.validate_identity(agent.id, agent.name)
            if identity_validation.is_failure():
                return ValidationResult.failure(identity_validation.exception)
            
            # Certify the agent's TeamDataService is correct.
            team_data_service_certification = service_validator.validate(candidate=agent.team_assignments)
            if team_data_service_certification.is_failure():
                return ValidationResult.failure(team_data_service_certification.exception)
            
            # Certify the agent's GameDataService is correct.
            game_data_service_certification = service_validator.validate(candidate=agent.games)
            if game_data_service_certification.is_failure():
                return ValidationResult.failure(game_data_service_certification.exception)
            
            # If the agent is a MachineAgent handoff control to certify_machine_agent_engine
            # for the final check.
            if isinstance(agent, MachineAgent):
                return cls._certify_machine_agent_engine(machine=cast(MachineAgent, agent))
            
            # If the agent is a HumanAgent all the checks have been passed. Return the
            # agent in the ValidationResult payload.
            if isinstance(agent, HumanAgent):
                return ValidationResult.success(payload=cast(HumanAgent, agent))
            
            # Any unexpected boundary conditions are caught and wrapped in an InvalidAgentException then,
            # the exception chain is returned inside a ValidationResult. The flow should only get here if
            # the logic does not handle each concrete Agent subclass.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidAgentException(ex=ex, message=f"{method}: {InvalidAgentException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def certify_agent_variety(cls, candidate: Any) -> ValidationResult[AgentVariety]:
        """
        # ACTION:
        This is just a decorator that encapsulates all the logic for making sure an object being
        passed as an AgentVariety is not null and is actually an AgentVariety object. The comments
        are almost as lomg as the code.
        
        1.  Verify the candidate is not null.
        2.  Verify the candidate is an AgentVariety. cast into an AgentVariety instance and return a success.
        3.  If any check fails, return the exception inside a ValidationResult.

        # PARAMETERS:
            *   candidate (Any)

        # Returns:
        ValidationResult[AgentVariety] containing either:
            - On success: AgentVariety in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NullAgentVarietyException
            *   InvalidAgentVarietyException
        """
        method = "AgentValidator.certify_variety"
        try:
            # Handle the null case.
            if candidate is None:
                return ValidationResult.failure(
                    AgentVarietyNullException(f"{method}: {AgentVarietyNullException.DEFAULT_MESSAGE}")
                )
            #Handle the incorrect type case
            if not isinstance(candidate, AgentVariety):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected AgentVariety,  {type(candidate).__name__} instead.")
                )
            # Cast and return.
            return ValidationResult.success(cast(AgentVariety, candidate))
        
        # If there is unhandled error-raising boundary condition wrap it inside an
        # InvalidAgentVarietyException then, send the exception chain in a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidAgentVarietyException(
                    ex=ex, message=f"{method}: {InvalidAgentVarietyException.DEFAULT_MESSAGE}"
                )
            )
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _certify_machine_agent_engine(
            cls,
            machine_agent: MachineAgent,
            engine_service_validator: EngineService = EngineService(),
    ) -> ValidationResult[Agent]:
        """
        # ACTION:
        1.  If machine.engine_service passes certification, return the machine inside a ValidationResult.
            Otherwise, send the exception in the ValidationResult..

        # PARAMETERS:
            *   machine (MachineAgent)
            *   engine_service_validator (EngineService)

        # Returns:
        ValidationResult[Agent] containing either:
            - On success: Agent in the payload.
            - On failure: Exception.

        # RAISES:
            *   InvalidMachineAgentException
        """
        method = "AgentValidator.certify_machine_agent_engine"
        try:
            engine_validation = engine_service_validator.validate_engine(machine_agent.engine_service)
            if engine_validation.is_failure():
                return ValidationResult.failure(engine_validation.exception)
            # On success just return the machineAgent
            return ValidationResult.success(payload=machine_agent)
        
        # If there is unhandled error-raising boundary condition wrap it inside an
        # InvalidAgentMachineException then, send the exception chain in a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidMachineAgentException(
                    ex=ex, message=f"{method}: {InvalidMachineAgentException.DEFAULT_MESSAGE}"
                )
            )