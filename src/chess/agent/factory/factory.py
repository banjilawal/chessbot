# src/chess/agent/builder.py

"""
Module: chess.agent.builder
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""

from typing import Optional

from chess.team import UniqueTeamDataService
from chess.game import UniqueGameDataService
from chess.engine.service import EngineService
from chess.agent import (
    Agent, AgentBuildFailedException, AgentContext, AgentContextBuildFailedException, AgentVariety,
    AgentValidator, HumanAgent, MachineAgent, NoAgentContextFlagException, TooManyAgentContextFlagsException
)
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
                name: str,
                id: id_emitter.agent_id,
                agent_variety: AgentVariety,
                engine_service: Optional[EngineService] = None,
        ) -> BuildResult[Agent]:
            """
            # ACTION:
            1.  verify agent_variety is a not-null AgentVariety object.
            2.  Use agent_variety to pick which factory method will create the concrete Agent object.

            # PARAMETERS:
                *   id (int)
                *   name (str)
                *   agent_variety (AgentVariety)
                *   engine_service (Optional[EngineService])

            # Returns:
            ValidationResult[Agent] containing either:
                - On success: Agent in the payload.
                - On failure: Exception.

            # Raises:
                *   AgentBuildFailedException
            """
            method = "AgentBuilder.build"
            try:
                # Ensure the agent_variety is the correct type and not null.
                variety_validation = agent_validator.certify_variety(candidate=agent_variety)
                if variety_validation.failure():
                    return BuildResult.failure(variety_validation.exception)
                # Use agent_variety to decide which factory method to call.
                if isinstance(agent_variety, HumanAgent):
                    return cls.build_human_agent(id=id, name=name,)
                # Machine agent requires an engine_service.
                if isinstance(agent_variety, MachineAgent):
                    return cls.build_machine_agent(id=id, name=name, engine_service=engine_service)
                
            # The flow should only get here if the logic did not route all the types of concrete Agents.
            # In that case wrap the unhandled exception inside an AgentBuildFailedException then, return
            # the exception chain inside a ValidationResult.
            # then return the exceptions inside a ValidationResult.
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
            1.  On successfully certifying the id and name create HumanAgent and return in BuildResult's
                payload. Otherwise, return a BuildResult containing an exception.

            # PARAMETERS:
                *   id (int)
                *   name (str)
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
                # Only need to certify the name and id are correct.
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
                        ex=ex, message=f"{method}:{HumanAgentBuildFailedException.DEFAULT_MESSAGE}"
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
            1.  Certifying the id and name and name are safe with identity_service.
            2.  Use engine_service_validator to ensure the engine_service has all the required components.

            # PARAMETERS:
                *   id (int)
                *   name (str)
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
                # Certify the id and name are safe.
                identity_validation = identity_service.validate_identity(id_candidate=id, name_candidate=name)
                if identity_validation.is_failure():
                    return BuildResult.failure(identity_validation.exception)
                # Certify the engine_service has all the required components
                engine_service_validation = engine_service_validator.validate(candidate=engine_service)
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


@classmethod
@LoggingLevelRouter.monitor
def _verify_build_attributes(
        cls,
        id: int,
        name: str,
        variety: AgentVariety,
        engine_service: Optional[EngineService],
        identity_service: IdentityService = IdentityService(),
) -> ValidationResult[(int, str, AgentVariety, Optional[EngineService])]:
    """
    # ACTION
    validate_build_attributes. This decouples verification logic from build logic so
    each factory method can run independently and build can direct which product
    should be manufactured.
    """
    method = "AgentFactory._verify_build_attributes"
    try:
        # Start the error detection process.
        identity_validation = identity_service.validate_identity(id_candidate=id, name_candidate=name)
        if identity_validation.is_failure():
            return BuildResult.failure(identity_validation.exception)
        
        rank_validation = rank_certifier.item_validator.validate(candidate=rank)
        if rank_validation.is_failure():
            return BuildResult.failure(rank_validation.exception)
        
        team_validation = team_certifier.item_validator.validate(candidate=team)
        if team_validation.is_failure():
            return BuildResult.failure(team_validation.exception)
        
        square_validation = square_certifier.item_validator.validate(candidate=opening_square)
        if square_validation.is_failure():
            return BuildResult.failure(square_validation.exception)
        
        roster_number_validation = identity_service.validate_id(candidate=roster_number)
        if roster_number_validation.is_failure():
            return BuildResult.failure(roster_number_validation.exception)
        
        # If no errors are detected return the successfully validated (id, name, rank, team) tuple.
        return ValidationResult.success((id, name, rank, team, roster_number, opening_square))
    
    # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
    # then return the exceptions inside a ValidationResult.
    except Exception as ex:
        return ValidationResult.failure(
            PieceBuildFailedException(ex=ex, message=f"{method}: {PieceBuildFailedException.DEFAULT_MESSAGE}")
        )