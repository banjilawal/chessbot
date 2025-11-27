# src/chess/agent/builder.py

"""
Module: chess.agent.builder
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""

from typing import Optional

from chess.team import UniqueTeamDataService
from chess.engine.service import EngineService
from chess.agent import Agent, AgentBuildFailedException, AgentVariety, AgentValidator, HumanAgent, MachineAgent
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter, ValidationResult, id_emitter


class AgentFactory(Builder[Agent]):
        """
        # ROLE: Builder, Data Integrity Guarantor

        # RESPONSIBILITIES:
        Produce Agent instances whose integrity is always guaranteed. If any attributes do not pass
        their integrity checks, send an exception instead of an unsafe Agent.

        # PROVIDES:
        BuildResult[Agent] containing either:
            - On success: Agent in the payload.
            - On failure: Exception.

        # ATTRIBUTES:
        None
        """
        
        @classmethod
        def build(
                cls,
                id: int,
                name: str,
                variety: AgentVariety,
                agent_validator: AgentValidator = AgentValidator(),
                identity_service: IdentityService = IdentityService(),
                team_stack: UniqueTeamDataService = UniqueTeamDataService(),
                engine_service: Optional[EngineService] = None,
        ) -> BuildResult[Agent]:
            """
            # ACTION:
            1.  Call _validate_build_params. to verify inputs are safe.
            2.  If the _validate params returns failure include the failure in a BuildResult.
            3.  If the engine is not validation call build_machine_agent. Otherwise, call build_human_agent.

            # PARAMETERS:
                *   id (int)
                *   name (str)
                *   identity_service (IdentityService)
                *   team_stack (teamStackService)
                *   engine_service (Optional[EngineService])

            # Returns:
            ValidationResult[TeamStackService] containing either:
                - On success: TeamStackService in the payload.
                - On failure: Exception.

            # Raises:
                *   AgentBuildFailedException
            """
            method = "AgentBuilder.build"
            
            try:
                variety_validation = agent_validator.certify_agent_variety(candidate=variety)
                if variety_validation.failure():
                    return BuildResult.failure(variety_validation.exception)
                
                if variety == AgentVariety.MACHINE_AGENT and engine_service is None:
                    return BuildResult.failure(
                        AgentBuildFailedException(
                            f"{method}: Cannot build a MachineAgent "
                            f"without an EngineService instance."
                        )
                    )
                
                if variety == AgentVariety.MACHINE_AGENT and engine_service is not None:
                    return cls.build_machine_agent(
                        id=id,
                        name=name,
                        team_stack=team_stack,
                        engine_service=engine_service,
                        identity_service=identity_service,
                    )
                
                return cls.build_human_agent(
                    id=id,
                    name=name,
                    team_stack=team_stack,
                    identity_service=identity_service,
                )
            
            except Exception as ex:
                return BuildResult.failure(
                    AgentBuildFailedException(
                        ex=ex,
                        message=(
                            f"{method}: "
                            f"{AgentBuildFailedException.DEFAULT_MESSAGE}"
                        )
                    )
                )
        
        @classmethod
        @LoggingLevelRouter.monitor
        def build_human_agent(
                cls,
                name: str,
                id: int = id_emitter.service_id,
                identity_service: IdentityService = IdentityService(),
                team_stack: UniqueTeamDataService = UniqueTeamDataService(),
        ) -> BuildResult[HumanAgent]:
            """"""
            method = "AgentBuilder.build_human_agent"
            
            try:
                validation_result = identity_service.validate_identity(
                    id_candidate=id,
                    name_candidate=name
                )
                if validation_result.is_failure():
                    return BuildResult.failure(validation_result.exception)
                
                return BuildResult.success(
                    HumanAgent(id=id, name=name, team_stack=team_stack)
                )
            except Exception as ex:
                return BuildResult.failure(
                    AgentBuildFailedException(
                        ex=ex,
                        message=(
                            f"{method}: "
                            f"{AgentBuildFailedException.DEFAULT_MESSAGE}"
                        )
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
                team_stack: UniqueTeamDataService = UniqueTeamDataService(),
        ) -> BuildResult[HumanAgent]:
            """"""
            method = "AgentBuilder.build_machine_agent"
            
            try:
                validation_result = identity_service.validate_identity(
                    id_candidate=id,
                    name_candidate=name
                )
                if validation_result.is_failure():
                    return BuildResult.failure(validation_result.exception)
                
                return BuildResult.success(
                    MachineAgent(
                        id=id,
                        name=name,
                        team_stack=team_stack,
                        engine_service=engine_service
                    )
                )
            except Exception as ex:
                return BuildResult.failure(
                    AgentBuildFailedException(
                        ex=ex,
                        message=(
                            f"{method}: "
                            f"{AgentBuildFailedException.DEFAULT_MESSAGE}"
                        )
                    )
                )
