# src/chess/agent/builder/factory.py

"""
Module: chess.agent.builder.factory
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Optional

from chess.engine import EngineService
from chess.game import UniqueGameDataService
from chess.team import UniqueTeamDataService
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter,ValidationResult, id_emitter

from chess.agent import (
    PlayerAgent, AgentBuildFailedException, AgentVariety, AgentValidator, HumanAgent, HumanAgentBuildFailedException,
    MachineAgent, MachineAgentBuildFailedException
)


class AgentFactory(Builder[PlayerAgent]):
    """
    # ROLE: Factory, Data Integrity Guarantor

    # RESPONSIBILITIES:
    1.  Produce PlayerAgent instances whose integrity is always guaranteed.
    2.  Manage construction of PlayerAgent instances that can be used safely by the client.
    3.  Ensure params for PlayerAgent creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.
    
    # PARENT:
        *   Builder

    # PROVIDES:
        *   build:  -> ValidationResult[HumanAgent|MachineAgent]

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    def build(
            cls,
            name: str,
            id: id_emitter.agent_id,
            agent_variety: AgentVariety,
            engine_service: Optional[EngineService] = None,
            agent_validator: AgentValidator = AgentValidator(),
    ) -> BuildResult[HumanAgent|MachineAgent]:
        """
        # ACTION:
        1.  verify agent_variety is a not-null AgentVariety object.
        2.  Use agent_variety to pick which factory method will create the concrete PlayerAgent object.

        # PARAMETERS:
            *   id (int)
            *   designation (str)
            *   agent_variety (AgentVariety)
            *   engine_service (Optional[EngineService])

        # Returns:
        ValidationResult[PlayerAgent] containing either:
            - On success: PlayerAgent in the payload.
            - On failure: Exception.

        # Raises:
            *   AgentBuildFailedException
        """
        method = "AgentBuilder.build"
        try:
            # Ensure the agent_variety is the correct type and not null.
            variety_validation = agent_validator.certify_agent_variety(candidate=agent_variety)
            if variety_validation.failure():
                return BuildResult.failure(variety_validation.exception)
            # Use agent_variety to decide which factory method to call.
            
            if isinstance(agent_variety, HumanAgent):
                return cls.build_human_agent(id=id, name=name, )
            
            # Machine player_agent requires an engine_service.
            if isinstance(agent_variety, MachineAgent):
                return cls.build_machine_agent(id=id, name=name, engine_service=engine_service)
        
        # The flow should only get here if the logic did not route all the types of concrete Agents.
        # In that case wrap the unhandled exception inside an AgentBuildFailedException then, return
        # the exception chain inside a ValidationResult.
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                AgentBuildFailedException(
                    ex=ex, message=f"{method}: {AgentBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_human_agent(
            cls,
            id: int,
            name: str,
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[HumanAgent]:
        """
        # ACTION:
        1.  On successfully certifying the id and designation create HumanAgent and return in BuildResult's
            payload. Otherwise, return a BuildResult containing an exception.

        # PARAMETERS:
            *   id (int)
            *   designation (str)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[HumanAgent] containing either:
            - On success: HumanAgent in the payload.
            - On failure: Exception.

        # Raises:
            *   HumanAgentBuildFailedException
        """
        method = "AgentBuilder.build_human_agent"
        try:
            # Only need to certify the designation and id are correct.
            validation = identity_service.validate_identity(id_candidate=id, name_candidate=name)
            if validation.is_failure():
                return BuildResult.failure(validation.exception)
            # On success return the HumanAgent in a BuildResult payload.
            return BuildResult.success(
                payload=HumanAgent(
                    id=id,
                    name=name,
                    games=UniqueGameDataService(),
                    team_assignments=UniqueTeamDataService(),
                )
            )
        
        # Finally, if some exception unrelated to identity verification is raised wrap it inside a
        # HumanAgentBuildFailedException then, send the exception chain inside a BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                HumanAgentBuildFailedException(
                    ex=ex, message=f"{method}: {HumanAgentBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_machine_agent(
            cls,
            name: str,
            id: int = id_emitter.service_id,
            engine_service: EngineService = EngineService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[MachineAgent]:
        """
        # ACTION:
        1.  Certifying the id and designation and designation are safe with identity_service.
        2.  Use engine_service_validator to ensure the engine_service has all the required components.

        # PARAMETERS:
            *   id (int)
            *   designation (str)
            *   engine_service (EngineService)
            *   identity_service (IdentityService)
            *   engine_service_validator (EngineServiceValidator)

        # Returns:
        ValidationResult[MachineAgent] containing either:
            - On success: MachineAgent in the payload.
            - On failure: Exception.

        # Raises:
            *   MachineAgentBuildFailedException
        """
        method = "AgentBuilder.build_machine_agent"
        try:
            # Certify the id and designation are safe.
            identity_validation = identity_service.validate_identity(id_candidate=id, name_candidate=name)
            if identity_validation.is_failure():
                return BuildResult.failure(identity_validation.exception)
            
            # Certify the engine_service has all the required components
            engine_service_validation = engine_service.validator.validate(candidate=engine_service)
            if engine_service_validation.is_failure():
                return BuildResult.failure(engine_service_validation.exception)
            # When all checks pass send a MachineAgent back.
            return BuildResult.success(
                MachineAgent(
                    id=id,
                    name=name,
                    engine_service=engine_service,
                    games=UniqueGameDataService(),
                    team_assignments=UniqueTeamDataService(),
                )
            )
        
        # Finally, if some exception unrelated to identity verification is raised wrap it inside a
        # MachineAgentBuildFailedException then, send the exception chain inside a BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                MachineAgentBuildFailedException(
                    ex=ex, message=f"{method}: {MachineAgentBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
