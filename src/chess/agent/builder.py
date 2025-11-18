# src/chess/agent/build.py

"""
Module: chess.agent.build
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""


from typing import Optional


from chess.engine.service import EngineService
from chess.agent import Agent, HumanAgent, MachineAgent, AgentBuildFailed, TeamStackService
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter, ValidationResult



class AgentBuilder(Builder[Agent]):
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
            identity_service: IdentityService = IdentityService(),
            team_stack_service: TeamStackService=TeamStackService(),
            engine_service: Optional[EngineService] = None,
    ) -> BuildResult[Agent]:
        """
        # ACTION:
        1.  Call _validate_build_params. to verify inputs are safe.
        2.  If the _validate params returns failure include the failure in a BuildResult.
        3.  If the engine is not null call build_machine_agent. Otherwise, call build_human_agent.

        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   identity_service (IdentityService)
            *   team_stack_service (teamStackService)
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
            params_validation = cls._validate_params(
                id=id,
                name=name,
                identity_service=identity_service,
            )
            
            if engine_service is not None:
                return cls._build_machine_agent(
                    id=id,
                    name=name,
                    identity_service=identity_service,
                    team_stack_service=team_stack_service,
                    engine_service=engine_service,
                )
            
            return cls.build_human_agent(
                id=id,
                name=name,
                identity_service=identity_service,
                team_stack_service=team_stack_service,
            )
        
        except Exception as ex:
            return BuildResult.failure(
                AgentBuildFailedException(
                    f"{method}: {PlayerAgentBuildFailed.DEFAULT_MESSAGE}",
                    ex
                )
            )
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_machine_agent(
            cls,
            id: int,
            name: str,
            identity_service: IdentityService = IdentityService(),
            team_stack_service: TeamStackService = TeamStackService(),
            engine_service: EngineService = EngineService(),
    ) -> BuildResult[MachineAgent]:
        try:
            param_validation = cls._validate_params(id=id, name=name, identity_service=identity_service)
            if param_validation.is_failure():
                return BuildResult.failure(param_validation.exception)
            
            return BuildResult.success(
                MachineAgent(
                    id=id,
                    name=name,
                    team_stack_service=team_stack_service,
                    engine_service=engine_service
                )
            )
        except Exception as ex:
            return BuildResult.failure(
                AgentBuildFailedException(
                    "f{method}: {PlayerAgentBuildFailed.DEFAULT_MESSAGE}",
                    ex
                )
            )
        
        
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_params(
            cls,
            id: int,
            name: str,
            identity_service: IdentityService
    ) -> ValidationResult[(int, str)]:
        try:
            return identity_service.validate_identity(id_candidate=id, name_candidate=name)
        except Exception as ex:
            return ValidationResult.failure(ex)
#
#
# def main():
#   build_result = AgentBuilder.build(commander_id=id_emitter.person_id, visitor_name=RandomName.person())
#   if build_result.is_success():
#     competitor = build_result.payload
#     print(f"Successfully built competitor: {competitor}")
#   else:
#     print(f"Failed to build competitor: {build_result.err}")
#
#   build_result = AgentBuilder.build(-1, 4)
#   if build_result.is_success():
#     competitor = build_result.payload
#     print(f"Successfully built competitor: {competitor}")
#   else:
#     print(f"Failed to build competitor: {build_result.err}")
#
# if __name__ == "__main__":
#   main()
